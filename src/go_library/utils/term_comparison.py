from dataclasses import dataclass
from typing import List

from go_library.datamodel.amigo_solr import Annotation, Bioentity
from go_library.datamodel.amigo_solr_api import AmigoSolrAPI
from oaklib import BasicOntologyInterface
from oaklib.types import CURIE


@dataclass
class TermComparisonEngine:
    """
    A class to compare two terms and determine if they are the same.
    """
    ontology_adapter: BasicOntologyInterface = None
    amigo: AmigoSolrAPI = None
    facet_fields = ['evidence_type']

    def compare(self, terms: List[CURIE], taxon: CURIE = None) -> dict:
        """
        Compare two terms and determine if they are the same.

        :param term1: First term
        :param term2: Second term
        :param taxon: Taxon
        :return: Summary
        """
        summaries = {}
        for term in terms:
            solr_params = {'facet': 'on',
                           'facet.mincount': 1,
                           'facet.field': self.facet_fields,
                           'rows': 0,
                           }
            results = self.amigo.query_engine.search(Annotation,
                                                      solr_params=solr_params,
                                                     isa_partof_closure=term,
                                                     taxon=taxon)
            summary = self.summarize(results)
            summaries[term] = summary
            solr_params = {
                           'rows': 10000,
                           }
            results = self.amigo.query_engine.search(Bioentity,
                                                     solr_params=solr_params,
                                                     isa_partof_closure=term,
                                                     taxon=taxon)
            summary['bioentities'] = results.num_found
        return summaries


    def summarize(self, results) -> dict:
        """
        Summarize the results of a query

        :param results: Results of a query
        :return: Summarized results
        """
        r = {'annotations': results.num_found}
        for facet in self.facet_fields:
            if facet == 'evidence_type':
                r['IBA'] = results.facet_counts[facet].get('IBA', 0)
            else:
                r[facet] = results.facet_counts[facet]
        return r



