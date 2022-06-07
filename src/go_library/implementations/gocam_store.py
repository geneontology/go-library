import inspect
from collections import Iterator
from copy import deepcopy
from dataclasses import dataclass
from pathlib import Path
from typing import List, Dict

from go_library.datamodel.gocam_queries import ModelInteraction, ModelQuery
from linkml_dataops.query.queryengine import QueryEngine
from linkml_runtime import CurieNamespace, SchemaView
from linkml_runtime.dumpers import yaml_dumper
from oaklib.datamodels.vocabulary import DEFAULT_PREFIX_MAP
from oaklib.implementations.sparql.abstract_sparql_implementation import _sparql_values
from oaklib.implementations.sparql.sparql_query import SparqlQuery
from oaklib.implementations.ubergraph import UbergraphImplementation
from oaklib.interfaces.basic_ontology_interface import PREFIX_MAP
from oaklib.types import CURIE

import go_library
import go_library.datamodel.gocam as gocam_dm
from go_library.datamodel.gocam import Model
from oaklib.utilities.iterator_utils import chunk_to_lists
from rdflib import URIRef

from sparqlfun.query_engine import SparqlEngine


@dataclass
class GoCamStore(UbergraphImplementation, QueryEngine):
    """
    Implementation for GO-CAM queries

    """
    gocam_queries_sv: SchemaView = None
    sparqlfun_engine: SparqlEngine = None

    def __post_init__(self):
        super().__post_init__()
        root_path = Path(inspect.getfile(go_library))
        schema_path = root_path.parent / '../../src/linkml/gocam_queries.yaml'
        self.gocam_queries_sv = SchemaView(str(schema_path))
        self.sparqlfun_engine = SparqlEngine(endpoint='go',
                                             schema_view=self.gocam_queries_sv)

    def _default_url(self) -> str:
        return "http://rdf.geneontology.org/sparql"


    def add_prefixes(self, pm: PREFIX_MAP, prefixes: List[CurieNamespace]) -> PREFIX_MAP:
        for p in prefixes:
            pm[p.prefix] = str(p)
        return pm


    def get_prefix_map(self) -> PREFIX_MAP:
        pm = deepcopy(super().get_prefix_map())
        return self.add_prefixes(pm, [gocam_dm.GOMODEL])

    def instances(self, class_curie: CURIE) -> Iterator[CURIE]:
        class_uri = self.curie_to_sparql(class_curie)
        query = SparqlQuery(select=['?s'],
                            distinct=True,
                            where=[f'?s rdf:type {class_uri}'])
        bindings = self._query(query.query_str())
        for row in bindings:
            yield self.uri_to_curie(row['s']['value'])

    def all_models(self) -> Iterator[CURIE]:
        query = SparqlQuery(select=['?s'],
                            distinct=True,
                            where=[f'?s <{gocam_dm.slots.state.uri}> ?o'])
        print(query.query_str())
        bindings = self._query(query.query_str())
        for row in bindings:
            yield self.uri_to_curie(row['s']['value'])

    def get_models_by_curies(self, curies: List[CURIE]) -> Iterator[Model]:
        query = SparqlQuery(select=['?s ?p ?o'],
                            distinct=True,
                            where=['?s ?p ?o',
                                   _sparql_values('s', [self.curie_to_sparql(s) for s in curies])])
        print(query.query_str())
        models = {}
        bindings = self._query(query)
        for row in bindings:
            id = self.uri_to_curie(row['s']['value'])
            if id in models:
                m = models[id]
            else:
                m = Model(id=id)
                models[id] = m
            p = URIRef(row['p']['value'])
            o = row['o']['value']
            # TODO: use generic approach for this
            if p == gocam_dm.slots.title.uri:
                m.title = o
            elif p == gocam_dm.slots.state.uri:
                m.state = o
        for m in models.values():
            yield m

    def search_models(self,
                      search_term: str = None) -> Iterator[Model]:
        preds = [gocam_dm.slots.title.uri]
        where = [f'?s ?p ?v ',
                 f'?v bds:search "{search_term}"',
                 f'?s <{gocam_dm.slots.state.uri}> ?model_state',
                _sparql_values('p', [self.curie_to_sparql(p) for p in preds])]
        query = SparqlQuery(select=['?s ?model_state'],
                            where=where)
        bindings = self._query(query)
        for rows in chunk_to_lists(bindings):
            model_ids = [self.uri_to_curie(row['s']['value']) for row in rows]
            for model in self.get_models_by_curies(model_ids):
                yield model

    def causally_connected_enablers(self) -> Iterator:
        pass
        #query = SparqlQuery(select=['?s ?p ?o'],
        #                    where=where)

    def query_model_ids(self, **kwargs) -> Iterator[CURIE]:
        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        for result in self.sparqlfun_engine.query(ModelQuery, predicate='lego:modelstate', **kwargs).results:
            print(yaml_dumper.dumps(result))
            yield result.id

    def all_model_interactions(self, model_id=None, **kwargs) -> Iterator[ModelInteraction]:
        for model_id in self.query_model_ids(id=model_id, **kwargs):
            print(f'MODEL={model_id}')
            for result in self.sparqlfun_engine.query(ModelInteraction, model_id=model_id).results:
                yield result










