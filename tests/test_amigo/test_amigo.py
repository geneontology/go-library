import unittest
from go_library.amigo_solr.engine import create_handle

NUCLEAR_MEMBRANE = 'GO:0031965'
NUCLEUS = 'GO:0005634'
MEMBRANE = 'GO:0016020'
PROTEIN_COMPLEX = 'GO:0032991'


class QueryTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.api = api = create_handle()


    def test_api(self):
        api = self.api
        c = api.fetch_OntologyClass(NUCLEAR_MEMBRANE)
        #print(c)
        self.assertEqual('nuclear membrane', c.annotation_class_label)
        self.assertEqual(NUCLEAR_MEMBRANE, c.annotation_class)
        results = list(api.query_OntologyClass(isa_partof_closure=[NUCLEAR_MEMBRANE, PROTEIN_COMPLEX]))
        for r in results:
            print(f'{r.id} {r.annotation_class_label}')
        assert len(results) > 1


if __name__ == '__main__':
    unittest.main()
