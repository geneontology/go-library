# Auto generated from gocam.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-04-26T20:35:28
# Schema: gocam
#
# id: https://w3id.org/gocam
# description: GO CAM LinkML schema (experimental) The central class in this datamodel is a [Model](Model.md). A
#              model consists of a set of [MolecularActivity](MolecularActivity.md) objects, from which hangs
#              various elements connected by different kinds of [Association](Association.md) See: *
#              [https://github.com/cmungall/linkml-gocam](https://github.com/cmungall/linkml-gocam) *
#              [https://cmungall.github.io/linkml-gocam/](https://cmungall.github.io/linkml-gocam/)
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BFO = CurieNamespace('BFO', 'http://purl.obolibrary.org/obo/BFO_')
DOI = CurieNamespace('DOI', 'http://dx.doi.org/')
ECO = CurieNamespace('ECO', 'http://purl.obolibrary.org/obo/ECO_')
GO = CurieNamespace('GO', 'http://purl.obolibrary.org/obo/GO_')
OBAN = CurieNamespace('OBAN', 'http://purl.org/oban/')
PMID = CurieNamespace('PMID', 'http://www.ncbi.nlm.nih.gov/pubmed/')
RO = CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
DCE = CurieNamespace('dce', 'http://purl.org/dc/elements/1.1/')
GOCAM = CurieNamespace('gocam', 'https://w3id.org/gocam/')
GOMODEL = CurieNamespace('gomodel', 'http://model.geneontology.org/')
GOSHAPES = CurieNamespace('goshapes', 'http://purl.obolibrary.org/obo/go/shapes/')
LEGO = CurieNamespace('lego', 'http://geneontology.org/lego/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
PAV = CurieNamespace('pav', 'http://purl.org/pav/')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = GOCAM


# Types
class ChemicalFormulaValue(str):
    """ A chemical formula """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "chemical formula value"
    type_model_uri = GOCAM.ChemicalFormulaValue


class CategoryType(Uriorcurie):
    """ A primitive type in which the value denotes a class within the biolink model. The value must be a URI or a CURIE. In a Neo4j representation, the value should be the CURIE for the biolink class, for example biolink:Gene. For an RDF representation, the value should be a URI such as https://w3id.org/biolink/vocab/Gene """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "category type"
    type_model_uri = GOCAM.CategoryType


class IriType(Uriorcurie):
    """ An IRI """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "iri type"
    type_model_uri = GOCAM.IriType


class LabelType(String):
    """ A string that provides a human-readable name for an Entity """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "label type"
    type_model_uri = GOCAM.LabelType


class PredicateType(Uriorcurie):
    """ A RO identifier """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "predicate type"
    type_model_uri = GOCAM.PredicateType


class NarrativeText(String):
    """ A string that provides a human-readable description of something """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "narrative text"
    type_model_uri = GOCAM.NarrativeText


class SymbolType(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "symbol type"
    type_model_uri = GOCAM.SymbolType


# Class references
class EntityId(URIorCURIE):
    pass


class ModelId(EntityId):
    pass


class DomainEntityId(EntityId):
    pass


class MolecularActivityId(DomainEntityId):
    pass


class BiologicalProcessId(DomainEntityId):
    pass


class AnatomicalEntityId(DomainEntityId):
    pass


class ChemicalEntityId(DomainEntityId):
    pass


class InformationBiomacromoleculeId(ChemicalEntityId):
    pass


class OntologyClassId(URIorCURIE):
    pass


class InformationEntityId(EntityId):
    pass


class PublicationId(InformationEntityId):
    pass


class EvidenceId(InformationEntityId):
    pass


class DomainEntityMixinId(URIorCURIE):
    pass


class ActivityOrProcessId(DomainEntityMixinId):
    pass


class ProcessOrPhaseId(DomainEntityMixinId):
    pass


class ContinuantId(DomainEntityMixinId):
    pass


@dataclass
class Entity(YAMLRoot):
    """
    Abstract base class for any biological Entity or ActivityOrProcess in a GO-CAM model
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.Entity
    class_class_curie: ClassVar[str] = "gocam:Entity"
    class_name: ClassVar[str] = "Entity"
    class_model_uri: ClassVar[URIRef] = GOCAM.Entity

    id: Union[str, EntityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EntityId):
            self.id = EntityId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Model(Entity):
    """
    A collection of GO-CAM entities and associated metadata. A model combines multiple simple GO annotations into an
    integrated, semantically precise and computable model of biological function.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.Model
    class_class_curie: ClassVar[str] = "gocam:Model"
    class_name: ClassVar[str] = "model"
    class_model_uri: ClassVar[URIRef] = GOCAM.Model

    id: Union[str, ModelId] = None
    title: Optional[str] = None
    contributor: Optional[Union[str, List[str]]] = empty_list()
    date: Optional[str] = None
    state: Optional[str] = None
    version: Optional[Union[str, URIorCURIE]] = None
    comment: Optional[Union[str, List[str]]] = empty_list()
    graph_type: Optional[Union[str, URIorCURIE]] = None
    in_taxon: Optional[Union[str, URIorCURIE]] = None
    provided_by: Optional[str] = None
    molecular_activity_set: Optional[Union[Dict[Union[str, MolecularActivityId], Union[dict, "MolecularActivity"]], List[Union[dict, "MolecularActivity"]]]] = empty_dict()
    biological_process_set: Optional[Union[Dict[Union[str, BiologicalProcessId], Union[dict, "BiologicalProcess"]], List[Union[dict, "BiologicalProcess"]]]] = empty_dict()
    information_biomacromolecule_set: Optional[Union[Dict[Union[str, InformationBiomacromoleculeId], Union[dict, "InformationBiomacromolecule"]], List[Union[dict, "InformationBiomacromolecule"]]]] = empty_dict()
    chemical_entity_set: Optional[Union[Dict[Union[str, ChemicalEntityId], Union[dict, "ChemicalEntity"]], List[Union[dict, "ChemicalEntity"]]]] = empty_dict()
    ontology_class_set: Optional[Union[Dict[Union[str, OntologyClassId], Union[dict, "OntologyClass"]], List[Union[dict, "OntologyClass"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ModelId):
            self.id = ModelId(self.id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.contributor, list):
            self.contributor = [self.contributor] if self.contributor is not None else []
        self.contributor = [v if isinstance(v, str) else str(v) for v in self.contributor]

        if self.date is not None and not isinstance(self.date, str):
            self.date = str(self.date)

        if self.state is not None and not isinstance(self.state, str):
            self.state = str(self.state)

        if self.version is not None and not isinstance(self.version, URIorCURIE):
            self.version = URIorCURIE(self.version)

        if not isinstance(self.comment, list):
            self.comment = [self.comment] if self.comment is not None else []
        self.comment = [v if isinstance(v, str) else str(v) for v in self.comment]

        if self.graph_type is not None and not isinstance(self.graph_type, URIorCURIE):
            self.graph_type = URIorCURIE(self.graph_type)

        if self.in_taxon is not None and not isinstance(self.in_taxon, URIorCURIE):
            self.in_taxon = URIorCURIE(self.in_taxon)

        if self.provided_by is not None and not isinstance(self.provided_by, str):
            self.provided_by = str(self.provided_by)

        self._normalize_inlined_as_dict(slot_name="molecular_activity_set", slot_type=MolecularActivity, key_name="id", keyed=True)

        self._normalize_inlined_as_dict(slot_name="biological_process_set", slot_type=BiologicalProcess, key_name="id", keyed=True)

        self._normalize_inlined_as_dict(slot_name="information_biomacromolecule_set", slot_type=InformationBiomacromolecule, key_name="id", keyed=True)

        self._normalize_inlined_as_dict(slot_name="chemical_entity_set", slot_type=ChemicalEntity, key_name="id", keyed=True)

        self._normalize_inlined_as_dict(slot_name="ontology_class_set", slot_type=OntologyClass, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class DomainEntity(Entity):
    """
    Abstract Entity for representing any part_of a GO-CAM model
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.DomainEntity
    class_class_curie: ClassVar[str] = "gocam:DomainEntity"
    class_name: ClassVar[str] = "DomainEntity"
    class_model_uri: ClassVar[URIRef] = GOCAM.DomainEntity

    id: Union[str, DomainEntityId] = None
    type: Union[str, OntologyClassId] = None
    type_inferences: Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DomainEntityId):
            self.id = DomainEntityId(self.id)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, OntologyClassId):
            self.type = OntologyClassId(self.type)

        if not isinstance(self.type_inferences, list):
            self.type_inferences = [self.type_inferences] if self.type_inferences is not None else []
        self.type_inferences = [v if isinstance(v, OntologyClassId) else OntologyClassId(v) for v in self.type_inferences]

        super().__post_init__(**kwargs)


@dataclass
class MolecularActivity(DomainEntity):
    """
    An instance of a GO molecular function
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.MolecularActivity
    class_class_curie: ClassVar[str] = "gocam:MolecularActivity"
    class_name: ClassVar[str] = "MolecularActivity"
    class_model_uri: ClassVar[URIRef] = GOCAM.MolecularActivity

    id: Union[str, MolecularActivityId] = None
    type: Union[str, OntologyClassId] = None
    has_activity_causal_associations: Optional[Union[Union[dict, "ActivityToActivityCausalAssociation"], List[Union[dict, "ActivityToActivityCausalAssociation"]]]] = empty_list()
    has_process_causal_associations: Optional[Union[Union[dict, "ActivityToProcessCausalAssociation"], List[Union[dict, "ActivityToProcessCausalAssociation"]]]] = empty_list()
    happens_during: Optional[Union[Union[dict, "HappensDuringAssociation"], List[Union[dict, "HappensDuringAssociation"]]]] = empty_list()
    part_of: Optional[Union[Union[dict, "ProcessPartOfAssociation"], List[Union[dict, "ProcessPartOfAssociation"]]]] = empty_list()
    enabled_by: Optional[Union[Union[dict, "EnabledByAssociation"], List[Union[dict, "EnabledByAssociation"]]]] = empty_list()
    has_input: Optional[Union[Union[dict, "HasInputAssociation"], List[Union[dict, "HasInputAssociation"]]]] = empty_list()
    occurs_in: Optional[Union[Union[dict, "OccursInAssociation"], List[Union[dict, "OccursInAssociation"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MolecularActivityId):
            self.id = MolecularActivityId(self.id)

        if not isinstance(self.has_activity_causal_associations, list):
            self.has_activity_causal_associations = [self.has_activity_causal_associations] if self.has_activity_causal_associations is not None else []
        self.has_activity_causal_associations = [v if isinstance(v, ActivityToActivityCausalAssociation) else ActivityToActivityCausalAssociation(**as_dict(v)) for v in self.has_activity_causal_associations]

        if not isinstance(self.has_process_causal_associations, list):
            self.has_process_causal_associations = [self.has_process_causal_associations] if self.has_process_causal_associations is not None else []
        self.has_process_causal_associations = [v if isinstance(v, ActivityToProcessCausalAssociation) else ActivityToProcessCausalAssociation(**as_dict(v)) for v in self.has_process_causal_associations]

        if not isinstance(self.happens_during, list):
            self.happens_during = [self.happens_during] if self.happens_during is not None else []
        self.happens_during = [v if isinstance(v, HappensDuringAssociation) else HappensDuringAssociation(**as_dict(v)) for v in self.happens_during]

        if not isinstance(self.part_of, list):
            self.part_of = [self.part_of] if self.part_of is not None else []
        self.part_of = [v if isinstance(v, ProcessPartOfAssociation) else ProcessPartOfAssociation(**as_dict(v)) for v in self.part_of]

        if not isinstance(self.enabled_by, list):
            self.enabled_by = [self.enabled_by] if self.enabled_by is not None else []
        self.enabled_by = [v if isinstance(v, EnabledByAssociation) else EnabledByAssociation(**as_dict(v)) for v in self.enabled_by]

        if not isinstance(self.has_input, list):
            self.has_input = [self.has_input] if self.has_input is not None else []
        self.has_input = [v if isinstance(v, HasInputAssociation) else HasInputAssociation(**as_dict(v)) for v in self.has_input]

        if not isinstance(self.occurs_in, list):
            self.occurs_in = [self.occurs_in] if self.occurs_in is not None else []
        self.occurs_in = [v if isinstance(v, OccursInAssociation) else OccursInAssociation(**as_dict(v)) for v in self.occurs_in]

        super().__post_init__(**kwargs)


@dataclass
class BiologicalProcess(DomainEntity):
    """
    An instance of a GO BiologicalProcess
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.BiologicalProcess
    class_class_curie: ClassVar[str] = "gocam:BiologicalProcess"
    class_name: ClassVar[str] = "BiologicalProcess"
    class_model_uri: ClassVar[URIRef] = GOCAM.BiologicalProcess

    id: Union[str, BiologicalProcessId] = None
    type: Union[str, OntologyClassId] = None
    occurs_in: Optional[Union[Union[dict, "OccursInAssociation"], List[Union[dict, "OccursInAssociation"]]]] = empty_list()
    has_activity_causal_associations: Optional[Union[Union[dict, "ProcessToActivityCausalAssociation"], List[Union[dict, "ProcessToActivityCausalAssociation"]]]] = empty_list()
    has_process_causal_associations: Optional[Union[Union[dict, "ProcessToProcessCausalAssociation"], List[Union[dict, "ProcessToProcessCausalAssociation"]]]] = empty_list()
    happens_during: Optional[Union[Union[dict, "HappensDuringAssociation"], List[Union[dict, "HappensDuringAssociation"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BiologicalProcessId):
            self.id = BiologicalProcessId(self.id)

        if not isinstance(self.occurs_in, list):
            self.occurs_in = [self.occurs_in] if self.occurs_in is not None else []
        self.occurs_in = [v if isinstance(v, OccursInAssociation) else OccursInAssociation(**as_dict(v)) for v in self.occurs_in]

        if not isinstance(self.has_activity_causal_associations, list):
            self.has_activity_causal_associations = [self.has_activity_causal_associations] if self.has_activity_causal_associations is not None else []
        self.has_activity_causal_associations = [v if isinstance(v, ProcessToActivityCausalAssociation) else ProcessToActivityCausalAssociation(**as_dict(v)) for v in self.has_activity_causal_associations]

        if not isinstance(self.has_process_causal_associations, list):
            self.has_process_causal_associations = [self.has_process_causal_associations] if self.has_process_causal_associations is not None else []
        self.has_process_causal_associations = [v if isinstance(v, ProcessToProcessCausalAssociation) else ProcessToProcessCausalAssociation(**as_dict(v)) for v in self.has_process_causal_associations]

        if not isinstance(self.happens_during, list):
            self.happens_during = [self.happens_during] if self.happens_during is not None else []
        self.happens_during = [v if isinstance(v, HappensDuringAssociation) else HappensDuringAssociation(**as_dict(v)) for v in self.happens_during]

        super().__post_init__(**kwargs)


@dataclass
class AnatomicalEntity(DomainEntity):
    """
    An instance of a GO cellular AnatomicalEntity, a cell type, or gross anatomical structure
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.AnatomicalEntity
    class_class_curie: ClassVar[str] = "gocam:AnatomicalEntity"
    class_name: ClassVar[str] = "AnatomicalEntity"
    class_model_uri: ClassVar[URIRef] = GOCAM.AnatomicalEntity

    id: Union[str, AnatomicalEntityId] = None
    type: Union[str, OntologyClassId] = None
    category: Union[str, "AnatomicalEntityCategory"] = None
    part_of: Optional[Union[Union[dict, "AnatomicalPartOfAssociation"], List[Union[dict, "AnatomicalPartOfAssociation"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnatomicalEntityId):
            self.id = AnatomicalEntityId(self.id)

        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, AnatomicalEntityCategory):
            self.category = AnatomicalEntityCategory(self.category)

        if not isinstance(self.part_of, list):
            self.part_of = [self.part_of] if self.part_of is not None else []
        self.part_of = [v if isinstance(v, AnatomicalPartOfAssociation) else AnatomicalPartOfAssociation(**as_dict(v)) for v in self.part_of]

        super().__post_init__(**kwargs)


@dataclass
class ChemicalEntity(DomainEntity):
    """
    An instance of a ChemicalEntity, as defined in CHEBI, including macromolecules defined in NEO
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.ChemicalEntity
    class_class_curie: ClassVar[str] = "gocam:ChemicalEntity"
    class_name: ClassVar[str] = "ChemicalEntity"
    class_model_uri: ClassVar[URIRef] = GOCAM.ChemicalEntity

    id: Union[str, ChemicalEntityId] = None
    type: Union[str, OntologyClassId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChemicalEntityId):
            self.id = ChemicalEntityId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class InformationBiomacromolecule(ChemicalEntity):
    """
    This class groups gene, gene product (protein on ncRNA), or a macromolecular complex that is capable of carrying
    out a MolecularActivity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.InformationBiomacromolecule
    class_class_curie: ClassVar[str] = "gocam:InformationBiomacromolecule"
    class_name: ClassVar[str] = "InformationBiomacromolecule"
    class_model_uri: ClassVar[URIRef] = GOCAM.InformationBiomacromolecule

    id: Union[str, InformationBiomacromoleculeId] = None
    type: Union[str, OntologyClassId] = None
    category: Union[str, "InformationBiomacromoleculeCategory"] = None
    has_part: Optional[Union[Union[dict, "MacromoleculeHasPartAssociation"], List[Union[dict, "MacromoleculeHasPartAssociation"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InformationBiomacromoleculeId):
            self.id = InformationBiomacromoleculeId(self.id)

        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, InformationBiomacromoleculeCategory):
            self.category = InformationBiomacromoleculeCategory(self.category)

        if not isinstance(self.has_part, list):
            self.has_part = [self.has_part] if self.has_part is not None else []
        self.has_part = [v if isinstance(v, MacromoleculeHasPartAssociation) else MacromoleculeHasPartAssociation(**as_dict(v)) for v in self.has_part]

        super().__post_init__(**kwargs)


@dataclass
class Association(YAMLRoot):
    """
    An association between a DomainEntity (e.g. a MolecularActivity) and another DomainEntity (e.g. another
    MolecularActivity) with evidence and provenance attached
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RDF.Statement
    class_class_curie: ClassVar[str] = "rdf:Statement"
    class_name: ClassVar[str] = "Association"
    class_model_uri: ClassVar[URIRef] = GOCAM.Association

    object: Union[str, EntityId] = None
    has_evidence: Optional[Union[Dict[Union[str, EvidenceId], Union[dict, "Evidence"]], List[Union[dict, "Evidence"]]]] = empty_dict()
    subject: Optional[Union[str, DomainEntityId]] = None
    predicate: Optional[Union[str, PredicateType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, EntityId):
            self.object = EntityId(self.object)

        self._normalize_inlined_as_list(slot_name="has_evidence", slot_type=Evidence, key_name="id", keyed=True)

        if self.subject is not None and not isinstance(self.subject, DomainEntityId):
            self.subject = DomainEntityId(self.subject)

        if self.predicate is not None and not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        super().__post_init__(**kwargs)


@dataclass
class OccursInAssociation(Association):
    """
    An association owned by a MA or BP that connect to an AE object in which the activity/process is carried out
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.OccursInAssociation
    class_class_curie: ClassVar[str] = "gocam:OccursInAssociation"
    class_name: ClassVar[str] = "OccursInAssociation"
    class_model_uri: ClassVar[URIRef] = GOCAM.OccursInAssociation

    object: Union[str, AnatomicalEntityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, AnatomicalEntityId):
            self.object = AnatomicalEntityId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class CausalAssociation(Association):
    """
    An association owned by an upstream MA or BP that connects to a downstream MA or BP. The nature of the causal
    relationship is indicated with the predicate.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.CausalAssociation
    class_class_curie: ClassVar[str] = "gocam:CausalAssociation"
    class_name: ClassVar[str] = "CausalAssociation"
    class_model_uri: ClassVar[URIRef] = GOCAM.CausalAssociation

    object: Union[str, ActivityOrProcessId] = None
    subject: Optional[Union[str, DomainEntityId]] = None
    predicate: Optional[Union[str, PredicateType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ActivityOrProcessId):
            self.object = ActivityOrProcessId(self.object)

        if self.subject is not None and not isinstance(self.subject, DomainEntityId):
            self.subject = DomainEntityId(self.subject)

        if self.predicate is not None and not isinstance(self.predicate, PredicateType):
            self.predicate = PredicateType(self.predicate)

        super().__post_init__(**kwargs)


@dataclass
class CausalAssociationToActivity(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.CausalAssociationToActivity
    class_class_curie: ClassVar[str] = "gocam:CausalAssociationToActivity"
    class_name: ClassVar[str] = "CausalAssociationToActivity"
    class_model_uri: ClassVar[URIRef] = GOCAM.CausalAssociationToActivity

    object: Union[str, MolecularActivityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, MolecularActivityId):
            self.object = MolecularActivityId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class CausalAssociationToProcess(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.CausalAssociationToProcess
    class_class_curie: ClassVar[str] = "gocam:CausalAssociationToProcess"
    class_name: ClassVar[str] = "CausalAssociationToProcess"
    class_model_uri: ClassVar[URIRef] = GOCAM.CausalAssociationToProcess

    object: Union[str, BiologicalProcessId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, BiologicalProcessId):
            self.object = BiologicalProcessId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ActivityToActivityCausalAssociation(CausalAssociation):
    """
    A CausalAssociation between two molecular activities
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.ActivityToActivityCausalAssociation
    class_class_curie: ClassVar[str] = "gocam:ActivityToActivityCausalAssociation"
    class_name: ClassVar[str] = "ActivityToActivityCausalAssociation"
    class_model_uri: ClassVar[URIRef] = GOCAM.ActivityToActivityCausalAssociation

    object: Union[str, MolecularActivityId] = None
    subject: Optional[Union[str, MolecularActivityId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, MolecularActivityId):
            self.object = MolecularActivityId(self.object)

        if self.subject is not None and not isinstance(self.subject, MolecularActivityId):
            self.subject = MolecularActivityId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class ProcessToProcessCausalAssociation(CausalAssociation):
    """
    A CausalAssociation between two BiologicalProcesses
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.ProcessToProcessCausalAssociation
    class_class_curie: ClassVar[str] = "gocam:ProcessToProcessCausalAssociation"
    class_name: ClassVar[str] = "ProcessToProcessCausalAssociation"
    class_model_uri: ClassVar[URIRef] = GOCAM.ProcessToProcessCausalAssociation

    object: Union[str, BiologicalProcessId] = None
    subject: Optional[Union[str, BiologicalProcessId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, BiologicalProcessId):
            self.object = BiologicalProcessId(self.object)

        if self.subject is not None and not isinstance(self.subject, BiologicalProcessId):
            self.subject = BiologicalProcessId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class ProcessToActivityCausalAssociation(CausalAssociation):
    """
    A CausalAssociation between a BiologicalProcess and a MolecularActivity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.ProcessToActivityCausalAssociation
    class_class_curie: ClassVar[str] = "gocam:ProcessToActivityCausalAssociation"
    class_name: ClassVar[str] = "ProcessToActivityCausalAssociation"
    class_model_uri: ClassVar[URIRef] = GOCAM.ProcessToActivityCausalAssociation

    object: Union[str, MolecularActivityId] = None
    subject: Optional[Union[str, BiologicalProcessId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, MolecularActivityId):
            self.object = MolecularActivityId(self.object)

        if self.subject is not None and not isinstance(self.subject, BiologicalProcessId):
            self.subject = BiologicalProcessId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class ActivityToProcessCausalAssociation(CausalAssociation):
    """
    A CausalAssociation between a MolecularActivity and a BiologicalProcess
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.ActivityToProcessCausalAssociation
    class_class_curie: ClassVar[str] = "gocam:ActivityToProcessCausalAssociation"
    class_name: ClassVar[str] = "ActivityToProcessCausalAssociation"
    class_model_uri: ClassVar[URIRef] = GOCAM.ActivityToProcessCausalAssociation

    object: Union[str, BiologicalProcessId] = None
    subject: Optional[Union[str, MolecularActivityId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, BiologicalProcessId):
            self.object = BiologicalProcessId(self.object)

        if self.subject is not None and not isinstance(self.subject, MolecularActivityId):
            self.subject = MolecularActivityId(self.subject)

        super().__post_init__(**kwargs)


@dataclass
class HasPartAssociation(Association):
    """
    General grouping for associations that Link an Entity to its parts by a HasPartAssociation
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.HasPartAssociation
    class_class_curie: ClassVar[str] = "gocam:HasPartAssociation"
    class_name: ClassVar[str] = "HasPartAssociation"
    class_model_uri: ClassVar[URIRef] = GOCAM.HasPartAssociation

    object: Union[str, EntityId] = None

@dataclass
class MacromoleculeHasPartAssociation(HasPartAssociation):
    """
    Connects a macromolecule (such as a protein complex) to its parts (gene products or chemical entities)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.MacromoleculeHasPartAssociation
    class_class_curie: ClassVar[str] = "gocam:MacromoleculeHasPartAssociation"
    class_name: ClassVar[str] = "MacromoleculeHasPartAssociation"
    class_model_uri: ClassVar[URIRef] = GOCAM.MacromoleculeHasPartAssociation

    object: Union[str, ContinuantId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ContinuantId):
            self.object = ContinuantId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class PartOfAssociation(Association):
    """
    General grouping for associations that Link an Entity to its wholes by a PartOfAssociation
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.PartOfAssociation
    class_class_curie: ClassVar[str] = "gocam:PartOfAssociation"
    class_name: ClassVar[str] = "PartOfAssociation"
    class_model_uri: ClassVar[URIRef] = GOCAM.PartOfAssociation

    object: Union[str, EntityId] = None

@dataclass
class AnatomicalPartOfAssociation(PartOfAssociation):
    """
    Connects an AnatomicalEntity (such as a component, cell, or gross AnatomicalEntity) to its parent parts
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.AnatomicalPartOfAssociation
    class_class_curie: ClassVar[str] = "gocam:AnatomicalPartOfAssociation"
    class_name: ClassVar[str] = "AnatomicalPartOfAssociation"
    class_model_uri: ClassVar[URIRef] = GOCAM.AnatomicalPartOfAssociation

    object: Union[str, AnatomicalEntityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, AnatomicalEntityId):
            self.object = AnatomicalEntityId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class ProcessPartOfAssociation(PartOfAssociation):
    """
    Connects a MA or BP to its parent parts
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.ProcessPartOfAssociation
    class_class_curie: ClassVar[str] = "gocam:ProcessPartOfAssociation"
    class_name: ClassVar[str] = "ProcessPartOfAssociation"
    class_model_uri: ClassVar[URIRef] = GOCAM.ProcessPartOfAssociation

    object: Union[str, BiologicalProcessId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, BiologicalProcessId):
            self.object = BiologicalProcessId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class EnabledByAssociation(Association):
    """
    Connects an MA to the InformationBiomacromolecule that executes the activity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.EnabledByAssociation
    class_class_curie: ClassVar[str] = "gocam:EnabledByAssociation"
    class_name: ClassVar[str] = "EnabledByAssociation"
    class_model_uri: ClassVar[URIRef] = GOCAM.EnabledByAssociation

    object: Union[str, InformationBiomacromoleculeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, InformationBiomacromoleculeId):
            self.object = InformationBiomacromoleculeId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class HappensDuringAssociation(Association):
    """
    Connects an MF to a ProcessOrPhase in which the process occurs
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.HappensDuringAssociation
    class_class_curie: ClassVar[str] = "gocam:HappensDuringAssociation"
    class_name: ClassVar[str] = "HappensDuringAssociation"
    class_model_uri: ClassVar[URIRef] = GOCAM.HappensDuringAssociation

    object: Union[str, ActivityOrProcessId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ActivityOrProcessId):
            self.object = ActivityOrProcessId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class HasInputAssociation(Association):
    """
    Connects an MF or BP to its input Entity, which may be a ChemicalEntity, an InformationBiomacromolecule, or a
    larger structure
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.HasInputAssociation
    class_class_curie: ClassVar[str] = "gocam:HasInputAssociation"
    class_name: ClassVar[str] = "HasInputAssociation"
    class_model_uri: ClassVar[URIRef] = GOCAM.HasInputAssociation

    object: Union[str, ContinuantId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.object):
            self.MissingRequiredField("object")
        if not isinstance(self.object, ContinuantId):
            self.object = ContinuantId(self.object)

        super().__post_init__(**kwargs)


@dataclass
class OntologyClass(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.OntologyClass
    class_class_curie: ClassVar[str] = "gocam:OntologyClass"
    class_name: ClassVar[str] = "OntologyClass"
    class_model_uri: ClassVar[URIRef] = GOCAM.OntologyClass

    id: Union[str, OntologyClassId] = None
    category: Union[str, CategoryType] = None
    name: Optional[Union[str, LabelType]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OntologyClassId):
            self.id = OntologyClassId(self.id)

        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, CategoryType):
            self.category = CategoryType(self.category)

        if self.name is not None and not isinstance(self.name, LabelType):
            self.name = LabelType(self.name)

        super().__post_init__(**kwargs)


@dataclass
class InformationEntity(Entity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.InformationEntity
    class_class_curie: ClassVar[str] = "gocam:InformationEntity"
    class_name: ClassVar[str] = "InformationEntity"
    class_model_uri: ClassVar[URIRef] = GOCAM.InformationEntity

    id: Union[str, InformationEntityId] = None

@dataclass
class Publication(InformationEntity):
    """
    A published Entity such as a paper in pubmed
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.Publication
    class_class_curie: ClassVar[str] = "gocam:Publication"
    class_name: ClassVar[str] = "Publication"
    class_model_uri: ClassVar[URIRef] = GOCAM.Publication

    id: Union[str, PublicationId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PublicationId):
            self.id = PublicationId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Evidence(InformationEntity):
    """
    An instance of a piece of Evidence. Evidence attributes such as type, reference, hang off of here
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.Evidence
    class_class_curie: ClassVar[str] = "gocam:Evidence"
    class_name: ClassVar[str] = "Evidence"
    class_model_uri: ClassVar[URIRef] = GOCAM.Evidence

    id: Union[str, EvidenceId] = None
    evidence_type: Union[str, OntologyClassId] = None
    contributor: Optional[Union[str, List[str]]] = empty_list()
    date: Optional[str] = None
    reference: Optional[Union[Union[str, PublicationId], List[Union[str, PublicationId]]]] = empty_list()
    with_object: Optional[Union[Union[str, EntityId], List[Union[str, EntityId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EvidenceId):
            self.id = EvidenceId(self.id)

        if self._is_empty(self.evidence_type):
            self.MissingRequiredField("evidence_type")
        if not isinstance(self.evidence_type, OntologyClassId):
            self.evidence_type = OntologyClassId(self.evidence_type)

        if not isinstance(self.contributor, list):
            self.contributor = [self.contributor] if self.contributor is not None else []
        self.contributor = [v if isinstance(v, str) else str(v) for v in self.contributor]

        if self.date is not None and not isinstance(self.date, str):
            self.date = str(self.date)

        if not isinstance(self.reference, list):
            self.reference = [self.reference] if self.reference is not None else []
        self.reference = [v if isinstance(v, PublicationId) else PublicationId(v) for v in self.reference]

        if not isinstance(self.with_object, list):
            self.with_object = [self.with_object] if self.with_object is not None else []
        self.with_object = [v if isinstance(v, EntityId) else EntityId(v) for v in self.with_object]

        super().__post_init__(**kwargs)


@dataclass
class DomainEntityMixin(YAMLRoot):
    """
    Grouping for mixins that apply to GO-CAM entities. These mixins allow us to group together entities that are alike
    in some fashion
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.DomainEntityMixin
    class_class_curie: ClassVar[str] = "gocam:DomainEntityMixin"
    class_name: ClassVar[str] = "DomainEntityMixin"
    class_model_uri: ClassVar[URIRef] = GOCAM.DomainEntityMixin

    id: Union[str, DomainEntityMixinId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DomainEntityMixinId):
            self.id = DomainEntityMixinId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ActivityOrProcess(DomainEntityMixin):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.ActivityOrProcess
    class_class_curie: ClassVar[str] = "gocam:ActivityOrProcess"
    class_name: ClassVar[str] = "ActivityOrProcess"
    class_model_uri: ClassVar[URIRef] = GOCAM.ActivityOrProcess

    id: Union[str, ActivityOrProcessId] = None

@dataclass
class ProcessOrPhase(DomainEntityMixin):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.ProcessOrPhase
    class_class_curie: ClassVar[str] = "gocam:ProcessOrPhase"
    class_name: ClassVar[str] = "ProcessOrPhase"
    class_model_uri: ClassVar[URIRef] = GOCAM.ProcessOrPhase

    id: Union[str, ProcessOrPhaseId] = None

@dataclass
class Continuant(DomainEntityMixin):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.Continuant
    class_class_curie: ClassVar[str] = "gocam:Continuant"
    class_name: ClassVar[str] = "Continuant"
    class_model_uri: ClassVar[URIRef] = GOCAM.Continuant

    id: Union[str, ContinuantId] = None

# Enumerations
class ModelStateEnum(EnumDefinitionImpl):
    """
    Status of a model
    """
    production = PermissibleValue(text="production")
    development = PermissibleValue(text="development")

    _defn = EnumDefinition(
        name="ModelStateEnum",
        description="Status of a model",
    )

class AnatomicalEntityCategory(EnumDefinitionImpl):

    CellularAnatomicalEntity = PermissibleValue(text="CellularAnatomicalEntity")
    Cell = PermissibleValue(text="Cell")
    GrossAnatomicalStructure = PermissibleValue(text="GrossAnatomicalStructure")
    Organism = PermissibleValue(text="Organism")

    _defn = EnumDefinition(
        name="AnatomicalEntityCategory",
    )

class InformationBiomacromoleculeCategory(EnumDefinitionImpl):

    GeneOrReferenceProtein = PermissibleValue(text="GeneOrReferenceProtein",
                                                                   meaning=GOCAM["biolink.GeneOrGeneProduct"])
    ProteinIsoform = PermissibleValue(text="ProteinIsoform")
    MacromolecularComplex = PermissibleValue(text="MacromolecularComplex")
    Unknown = PermissibleValue(text="Unknown")

    _defn = EnumDefinition(
        name="InformationBiomacromoleculeCategory",
    )

class CausalPredicateEnum(EnumDefinitionImpl):

    regulates = PermissibleValue(text="regulates",
                                         meaning=RO["0002211"])

    _defn = EnumDefinition(
        name="CausalPredicateEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "causally upstream of, positive effect",
                PermissibleValue(text="causally upstream of, positive effect",
                                 meaning=RO["0002304"]) )
        setattr(cls, "causally upstream of, negative effect",
                PermissibleValue(text="causally upstream of, negative effect",
                                 meaning=RO["0002305"]) )
        setattr(cls, "causally upstream of",
                PermissibleValue(text="causally upstream of",
                                 meaning=RO["0002411"]) )
        setattr(cls, "immediately causally upstream of",
                PermissibleValue(text="immediately causally upstream of",
                                 meaning=RO["0002412"]) )
        setattr(cls, "causally upstream of or within",
                PermissibleValue(text="causally upstream of or within",
                                 meaning=RO["0002418"]) )
        setattr(cls, "causally upstream of or within, negative effect",
                PermissibleValue(text="causally upstream of or within, negative effect",
                                 meaning=RO["0004046"]) )
        setattr(cls, "causally upstream of or within, positive effect",
                PermissibleValue(text="causally upstream of or within, positive effect",
                                 meaning=RO["0004047"]) )
        setattr(cls, "negatively regulates",
                PermissibleValue(text="negatively regulates",
                                 meaning=RO["0002212"]) )
        setattr(cls, "positively regulates",
                PermissibleValue(text="positively regulates",
                                 meaning=RO["0002213"]) )

# Slots
class slots:
    pass

slots.id = Slot(uri=GOCAM.id, name="id", curie=GOCAM.curie('id'),
                   model_uri=GOCAM.id, domain=None, range=URIRef)

slots.name = Slot(uri=RDFS.label, name="name", curie=RDFS.curie('label'),
                   model_uri=GOCAM.name, domain=None, range=Optional[Union[str, LabelType]])

slots.type = Slot(uri=RDF.type, name="type", curie=RDF.curie('type'),
                   model_uri=GOCAM.type, domain=None, range=Union[str, OntologyClassId])

slots.category = Slot(uri=GOCAM.category, name="category", curie=GOCAM.curie('category'),
                   model_uri=GOCAM.category, domain=None, range=Union[str, CategoryType])

slots.with_object = Slot(uri=LEGO.evidence, name="with_object", curie=LEGO.curie('evidence'),
                   model_uri=GOCAM.with_object, domain=None, range=Optional[Union[Union[str, EntityId], List[Union[str, EntityId]]]])

slots.reference = Slot(uri=DCE.source, name="reference", curie=DCE.curie('source'),
                   model_uri=GOCAM.reference, domain=None, range=Optional[Union[Union[str, PublicationId], List[Union[str, PublicationId]]]])

slots.provided_by = Slot(uri=PAV.providedBy, name="provided_by", curie=PAV.curie('providedBy'),
                   model_uri=GOCAM.provided_by, domain=None, range=Optional[str])

slots.contributor = Slot(uri=DCE.contributor, name="contributor", curie=DCE.curie('contributor'),
                   model_uri=GOCAM.contributor, domain=None, range=Optional[Union[str, List[str]]])

slots.date = Slot(uri=DCE.date, name="date", curie=DCE.curie('date'),
                   model_uri=GOCAM.date, domain=None, range=Optional[str])

slots.evidence_type = Slot(uri=GOCAM.evidence_type, name="evidence_type", curie=GOCAM.curie('evidence_type'),
                   model_uri=GOCAM.evidence_type, domain=None, range=Union[str, OntologyClassId],
                   pattern=re.compile(r'^ECO:\d+$'))

slots.type_inferences = Slot(uri=GOCAM.type_inferences, name="type_inferences", curie=GOCAM.curie('type_inferences'),
                   model_uri=GOCAM.type_inferences, domain=None, range=Optional[Union[Union[str, OntologyClassId], List[Union[str, OntologyClassId]]]])

slots.related_to = Slot(uri=GOCAM.related_to, name="related_to", curie=GOCAM.curie('related_to'),
                   model_uri=GOCAM.related_to, domain=None, range=Optional[Union[Union[dict, Association], List[Union[dict, Association]]]])

slots.occurs_in = Slot(uri=GOCAM.occurs_in, name="occurs_in", curie=GOCAM.curie('occurs_in'),
                   model_uri=GOCAM.occurs_in, domain=None, range=Optional[Union[Union[dict, OccursInAssociation], List[Union[dict, OccursInAssociation]]]])

slots.has_causal_associations = Slot(uri=GOCAM.has_causal_associations, name="has_causal_associations", curie=GOCAM.curie('has_causal_associations'),
                   model_uri=GOCAM.has_causal_associations, domain=None, range=Optional[Union[Union[dict, CausalAssociation], List[Union[dict, CausalAssociation]]]])

slots.has_activity_causal_associations = Slot(uri=GOCAM.has_activity_causal_associations, name="has_activity_causal_associations", curie=GOCAM.curie('has_activity_causal_associations'),
                   model_uri=GOCAM.has_activity_causal_associations, domain=None, range=Optional[Union[Union[dict, CausalAssociationToActivity], List[Union[dict, CausalAssociationToActivity]]]])

slots.has_process_causal_associations = Slot(uri=GOCAM.has_process_causal_associations, name="has_process_causal_associations", curie=GOCAM.curie('has_process_causal_associations'),
                   model_uri=GOCAM.has_process_causal_associations, domain=None, range=Optional[Union[Union[dict, CausalAssociationToProcess], List[Union[dict, CausalAssociationToProcess]]]])

slots.happens_during = Slot(uri=GOCAM.happens_during, name="happens_during", curie=GOCAM.curie('happens_during'),
                   model_uri=GOCAM.happens_during, domain=None, range=Optional[Union[Union[dict, HappensDuringAssociation], List[Union[dict, HappensDuringAssociation]]]])

slots.part_of = Slot(uri=GOCAM.part_of, name="part_of", curie=GOCAM.curie('part_of'),
                   model_uri=GOCAM.part_of, domain=None, range=Optional[Union[Union[dict, PartOfAssociation], List[Union[dict, PartOfAssociation]]]])

slots.has_part = Slot(uri=GOCAM.has_part, name="has_part", curie=GOCAM.curie('has_part'),
                   model_uri=GOCAM.has_part, domain=None, range=Optional[Union[Union[dict, HasPartAssociation], List[Union[dict, HasPartAssociation]]]])

slots.enabled_by = Slot(uri=GOCAM.enabled_by, name="enabled by", curie=GOCAM.curie('enabled_by'),
                   model_uri=GOCAM.enabled_by, domain=MolecularActivity, range=Optional[Union[Union[dict, "EnabledByAssociation"], List[Union[dict, "EnabledByAssociation"]]]])

slots.has_input = Slot(uri=GOCAM.has_input, name="has_input", curie=GOCAM.curie('has_input'),
                   model_uri=GOCAM.has_input, domain=None, range=Optional[Union[Union[dict, HasInputAssociation], List[Union[dict, HasInputAssociation]]]])

slots.has_evidence = Slot(uri=GOCAM.has_evidence, name="has_evidence", curie=GOCAM.curie('has_evidence'),
                   model_uri=GOCAM.has_evidence, domain=Association, range=Optional[Union[Dict[Union[str, EvidenceId], Union[dict, "Evidence"]], List[Union[dict, "Evidence"]]]])

slots.association_slot = Slot(uri=GOCAM.association_slot, name="association_slot", curie=GOCAM.curie('association_slot'),
                   model_uri=GOCAM.association_slot, domain=Association, range=Optional[str])

slots.subject = Slot(uri=RDF.subject, name="subject", curie=RDF.curie('subject'),
                   model_uri=GOCAM.subject, domain=Association, range=Optional[Union[str, DomainEntityId]])

slots.object = Slot(uri=RDF.object, name="object", curie=RDF.curie('object'),
                   model_uri=GOCAM.object, domain=Association, range=Union[str, EntityId])

slots.predicate = Slot(uri=RDF.predicate, name="predicate", curie=RDF.curie('predicate'),
                   model_uri=GOCAM.predicate, domain=Association, range=Optional[Union[str, PredicateType]])

slots.model_property = Slot(uri=GOCAM.model_property, name="model_property", curie=GOCAM.curie('model_property'),
                   model_uri=GOCAM.model_property, domain=None, range=Optional[str])

slots.title = Slot(uri=DCE.title, name="title", curie=DCE.curie('title'),
                   model_uri=GOCAM.title, domain=None, range=Optional[str])

slots.version = Slot(uri=OWL.versionIRI, name="version", curie=OWL.curie('versionIRI'),
                   model_uri=GOCAM.version, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.comment = Slot(uri=RDFS.comment, name="comment", curie=RDFS.curie('comment'),
                   model_uri=GOCAM.comment, domain=None, range=Optional[Union[str, List[str]]])

slots.state = Slot(uri=LEGO.modelstate, name="state", curie=LEGO.curie('modelstate'),
                   model_uri=GOCAM.state, domain=None, range=Optional[str])

slots.graph_type = Slot(uri=GOMODEL.graphType, name="graph_type", curie=GOMODEL.curie('graphType'),
                   model_uri=GOCAM.graph_type, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.in_taxon = Slot(uri=BIOLINK.in_taxon, name="in_taxon", curie=BIOLINK.curie('in_taxon'),
                   model_uri=GOCAM.in_taxon, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.domain_entity_set = Slot(uri=GOCAM.domain_entity_set, name="domain_entity_set", curie=GOCAM.curie('domain_entity_set'),
                   model_uri=GOCAM.domain_entity_set, domain=None, range=Optional[Union[Dict[Union[str, DomainEntityId], Union[dict, DomainEntity]], List[Union[dict, DomainEntity]]]])

slots.molecular_activity_set = Slot(uri=GOCAM.molecular_activity_set, name="molecular_activity_set", curie=GOCAM.curie('molecular_activity_set'),
                   model_uri=GOCAM.molecular_activity_set, domain=None, range=Optional[Union[Dict[Union[str, MolecularActivityId], Union[dict, MolecularActivity]], List[Union[dict, MolecularActivity]]]])

slots.biological_process_set = Slot(uri=GOCAM.biological_process_set, name="biological_process_set", curie=GOCAM.curie('biological_process_set'),
                   model_uri=GOCAM.biological_process_set, domain=None, range=Optional[Union[Dict[Union[str, BiologicalProcessId], Union[dict, BiologicalProcess]], List[Union[dict, BiologicalProcess]]]])

slots.information_biomacromolecule_set = Slot(uri=GOCAM.information_biomacromolecule_set, name="information_biomacromolecule_set", curie=GOCAM.curie('information_biomacromolecule_set'),
                   model_uri=GOCAM.information_biomacromolecule_set, domain=None, range=Optional[Union[Dict[Union[str, InformationBiomacromoleculeId], Union[dict, InformationBiomacromolecule]], List[Union[dict, InformationBiomacromolecule]]]])

slots.chemical_entity_set = Slot(uri=GOCAM.chemical_entity_set, name="chemical_entity_set", curie=GOCAM.curie('chemical_entity_set'),
                   model_uri=GOCAM.chemical_entity_set, domain=None, range=Optional[Union[Dict[Union[str, ChemicalEntityId], Union[dict, ChemicalEntity]], List[Union[dict, ChemicalEntity]]]])

slots.ontology_class_set = Slot(uri=GOCAM.ontology_class_set, name="ontology_class_set", curie=GOCAM.curie('ontology_class_set'),
                   model_uri=GOCAM.ontology_class_set, domain=None, range=Optional[Union[Dict[Union[str, OntologyClassId], Union[dict, OntologyClass]], List[Union[dict, OntologyClass]]]])

slots.MolecularActivity_part_of = Slot(uri=GOCAM.part_of, name="MolecularActivity_part_of", curie=GOCAM.curie('part_of'),
                   model_uri=GOCAM.MolecularActivity_part_of, domain=MolecularActivity, range=Optional[Union[Union[dict, "ProcessPartOfAssociation"], List[Union[dict, "ProcessPartOfAssociation"]]]])

slots.MolecularActivity_has_activity_causal_associations = Slot(uri=GOCAM.has_activity_causal_associations, name="MolecularActivity_has_activity_causal_associations", curie=GOCAM.curie('has_activity_causal_associations'),
                   model_uri=GOCAM.MolecularActivity_has_activity_causal_associations, domain=MolecularActivity, range=Optional[Union[Union[dict, "ActivityToActivityCausalAssociation"], List[Union[dict, "ActivityToActivityCausalAssociation"]]]])

slots.MolecularActivity_has_process_causal_associations = Slot(uri=GOCAM.has_process_causal_associations, name="MolecularActivity_has_process_causal_associations", curie=GOCAM.curie('has_process_causal_associations'),
                   model_uri=GOCAM.MolecularActivity_has_process_causal_associations, domain=MolecularActivity, range=Optional[Union[Union[dict, "ActivityToProcessCausalAssociation"], List[Union[dict, "ActivityToProcessCausalAssociation"]]]])

slots.BiologicalProcess_has_activity_causal_associations = Slot(uri=GOCAM.has_activity_causal_associations, name="BiologicalProcess_has_activity_causal_associations", curie=GOCAM.curie('has_activity_causal_associations'),
                   model_uri=GOCAM.BiologicalProcess_has_activity_causal_associations, domain=BiologicalProcess, range=Optional[Union[Union[dict, "ProcessToActivityCausalAssociation"], List[Union[dict, "ProcessToActivityCausalAssociation"]]]])

slots.BiologicalProcess_has_process_causal_associations = Slot(uri=GOCAM.has_process_causal_associations, name="BiologicalProcess_has_process_causal_associations", curie=GOCAM.curie('has_process_causal_associations'),
                   model_uri=GOCAM.BiologicalProcess_has_process_causal_associations, domain=BiologicalProcess, range=Optional[Union[Union[dict, "ProcessToProcessCausalAssociation"], List[Union[dict, "ProcessToProcessCausalAssociation"]]]])

slots.AnatomicalEntity_category = Slot(uri=GOCAM.category, name="AnatomicalEntity_category", curie=GOCAM.curie('category'),
                   model_uri=GOCAM.AnatomicalEntity_category, domain=AnatomicalEntity, range=Union[str, "AnatomicalEntityCategory"])

slots.AnatomicalEntity_part_of = Slot(uri=GOCAM.part_of, name="AnatomicalEntity_part_of", curie=GOCAM.curie('part_of'),
                   model_uri=GOCAM.AnatomicalEntity_part_of, domain=AnatomicalEntity, range=Optional[Union[Union[dict, "AnatomicalPartOfAssociation"], List[Union[dict, "AnatomicalPartOfAssociation"]]]])

slots.InformationBiomacromolecule_category = Slot(uri=GOCAM.category, name="InformationBiomacromolecule_category", curie=GOCAM.curie('category'),
                   model_uri=GOCAM.InformationBiomacromolecule_category, domain=InformationBiomacromolecule, range=Union[str, "InformationBiomacromoleculeCategory"])

slots.InformationBiomacromolecule_has_part = Slot(uri=GOCAM.has_part, name="InformationBiomacromolecule_has_part", curie=GOCAM.curie('has_part'),
                   model_uri=GOCAM.InformationBiomacromolecule_has_part, domain=InformationBiomacromolecule, range=Optional[Union[Union[dict, "MacromoleculeHasPartAssociation"], List[Union[dict, "MacromoleculeHasPartAssociation"]]]])

slots.OccursInAssociation_object = Slot(uri=RDF.object, name="OccursInAssociation_object", curie=RDF.curie('object'),
                   model_uri=GOCAM.OccursInAssociation_object, domain=OccursInAssociation, range=Union[str, AnatomicalEntityId])

slots.CausalAssociation_subject = Slot(uri=RDF.subject, name="CausalAssociation_subject", curie=RDF.curie('subject'),
                   model_uri=GOCAM.CausalAssociation_subject, domain=CausalAssociation, range=Optional[Union[str, DomainEntityId]])

slots.CausalAssociation_object = Slot(uri=RDF.object, name="CausalAssociation_object", curie=RDF.curie('object'),
                   model_uri=GOCAM.CausalAssociation_object, domain=CausalAssociation, range=Union[str, ActivityOrProcessId])

slots.CausalAssociation_predicate = Slot(uri=RDF.predicate, name="CausalAssociation_predicate", curie=RDF.curie('predicate'),
                   model_uri=GOCAM.CausalAssociation_predicate, domain=CausalAssociation, range=Optional[Union[str, PredicateType]])

slots.CausalAssociationToActivity_object = Slot(uri=RDF.object, name="CausalAssociationToActivity_object", curie=RDF.curie('object'),
                   model_uri=GOCAM.CausalAssociationToActivity_object, domain=None, range=Union[str, MolecularActivityId])

slots.CausalAssociationToProcess_object = Slot(uri=RDF.object, name="CausalAssociationToProcess_object", curie=RDF.curie('object'),
                   model_uri=GOCAM.CausalAssociationToProcess_object, domain=None, range=Union[str, BiologicalProcessId])

slots.ActivityToActivityCausalAssociation_subject = Slot(uri=RDF.subject, name="ActivityToActivityCausalAssociation_subject", curie=RDF.curie('subject'),
                   model_uri=GOCAM.ActivityToActivityCausalAssociation_subject, domain=ActivityToActivityCausalAssociation, range=Optional[Union[str, MolecularActivityId]])

slots.ActivityToActivityCausalAssociation_object = Slot(uri=RDF.object, name="ActivityToActivityCausalAssociation_object", curie=RDF.curie('object'),
                   model_uri=GOCAM.ActivityToActivityCausalAssociation_object, domain=ActivityToActivityCausalAssociation, range=Union[str, MolecularActivityId])

slots.ProcessToProcessCausalAssociation_subject = Slot(uri=RDF.subject, name="ProcessToProcessCausalAssociation_subject", curie=RDF.curie('subject'),
                   model_uri=GOCAM.ProcessToProcessCausalAssociation_subject, domain=ProcessToProcessCausalAssociation, range=Optional[Union[str, BiologicalProcessId]])

slots.ProcessToProcessCausalAssociation_object = Slot(uri=RDF.object, name="ProcessToProcessCausalAssociation_object", curie=RDF.curie('object'),
                   model_uri=GOCAM.ProcessToProcessCausalAssociation_object, domain=ProcessToProcessCausalAssociation, range=Union[str, BiologicalProcessId])

slots.ProcessToActivityCausalAssociation_subject = Slot(uri=RDF.subject, name="ProcessToActivityCausalAssociation_subject", curie=RDF.curie('subject'),
                   model_uri=GOCAM.ProcessToActivityCausalAssociation_subject, domain=ProcessToActivityCausalAssociation, range=Optional[Union[str, BiologicalProcessId]])

slots.ProcessToActivityCausalAssociation_object = Slot(uri=RDF.object, name="ProcessToActivityCausalAssociation_object", curie=RDF.curie('object'),
                   model_uri=GOCAM.ProcessToActivityCausalAssociation_object, domain=ProcessToActivityCausalAssociation, range=Union[str, MolecularActivityId])

slots.ActivityToProcessCausalAssociation_subject = Slot(uri=RDF.subject, name="ActivityToProcessCausalAssociation_subject", curie=RDF.curie('subject'),
                   model_uri=GOCAM.ActivityToProcessCausalAssociation_subject, domain=ActivityToProcessCausalAssociation, range=Optional[Union[str, MolecularActivityId]])

slots.ActivityToProcessCausalAssociation_object = Slot(uri=RDF.object, name="ActivityToProcessCausalAssociation_object", curie=RDF.curie('object'),
                   model_uri=GOCAM.ActivityToProcessCausalAssociation_object, domain=ActivityToProcessCausalAssociation, range=Union[str, BiologicalProcessId])

slots.MacromoleculeHasPartAssociation_object = Slot(uri=RDF.object, name="MacromoleculeHasPartAssociation_object", curie=RDF.curie('object'),
                   model_uri=GOCAM.MacromoleculeHasPartAssociation_object, domain=MacromoleculeHasPartAssociation, range=Union[str, ContinuantId])

slots.AnatomicalPartOfAssociation_object = Slot(uri=RDF.object, name="AnatomicalPartOfAssociation_object", curie=RDF.curie('object'),
                   model_uri=GOCAM.AnatomicalPartOfAssociation_object, domain=AnatomicalPartOfAssociation, range=Union[str, AnatomicalEntityId])

slots.ProcessPartOfAssociation_object = Slot(uri=RDF.object, name="ProcessPartOfAssociation_object", curie=RDF.curie('object'),
                   model_uri=GOCAM.ProcessPartOfAssociation_object, domain=ProcessPartOfAssociation, range=Union[str, BiologicalProcessId])

slots.EnabledByAssociation_object = Slot(uri=RDF.object, name="EnabledByAssociation_object", curie=RDF.curie('object'),
                   model_uri=GOCAM.EnabledByAssociation_object, domain=EnabledByAssociation, range=Union[str, InformationBiomacromoleculeId])

slots.HappensDuringAssociation_object = Slot(uri=RDF.object, name="HappensDuringAssociation_object", curie=RDF.curie('object'),
                   model_uri=GOCAM.HappensDuringAssociation_object, domain=HappensDuringAssociation, range=Union[str, ActivityOrProcessId])

slots.HasInputAssociation_object = Slot(uri=RDF.object, name="HasInputAssociation_object", curie=RDF.curie('object'),
                   model_uri=GOCAM.HasInputAssociation_object, domain=HasInputAssociation, range=Union[str, ContinuantId])
