import unittest
from go_library.amigo_solr.engine import create_handle
from go_library.utils.term_comparison import TermComparisonEngine

NUCLEAR_MEMBRANE = 'GO:0031965'
NUCLEUS = 'GO:0005634'
MEMBRANE = 'GO:0016020'
PROTEIN_COMPLEX = 'GO:0032991'


class TermComparisonTest(unittest.TestCase):

    def setUp(self) -> None:
        api = create_handle()
        self.tc = TermComparisonEngine(amigo=api)

    def test_term_comparison(self):
        results = self.tc.compare(["GO:0060911", "GO:0060912", "GO:0060913"], taxon='NCBITaxon:10090')
        print(results)


if __name__ == '__main__':
    unittest.main()
