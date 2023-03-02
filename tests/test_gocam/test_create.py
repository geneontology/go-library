# -*- coding: utf-8 -*-
import pkgutil

from go_library.datamodel import MAIN_SCHEMA_PATH
from go_library.datamodel.gocam import *
from linkml_runtime import SchemaView
from linkml_runtime.utils.introspection import package_schemaview
from rdflib import Graph
import json

from hbreader import hbread
from linkml_runtime.loaders import yaml_loader, json_loader, rdf_loader
from linkml_runtime.dumpers import json_dumper, yaml_dumper, rdf_dumper, rdflib_dumper

import os
from tests import JSONLD_DIR, TARGET_DIR

"""Test the module can be imported."""

import unittest

# from https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7012280/figure/F3/

WNT_SIGNALING = 'GO:0060070' ## canonical Wnt signaling pathway
RECEPTOR_LIGAND = 'GO:0048018' ## receptor ligand activity
RECEPTOR_ACTIVITY = 'GO:0042813' ## Wnt-activated receptor activity
EXTRACELLULAR = 'GO:0005615' ## extracellular space
PM = 'GO:0005886' ## plasma membrane
WNT3 = 'UniProtKB:P56703'
FZD1 = 'UniProtKB:Q9UP38'

ttl_out = os.path.join(TARGET_DIR, 'sample.ttl')
jsonld_out = os.path.join(TARGET_DIR, 'sample.jsonld')
json_out = os.path.join(TARGET_DIR, 'sample.json')
ttl_roundtrip_out = os.path.join(TARGET_DIR, 'sample-roundtrip.ttl')
ttl_out = os.path.join(TARGET_DIR, 'sample.ttl')
#cntxt_file =  os.path.join(JSONLD_DIR, 'test_gocam.context.jsonld')

#cntxt = f.read()

def id(s):
    return f'gomodel:a5g4ccd08-{s}'

counter = 0
def gen_evidences(eco: str, ref: str = 'PMID:1234') -> List[Evidence]:
    global  counter
    counter += 1
    return [Evidence(id=id(f'e{counter}'),
                    evidence_type=eco, reference=ref)]


class TestCreate(unittest.TestCase):
    """A test case for create tests."""

    def test_create(self):
        #schema_str = pkgutil.get_data('go_library', '../../src/linkml/gocam.yaml').decode(encoding='utf-8')
        #print(schema_str)
        #package_schemaview()
        sv = SchemaView(str(MAIN_SCHEMA_PATH))
        #print(sv.all_classes())
        #f = open(cntxt_file)
        #cntxt = json.load(f)
        # TODO: centralize this
        #add_prefixes(cntxt, 'UniProtKB', 'http://purl.identifiers.org/uniprot/')
        #add_prefixes(cntxt, 'PMID', 'http://identifiers.org/pmid/')
        #add_prefixes(cntxt, 'orcid', 'http://identifiers.org/orcid/')
        #cntxt = json.dumps(cntxt)
        #print(f'C={cntxt}')
        m = Model(id=id('m1'),
                  title='test model: see https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7012280/figure/F3/',
                  contributor=['orcid:123', 'orcid:234'],
                  state=ModelStateEnum.development)
        print(f'Model = {m.id}')
        p1 = BiologicalProcess(id=id('p1'), type=WNT_SIGNALING)
        c1 = AnatomicalEntity(id=id('c1'), type=EXTRACELLULAR,
                              category=AnatomicalEntityCategory.CellularAnatomicalEntity)
        c2 = AnatomicalEntity(id=id('c2'), type=PM,
                              category=AnatomicalEntityCategory.CellularAnatomicalEntity)
        g1 = InformationBiomacromolecule(id=id('g1'), type=WNT3,
                                         category=InformationBiomacromoleculeCategory.GeneOrReferenceProtein)
        g2 = InformationBiomacromolecule(id=id('g2'), type=FZD1,
                                         category=InformationBiomacromoleculeCategory.GeneOrReferenceProtein)
        a2 = MolecularActivity(id=id('a2'), type=RECEPTOR_ACTIVITY,
                               enabled_by=EnabledByAssociation(has_evidence=gen_evidences('ECO:nnn'),
                                                               object=g2.id),
                               occurs_in=OccursInAssociation(
                                   has_evidence=gen_evidences('ECO:nnn'),
                                   object=c2.id),
                               part_of=ProcessPartOfAssociation(
                                   has_evidence=gen_evidences('ECO:nnn'),
                                   object=p1.id))
        a1_to_a2_assoc = \
            ActivityToActivityCausalAssociation(has_evidence=gen_evidences('ECO:nnn'),
                                                predicate='regulates',
                                                object=id('a2'))
        a1 = MolecularActivity(id=id('a1'), type=RECEPTOR_LIGAND,
                               enabled_by=EnabledByAssociation(
                                   has_evidence=gen_evidences('ECO:nnn'),
                                   object=g1.id),
                               occurs_in=OccursInAssociation(
                                   has_evidence=gen_evidences('ECO:nnn'),
                                   object=c1.id),
                               #has_activity_causal_associations=[a1_to_a2_assoc],
                               part_of=ProcessPartOfAssociation(
                                   has_evidence=gen_evidences('ECO:nnn'),
                                   object=p1.id))
        a1.has_activity_causal_associations = [a1_to_a2_assoc]

        m.molecular_activity_set = [a1, a2]
        m.information_biomacromolecule_set = [g1, g2]
        #json_dumper.dump(element=m, to_file=jsonld_out, contexts=cntxt)
        json_dumper.dump(element=m, to_file=json_out)
        rdflib_dumper.dump(element=m, to_file=ttl_out, schemaview=sv)
        g = Graph()

        g.parse(ttl_out, format="turtle")
        qres = g.query(
            """PREFIX test_gocam: <https://w3id.org/gocam/>
               SELECT DISTINCT ?g
               WHERE {
                   ?ai rdf:type <http://purl.obolibrary.org/obo/GO_0048018> ;
                       test_gocam:enabled_by [rdf:object [ rdf:type ?g ]]
               }""")
        found = False
        for row in qres:
            gene = row[0]
            print(f'row={gene}')
            if str(gene) == 'http://identifiers.org/uniprot/P56703':
                found = True
        assert found
        print(f'Writing to {ttl_roundtrip_out}')
        g.serialize(ttl_roundtrip_out, format='turtle')
        #ttl = g.serialize(ttl_roundtrip_out, format="turtle").decode()
        #print(ttl)
        # TEST THIS AFTER: https://github.com/linkml/linkml/issues/157
        #new_obj = json_loader.load(jsonld_out, Model)
        #print(new_obj)