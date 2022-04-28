import inspect
import os
import pkgutil
from pathlib import Path

import go_library
from go_library.datamodel.gocam_queries import ModelInfo, ModelStateEnum, ModelQuery
from go_library.implementations.gocam_store import GoCamStore
import unittest

from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper
from rdflib import Literal, URIRef

from tests import BIOLOGICAL_PROCESS, NUCLEOLUS, DMEL_EGFR_MODEL


class TestQuery(unittest.TestCase):

    def setUp(self):
        self.oi = GoCamStore()

    def test_lookup(self):
        oi = self.oi
        label = oi.get_label_by_curie(BIOLOGICAL_PROCESS)
        print(label)
        self.assertEqual(label, "biological_process")
        self.assertEqual([BIOLOGICAL_PROCESS], oi.get_curies_by_label(label))

    def test_search(self):
        oi = self.oi
        results = list(oi.basic_search("nucleolus"))
        for c, n in oi.get_labels_for_curies(results):
            print(f'{c} ! {n}')

    def test_instances(self):
        oi = self.oi
        n = 0
        for i in oi.instances(NUCLEOLUS):
            n += 1
            print(f'{i}')
            if n > 3:
                break

    def test_all_models(self):
        oi = self.oi
        for i in oi.all_models():
            print(f'{i}')

    def test_model_search(self):
        oi = self.oi
        for m in oi.search_models('epidermal growth factor receptor signaling pathway'):
            print(yaml_dumper.dumps(m))

    def test_sparqlfun(self):
        se = self.oi.sparqlfun_engine
        uri = self.oi.curie_to_uri(DMEL_EGFR_MODEL)
        resultset = se.query(ModelInfo, id=DMEL_EGFR_MODEL)
        print(yaml_dumper.dumps(resultset))
        assert len(resultset.results) == 1

    def test_search2(self):
        se = self.oi.sparqlfun_engine
        uri = self.oi.curie_to_uri(DMEL_EGFR_MODEL)
        resultset = se.query(ModelQuery, title="signaling")
        print(yaml_dumper.dumps(resultset))
        assert len(resultset.results) > 1
