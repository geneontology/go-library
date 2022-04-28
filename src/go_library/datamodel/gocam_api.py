
import logging
from dataclasses import dataclass
from linkml_dataops.query.queryengine import QueryEngine
from linkml_dataops.query.query_model import FetchQuery, Constraint, MatchConstraint, OrConstraint, AbstractQuery,     FetchById
from linkml_dataops.query.queryengine import MatchExpression

from .test_gocam import *

@dataclass
class TestGocamAPI:

    # attributes
    query_engine: QueryEngine = None

    
    # --
    # Entity methods
    # --
    def fetch_Entity(self, id_value: str) -> Entity:
        """
        Retrieves an instance of `Entity` via a primary key

        :param id_value:
        :return: Entity with matching ID
        """
        q = FetchById(id=id_value, target_class=Entity.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_Entity(self,
             id: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[Entity]:
        """
        Queries for instances of `Entity`

        :param id: A unique identifier for an Entity
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(Entity.class_name,
                                                 
                                                 id=id,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # Model methods
    # --
    def fetch_Model(self, id_value: str) -> Model:
        """
        Retrieves an instance of `Model` via a primary key

        :param id_value:
        :return: Model with matching ID
        """
        q = FetchById(id=id_value, target_class=Model.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_Model(self,
             id: Union[str, MatchExpression] = None,
             title: Union[str, MatchExpression] = None,
             contributor: Union[str, MatchExpression] = None,
             date: Union[str, MatchExpression] = None,
             state: Union[str, MatchExpression] = None,
             provided_by: Union[str, MatchExpression] = None,
             molecular_activity_set: Union[str, MatchExpression] = None,
             biological_process_set: Union[str, MatchExpression] = None,
             information_biomacromolecule_set: Union[str, MatchExpression] = None,
             chemical_entity_set: Union[str, MatchExpression] = None,
             ontology_class_set: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[Model]:
        """
        Queries for instances of `Model`

        :param id: A unique identifier for an Entity
        :param title: None
        :param contributor: connects an assertion to the individual that made a contribution to it
        :param date: connects anything to the date
        :param state: State of the model
        :param provided_by: connects an assertion to a group that provided it
        :param molecular_activity_set: All MolecularActivity instances that are part_of this model
        :param biological_process_set: All BiologicalProcess instances that are part_of this model
        :param information_biomacromolecule_set: All information macromolecule instances that are part_of this model
        :param chemical_entity_set: All ChemicalEntity instances that are part_of this model.
        :param ontology_class_set: All OntologyClass objects used in this model
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(Model.class_name,
                                                 
                                                 id=id,
                                                 
                                                 title=title,
                                                 
                                                 contributor=contributor,
                                                 
                                                 date=date,
                                                 
                                                 state=state,
                                                 
                                                 provided_by=provided_by,
                                                 
                                                 molecular_activity_set=molecular_activity_set,
                                                 
                                                 biological_process_set=biological_process_set,
                                                 
                                                 information_biomacromolecule_set=information_biomacromolecule_set,
                                                 
                                                 chemical_entity_set=chemical_entity_set,
                                                 
                                                 ontology_class_set=ontology_class_set,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # DomainEntity methods
    # --
    def fetch_DomainEntity(self, id_value: str) -> DomainEntity:
        """
        Retrieves an instance of `DomainEntity` via a primary key

        :param id_value:
        :return: DomainEntity with matching ID
        """
        q = FetchById(id=id_value, target_class=DomainEntity.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_DomainEntity(self,
             id: Union[str, MatchExpression] = None,
             type: Union[str, MatchExpression] = None,
             type_inferences: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[DomainEntity]:
        """
        Queries for instances of `DomainEntity`

        :param id: A unique identifier for an Entity
        :param type: links a GOCAM Entity (an OWL individual) to the specific class it instantiates
        :param type_inferences: links a GOCAM Entity (an OWL individual) to the specific class it instantiates
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(DomainEntity.class_name,
                                                 
                                                 id=id,
                                                 
                                                 type=type,
                                                 
                                                 type_inferences=type_inferences,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # MolecularActivity methods
    # --
    def fetch_MolecularActivity(self, id_value: str) -> MolecularActivity:
        """
        Retrieves an instance of `MolecularActivity` via a primary key

        :param id_value:
        :return: MolecularActivity with matching ID
        """
        q = FetchById(id=id_value, target_class=MolecularActivity.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_MolecularActivity(self,
             has_activity_causal_associations: Union[str, MatchExpression] = None,
             has_process_causal_associations: Union[str, MatchExpression] = None,
             happens_during: Union[str, MatchExpression] = None,
             part_of: Union[str, MatchExpression] = None,
             enabled_by: Union[str, MatchExpression] = None,
             has_input: Union[str, MatchExpression] = None,
             occurs_in: Union[str, MatchExpression] = None,
             id: Union[str, MatchExpression] = None,
             type: Union[str, MatchExpression] = None,
             type_inferences: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[MolecularActivity]:
        """
        Queries for instances of `MolecularActivity`

        :param has_activity_causal_associations: Links a subject DomainEntity (a MA or BP) to a MolecularActivity by way of an CausalAssociation
        :param has_process_causal_associations: Links a subject DomainEntity (a MA or BP) to a BiologicalProcess by way of an CausalAssociation
        :param happens_during: Links a subject DomainEntity (a MA or BP) to an object DomainEntity by way of a HappensDuringAssociation 
        :param part_of: Links a subject DomainEntity to an object DomainEntity by way of a PartOfAssociation
        :param enabled_by: Links a MolecularActivity to the InformationBiomacromolecule by way of a EnabledByAssociation
        :param has_input: Links a MA or BP to its input by way of a HasInputAssociation
        :param occurs_in: Links a subject DomainEntity (a MA or BP) to an object DomainEntity by way of an OccursInAssociation
        :param id: A unique identifier for an Entity
        :param type: links a GOCAM Entity (an OWL individual) to the specific class it instantiates
        :param type_inferences: links a GOCAM Entity (an OWL individual) to the specific class it instantiates
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(MolecularActivity.class_name,
                                                 
                                                 has_activity_causal_associations=has_activity_causal_associations,
                                                 
                                                 has_process_causal_associations=has_process_causal_associations,
                                                 
                                                 happens_during=happens_during,
                                                 
                                                 part_of=part_of,
                                                 
                                                 enabled_by=enabled_by,
                                                 
                                                 has_input=has_input,
                                                 
                                                 occurs_in=occurs_in,
                                                 
                                                 id=id,
                                                 
                                                 type=type,
                                                 
                                                 type_inferences=type_inferences,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # BiologicalProcess methods
    # --
    def fetch_BiologicalProcess(self, id_value: str) -> BiologicalProcess:
        """
        Retrieves an instance of `BiologicalProcess` via a primary key

        :param id_value:
        :return: BiologicalProcess with matching ID
        """
        q = FetchById(id=id_value, target_class=BiologicalProcess.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_BiologicalProcess(self,
             occurs_in: Union[str, MatchExpression] = None,
             has_activity_causal_associations: Union[str, MatchExpression] = None,
             has_process_causal_associations: Union[str, MatchExpression] = None,
             happens_during: Union[str, MatchExpression] = None,
             id: Union[str, MatchExpression] = None,
             type: Union[str, MatchExpression] = None,
             type_inferences: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[BiologicalProcess]:
        """
        Queries for instances of `BiologicalProcess`

        :param occurs_in: Links a subject DomainEntity (a MA or BP) to an object DomainEntity by way of an OccursInAssociation
        :param has_activity_causal_associations: Links a subject DomainEntity (a MA or BP) to a MolecularActivity by way of an CausalAssociation
        :param has_process_causal_associations: Links a subject DomainEntity (a MA or BP) to a BiologicalProcess by way of an CausalAssociation
        :param happens_during: Links a subject DomainEntity (a MA or BP) to an object DomainEntity by way of a HappensDuringAssociation 
        :param id: A unique identifier for an Entity
        :param type: links a GOCAM Entity (an OWL individual) to the specific class it instantiates
        :param type_inferences: links a GOCAM Entity (an OWL individual) to the specific class it instantiates
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(BiologicalProcess.class_name,
                                                 
                                                 occurs_in=occurs_in,
                                                 
                                                 has_activity_causal_associations=has_activity_causal_associations,
                                                 
                                                 has_process_causal_associations=has_process_causal_associations,
                                                 
                                                 happens_during=happens_during,
                                                 
                                                 id=id,
                                                 
                                                 type=type,
                                                 
                                                 type_inferences=type_inferences,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # AnatomicalEntity methods
    # --
    def fetch_AnatomicalEntity(self, id_value: str) -> AnatomicalEntity:
        """
        Retrieves an instance of `AnatomicalEntity` via a primary key

        :param id_value:
        :return: AnatomicalEntity with matching ID
        """
        q = FetchById(id=id_value, target_class=AnatomicalEntity.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_AnatomicalEntity(self,
             part_of: Union[str, MatchExpression] = None,
             id: Union[str, MatchExpression] = None,
             type: Union[str, MatchExpression] = None,
             type_inferences: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[AnatomicalEntity]:
        """
        Queries for instances of `AnatomicalEntity`

        :param part_of: Links a subject DomainEntity to an object DomainEntity by way of a PartOfAssociation
        :param id: A unique identifier for an Entity
        :param type: links a GOCAM Entity (an OWL individual) to the specific class it instantiates
        :param type_inferences: links a GOCAM Entity (an OWL individual) to the specific class it instantiates
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(AnatomicalEntity.class_name,
                                                 
                                                 part_of=part_of,
                                                 
                                                 id=id,
                                                 
                                                 type=type,
                                                 
                                                 type_inferences=type_inferences,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # ChemicalEntity methods
    # --
    def fetch_ChemicalEntity(self, id_value: str) -> ChemicalEntity:
        """
        Retrieves an instance of `ChemicalEntity` via a primary key

        :param id_value:
        :return: ChemicalEntity with matching ID
        """
        q = FetchById(id=id_value, target_class=ChemicalEntity.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_ChemicalEntity(self,
             id: Union[str, MatchExpression] = None,
             type: Union[str, MatchExpression] = None,
             type_inferences: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[ChemicalEntity]:
        """
        Queries for instances of `ChemicalEntity`

        :param id: A unique identifier for an Entity
        :param type: links a GOCAM Entity (an OWL individual) to the specific class it instantiates
        :param type_inferences: links a GOCAM Entity (an OWL individual) to the specific class it instantiates
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(ChemicalEntity.class_name,
                                                 
                                                 id=id,
                                                 
                                                 type=type,
                                                 
                                                 type_inferences=type_inferences,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # InformationBiomacromolecule methods
    # --
    def fetch_InformationBiomacromolecule(self, id_value: str) -> InformationBiomacromolecule:
        """
        Retrieves an instance of `InformationBiomacromolecule` via a primary key

        :param id_value:
        :return: InformationBiomacromolecule with matching ID
        """
        q = FetchById(id=id_value, target_class=InformationBiomacromolecule.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_InformationBiomacromolecule(self,
             has_part: Union[str, MatchExpression] = None,
             id: Union[str, MatchExpression] = None,
             type: Union[str, MatchExpression] = None,
             type_inferences: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[InformationBiomacromolecule]:
        """
        Queries for instances of `InformationBiomacromolecule`

        :param has_part: Links a subject DomainEntity to an object DomainEntity by way of a HasPartAssociation
        :param id: A unique identifier for an Entity
        :param type: links a GOCAM Entity (an OWL individual) to the specific class it instantiates
        :param type_inferences: links a GOCAM Entity (an OWL individual) to the specific class it instantiates
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(InformationBiomacromolecule.class_name,
                                                 
                                                 has_part=has_part,
                                                 
                                                 id=id,
                                                 
                                                 type=type,
                                                 
                                                 type_inferences=type_inferences,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # Association methods
    # --
    def fetch_Association(self, id_value: str) -> Association:
        """
        Retrieves an instance of `Association` via a primary key

        :param id_value:
        :return: Association with matching ID
        """
        q = FetchById(id=id_value, target_class=Association.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_Association(self,
             has_evidence: Union[str, MatchExpression] = None,
             subject: Union[str, MatchExpression] = None,
             predicate: Union[str, MatchExpression] = None,
             object: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[Association]:
        """
        Queries for instances of `Association`

        :param has_evidence: Links an association to evidence for it
        :param subject: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
        :param predicate: A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.
        :param object: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(Association.class_name,
                                                 
                                                 has_evidence=has_evidence,
                                                 
                                                 subject=subject,
                                                 
                                                 predicate=predicate,
                                                 
                                                 object=object,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # OccursInAssociation methods
    # --
    def fetch_OccursInAssociation(self, id_value: str) -> OccursInAssociation:
        """
        Retrieves an instance of `OccursInAssociation` via a primary key

        :param id_value:
        :return: OccursInAssociation with matching ID
        """
        q = FetchById(id=id_value, target_class=OccursInAssociation.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_OccursInAssociation(self,
             has_evidence: Union[str, MatchExpression] = None,
             subject: Union[str, MatchExpression] = None,
             predicate: Union[str, MatchExpression] = None,
             object: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[OccursInAssociation]:
        """
        Queries for instances of `OccursInAssociation`

        :param has_evidence: Links an association to evidence for it
        :param subject: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
        :param predicate: A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.
        :param object: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(OccursInAssociation.class_name,
                                                 
                                                 has_evidence=has_evidence,
                                                 
                                                 subject=subject,
                                                 
                                                 predicate=predicate,
                                                 
                                                 object=object,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # CausalAssociation methods
    # --
    def fetch_CausalAssociation(self, id_value: str) -> CausalAssociation:
        """
        Retrieves an instance of `CausalAssociation` via a primary key

        :param id_value:
        :return: CausalAssociation with matching ID
        """
        q = FetchById(id=id_value, target_class=CausalAssociation.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_CausalAssociation(self,
             has_evidence: Union[str, MatchExpression] = None,
             subject: Union[str, MatchExpression] = None,
             predicate: Union[str, MatchExpression] = None,
             object: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[CausalAssociation]:
        """
        Queries for instances of `CausalAssociation`

        :param has_evidence: Links an association to evidence for it
        :param subject: The upstream ActivityOrProcess
        :param predicate: The causal relationship type which holds between the two activities/processes. This must be drawn from the causal relation hierarchy in RO
        :param object: The upstream ActivityOrProcess
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(CausalAssociation.class_name,
                                                 
                                                 has_evidence=has_evidence,
                                                 
                                                 subject=subject,
                                                 
                                                 predicate=predicate,
                                                 
                                                 object=object,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # CausalAssociationToActivity methods
    # --
    def fetch_CausalAssociationToActivity(self, id_value: str) -> CausalAssociationToActivity:
        """
        Retrieves an instance of `CausalAssociationToActivity` via a primary key

        :param id_value:
        :return: CausalAssociationToActivity with matching ID
        """
        q = FetchById(id=id_value, target_class=CausalAssociationToActivity.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_CausalAssociationToActivity(self,
             
             _extra: Any = None) -> List[CausalAssociationToActivity]:
        """
        Queries for instances of `CausalAssociationToActivity`

        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(CausalAssociationToActivity.class_name,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # CausalAssociationToProcess methods
    # --
    def fetch_CausalAssociationToProcess(self, id_value: str) -> CausalAssociationToProcess:
        """
        Retrieves an instance of `CausalAssociationToProcess` via a primary key

        :param id_value:
        :return: CausalAssociationToProcess with matching ID
        """
        q = FetchById(id=id_value, target_class=CausalAssociationToProcess.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_CausalAssociationToProcess(self,
             
             _extra: Any = None) -> List[CausalAssociationToProcess]:
        """
        Queries for instances of `CausalAssociationToProcess`

        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(CausalAssociationToProcess.class_name,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # ActivityToActivityCausalAssociation methods
    # --
    def fetch_ActivityToActivityCausalAssociation(self, id_value: str) -> ActivityToActivityCausalAssociation:
        """
        Retrieves an instance of `ActivityToActivityCausalAssociation` via a primary key

        :param id_value:
        :return: ActivityToActivityCausalAssociation with matching ID
        """
        q = FetchById(id=id_value, target_class=ActivityToActivityCausalAssociation.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_ActivityToActivityCausalAssociation(self,
             has_evidence: Union[str, MatchExpression] = None,
             subject: Union[str, MatchExpression] = None,
             predicate: Union[str, MatchExpression] = None,
             object: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[ActivityToActivityCausalAssociation]:
        """
        Queries for instances of `ActivityToActivityCausalAssociation`

        :param has_evidence: Links an association to evidence for it
        :param subject: The upstream MolecularActivity
        :param predicate: A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.
        :param object: The downstream MolecularActivity
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(ActivityToActivityCausalAssociation.class_name,
                                                 
                                                 has_evidence=has_evidence,
                                                 
                                                 subject=subject,
                                                 
                                                 predicate=predicate,
                                                 
                                                 object=object,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # ProcessToProcessCausalAssociation methods
    # --
    def fetch_ProcessToProcessCausalAssociation(self, id_value: str) -> ProcessToProcessCausalAssociation:
        """
        Retrieves an instance of `ProcessToProcessCausalAssociation` via a primary key

        :param id_value:
        :return: ProcessToProcessCausalAssociation with matching ID
        """
        q = FetchById(id=id_value, target_class=ProcessToProcessCausalAssociation.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_ProcessToProcessCausalAssociation(self,
             has_evidence: Union[str, MatchExpression] = None,
             subject: Union[str, MatchExpression] = None,
             predicate: Union[str, MatchExpression] = None,
             object: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[ProcessToProcessCausalAssociation]:
        """
        Queries for instances of `ProcessToProcessCausalAssociation`

        :param has_evidence: Links an association to evidence for it
        :param subject: The upstream BiologicalProcess
        :param predicate: A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.
        :param object: The downstream BiologicalProcess
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(ProcessToProcessCausalAssociation.class_name,
                                                 
                                                 has_evidence=has_evidence,
                                                 
                                                 subject=subject,
                                                 
                                                 predicate=predicate,
                                                 
                                                 object=object,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # ProcessToActivityCausalAssociation methods
    # --
    def fetch_ProcessToActivityCausalAssociation(self, id_value: str) -> ProcessToActivityCausalAssociation:
        """
        Retrieves an instance of `ProcessToActivityCausalAssociation` via a primary key

        :param id_value:
        :return: ProcessToActivityCausalAssociation with matching ID
        """
        q = FetchById(id=id_value, target_class=ProcessToActivityCausalAssociation.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_ProcessToActivityCausalAssociation(self,
             has_evidence: Union[str, MatchExpression] = None,
             subject: Union[str, MatchExpression] = None,
             predicate: Union[str, MatchExpression] = None,
             object: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[ProcessToActivityCausalAssociation]:
        """
        Queries for instances of `ProcessToActivityCausalAssociation`

        :param has_evidence: Links an association to evidence for it
        :param subject: The upstream BiologicalProcess
        :param predicate: A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.
        :param object: The downstream MolecularActivity
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(ProcessToActivityCausalAssociation.class_name,
                                                 
                                                 has_evidence=has_evidence,
                                                 
                                                 subject=subject,
                                                 
                                                 predicate=predicate,
                                                 
                                                 object=object,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # ActivityToProcessCausalAssociation methods
    # --
    def fetch_ActivityToProcessCausalAssociation(self, id_value: str) -> ActivityToProcessCausalAssociation:
        """
        Retrieves an instance of `ActivityToProcessCausalAssociation` via a primary key

        :param id_value:
        :return: ActivityToProcessCausalAssociation with matching ID
        """
        q = FetchById(id=id_value, target_class=ActivityToProcessCausalAssociation.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_ActivityToProcessCausalAssociation(self,
             has_evidence: Union[str, MatchExpression] = None,
             subject: Union[str, MatchExpression] = None,
             predicate: Union[str, MatchExpression] = None,
             object: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[ActivityToProcessCausalAssociation]:
        """
        Queries for instances of `ActivityToProcessCausalAssociation`

        :param has_evidence: Links an association to evidence for it
        :param subject: The downstream MolecularActivity
        :param predicate: A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.
        :param object: The upstream BiologicalProcess
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(ActivityToProcessCausalAssociation.class_name,
                                                 
                                                 has_evidence=has_evidence,
                                                 
                                                 subject=subject,
                                                 
                                                 predicate=predicate,
                                                 
                                                 object=object,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # HasPartAssociation methods
    # --
    def fetch_HasPartAssociation(self, id_value: str) -> HasPartAssociation:
        """
        Retrieves an instance of `HasPartAssociation` via a primary key

        :param id_value:
        :return: HasPartAssociation with matching ID
        """
        q = FetchById(id=id_value, target_class=HasPartAssociation.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_HasPartAssociation(self,
             has_evidence: Union[str, MatchExpression] = None,
             subject: Union[str, MatchExpression] = None,
             predicate: Union[str, MatchExpression] = None,
             object: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[HasPartAssociation]:
        """
        Queries for instances of `HasPartAssociation`

        :param has_evidence: Links an association to evidence for it
        :param subject: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
        :param predicate: A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.
        :param object: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(HasPartAssociation.class_name,
                                                 
                                                 has_evidence=has_evidence,
                                                 
                                                 subject=subject,
                                                 
                                                 predicate=predicate,
                                                 
                                                 object=object,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # MacromoleculeHasPartAssociation methods
    # --
    def fetch_MacromoleculeHasPartAssociation(self, id_value: str) -> MacromoleculeHasPartAssociation:
        """
        Retrieves an instance of `MacromoleculeHasPartAssociation` via a primary key

        :param id_value:
        :return: MacromoleculeHasPartAssociation with matching ID
        """
        q = FetchById(id=id_value, target_class=MacromoleculeHasPartAssociation.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_MacromoleculeHasPartAssociation(self,
             has_evidence: Union[str, MatchExpression] = None,
             subject: Union[str, MatchExpression] = None,
             predicate: Union[str, MatchExpression] = None,
             object: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[MacromoleculeHasPartAssociation]:
        """
        Queries for instances of `MacromoleculeHasPartAssociation`

        :param has_evidence: Links an association to evidence for it
        :param subject: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
        :param predicate: A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.
        :param object: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(MacromoleculeHasPartAssociation.class_name,
                                                 
                                                 has_evidence=has_evidence,
                                                 
                                                 subject=subject,
                                                 
                                                 predicate=predicate,
                                                 
                                                 object=object,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # PartOfAssociation methods
    # --
    def fetch_PartOfAssociation(self, id_value: str) -> PartOfAssociation:
        """
        Retrieves an instance of `PartOfAssociation` via a primary key

        :param id_value:
        :return: PartOfAssociation with matching ID
        """
        q = FetchById(id=id_value, target_class=PartOfAssociation.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_PartOfAssociation(self,
             has_evidence: Union[str, MatchExpression] = None,
             subject: Union[str, MatchExpression] = None,
             predicate: Union[str, MatchExpression] = None,
             object: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[PartOfAssociation]:
        """
        Queries for instances of `PartOfAssociation`

        :param has_evidence: Links an association to evidence for it
        :param subject: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
        :param predicate: A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.
        :param object: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(PartOfAssociation.class_name,
                                                 
                                                 has_evidence=has_evidence,
                                                 
                                                 subject=subject,
                                                 
                                                 predicate=predicate,
                                                 
                                                 object=object,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # AnatomicalPartOfAssociation methods
    # --
    def fetch_AnatomicalPartOfAssociation(self, id_value: str) -> AnatomicalPartOfAssociation:
        """
        Retrieves an instance of `AnatomicalPartOfAssociation` via a primary key

        :param id_value:
        :return: AnatomicalPartOfAssociation with matching ID
        """
        q = FetchById(id=id_value, target_class=AnatomicalPartOfAssociation.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_AnatomicalPartOfAssociation(self,
             has_evidence: Union[str, MatchExpression] = None,
             subject: Union[str, MatchExpression] = None,
             predicate: Union[str, MatchExpression] = None,
             object: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[AnatomicalPartOfAssociation]:
        """
        Queries for instances of `AnatomicalPartOfAssociation`

        :param has_evidence: Links an association to evidence for it
        :param subject: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
        :param predicate: A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.
        :param object: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(AnatomicalPartOfAssociation.class_name,
                                                 
                                                 has_evidence=has_evidence,
                                                 
                                                 subject=subject,
                                                 
                                                 predicate=predicate,
                                                 
                                                 object=object,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # ProcessPartOfAssociation methods
    # --
    def fetch_ProcessPartOfAssociation(self, id_value: str) -> ProcessPartOfAssociation:
        """
        Retrieves an instance of `ProcessPartOfAssociation` via a primary key

        :param id_value:
        :return: ProcessPartOfAssociation with matching ID
        """
        q = FetchById(id=id_value, target_class=ProcessPartOfAssociation.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_ProcessPartOfAssociation(self,
             has_evidence: Union[str, MatchExpression] = None,
             subject: Union[str, MatchExpression] = None,
             predicate: Union[str, MatchExpression] = None,
             object: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[ProcessPartOfAssociation]:
        """
        Queries for instances of `ProcessPartOfAssociation`

        :param has_evidence: Links an association to evidence for it
        :param subject: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
        :param predicate: A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.
        :param object: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(ProcessPartOfAssociation.class_name,
                                                 
                                                 has_evidence=has_evidence,
                                                 
                                                 subject=subject,
                                                 
                                                 predicate=predicate,
                                                 
                                                 object=object,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # EnabledByAssociation methods
    # --
    def fetch_EnabledByAssociation(self, id_value: str) -> EnabledByAssociation:
        """
        Retrieves an instance of `EnabledByAssociation` via a primary key

        :param id_value:
        :return: EnabledByAssociation with matching ID
        """
        q = FetchById(id=id_value, target_class=EnabledByAssociation.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_EnabledByAssociation(self,
             has_evidence: Union[str, MatchExpression] = None,
             subject: Union[str, MatchExpression] = None,
             predicate: Union[str, MatchExpression] = None,
             object: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[EnabledByAssociation]:
        """
        Queries for instances of `EnabledByAssociation`

        :param has_evidence: Links an association to evidence for it
        :param subject: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
        :param predicate: A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.
        :param object: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(EnabledByAssociation.class_name,
                                                 
                                                 has_evidence=has_evidence,
                                                 
                                                 subject=subject,
                                                 
                                                 predicate=predicate,
                                                 
                                                 object=object,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # HappensDuringAssociation methods
    # --
    def fetch_HappensDuringAssociation(self, id_value: str) -> HappensDuringAssociation:
        """
        Retrieves an instance of `HappensDuringAssociation` via a primary key

        :param id_value:
        :return: HappensDuringAssociation with matching ID
        """
        q = FetchById(id=id_value, target_class=HappensDuringAssociation.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_HappensDuringAssociation(self,
             has_evidence: Union[str, MatchExpression] = None,
             subject: Union[str, MatchExpression] = None,
             predicate: Union[str, MatchExpression] = None,
             object: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[HappensDuringAssociation]:
        """
        Queries for instances of `HappensDuringAssociation`

        :param has_evidence: Links an association to evidence for it
        :param subject: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
        :param predicate: A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.
        :param object: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(HappensDuringAssociation.class_name,
                                                 
                                                 has_evidence=has_evidence,
                                                 
                                                 subject=subject,
                                                 
                                                 predicate=predicate,
                                                 
                                                 object=object,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # HasInputAssociation methods
    # --
    def fetch_HasInputAssociation(self, id_value: str) -> HasInputAssociation:
        """
        Retrieves an instance of `HasInputAssociation` via a primary key

        :param id_value:
        :return: HasInputAssociation with matching ID
        """
        q = FetchById(id=id_value, target_class=HasInputAssociation.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_HasInputAssociation(self,
             has_evidence: Union[str, MatchExpression] = None,
             subject: Union[str, MatchExpression] = None,
             predicate: Union[str, MatchExpression] = None,
             object: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[HasInputAssociation]:
        """
        Queries for instances of `HasInputAssociation`

        :param has_evidence: Links an association to evidence for it
        :param subject: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
        :param predicate: A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.
        :param object: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(HasInputAssociation.class_name,
                                                 
                                                 has_evidence=has_evidence,
                                                 
                                                 subject=subject,
                                                 
                                                 predicate=predicate,
                                                 
                                                 object=object,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # OntologyClass methods
    # --
    def fetch_OntologyClass(self, id_value: str) -> OntologyClass:
        """
        Retrieves an instance of `OntologyClass` via a primary key

        :param id_value:
        :return: OntologyClass with matching ID
        """
        q = FetchById(id=id_value, target_class=OntologyClass.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_OntologyClass(self,
             id: Union[str, MatchExpression] = None,
             name: Union[str, MatchExpression] = None,
             category: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[OntologyClass]:
        """
        Queries for instances of `OntologyClass`

        :param id: A unique identifier for an Entity
        :param name: A human-readable name for an attribute or Entity.
        :param category: Name of the high level OntologyClass in which this Entity is categorized
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(OntologyClass.class_name,
                                                 
                                                 id=id,
                                                 
                                                 name=name,
                                                 
                                                 category=category,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # InformationEntity methods
    # --
    def fetch_InformationEntity(self, id_value: str) -> InformationEntity:
        """
        Retrieves an instance of `InformationEntity` via a primary key

        :param id_value:
        :return: InformationEntity with matching ID
        """
        q = FetchById(id=id_value, target_class=InformationEntity.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_InformationEntity(self,
             id: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[InformationEntity]:
        """
        Queries for instances of `InformationEntity`

        :param id: A unique identifier for an Entity
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(InformationEntity.class_name,
                                                 
                                                 id=id,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # Publication methods
    # --
    def fetch_Publication(self, id_value: str) -> Publication:
        """
        Retrieves an instance of `Publication` via a primary key

        :param id_value:
        :return: Publication with matching ID
        """
        q = FetchById(id=id_value, target_class=Publication.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_Publication(self,
             id: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[Publication]:
        """
        Queries for instances of `Publication`

        :param id: A unique identifier for an Entity
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(Publication.class_name,
                                                 
                                                 id=id,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # Evidence methods
    # --
    def fetch_Evidence(self, id_value: str) -> Evidence:
        """
        Retrieves an instance of `Evidence` via a primary key

        :param id_value:
        :return: Evidence with matching ID
        """
        q = FetchById(id=id_value, target_class=Evidence.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_Evidence(self,
             contributor: Union[str, MatchExpression] = None,
             date: Union[str, MatchExpression] = None,
             evidence_type: Union[str, MatchExpression] = None,
             reference: Union[str, MatchExpression] = None,
             with_object: Union[str, MatchExpression] = None,
             id: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[Evidence]:
        """
        Queries for instances of `Evidence`

        :param contributor: connects an assertion to the individual that made a contribution to it
        :param date: connects anything to the date
        :param evidence_type: Connectes a piece of evidence to the evidence_type from ECO
        :param reference: A publication or other reference that supports a piece of evidence
        :param with_object: An object that supports a piece of evidence
        :param id: A unique identifier for an Entity
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(Evidence.class_name,
                                                 
                                                 contributor=contributor,
                                                 
                                                 date=date,
                                                 
                                                 evidence_type=evidence_type,
                                                 
                                                 reference=reference,
                                                 
                                                 with_object=with_object,
                                                 
                                                 id=id,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # DomainEntityMixin methods
    # --
    def fetch_DomainEntityMixin(self, id_value: str) -> DomainEntityMixin:
        """
        Retrieves an instance of `DomainEntityMixin` via a primary key

        :param id_value:
        :return: DomainEntityMixin with matching ID
        """
        q = FetchById(id=id_value, target_class=DomainEntityMixin.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_DomainEntityMixin(self,
             id: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[DomainEntityMixin]:
        """
        Queries for instances of `DomainEntityMixin`

        :param id: A unique identifier for an Entity
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(DomainEntityMixin.class_name,
                                                 
                                                 id=id,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # ActivityOrProcess methods
    # --
    def fetch_ActivityOrProcess(self, id_value: str) -> ActivityOrProcess:
        """
        Retrieves an instance of `ActivityOrProcess` via a primary key

        :param id_value:
        :return: ActivityOrProcess with matching ID
        """
        q = FetchById(id=id_value, target_class=ActivityOrProcess.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_ActivityOrProcess(self,
             id: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[ActivityOrProcess]:
        """
        Queries for instances of `ActivityOrProcess`

        :param id: A unique identifier for an Entity
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(ActivityOrProcess.class_name,
                                                 
                                                 id=id,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # ProcessOrPhase methods
    # --
    def fetch_ProcessOrPhase(self, id_value: str) -> ProcessOrPhase:
        """
        Retrieves an instance of `ProcessOrPhase` via a primary key

        :param id_value:
        :return: ProcessOrPhase with matching ID
        """
        q = FetchById(id=id_value, target_class=ProcessOrPhase.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_ProcessOrPhase(self,
             id: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[ProcessOrPhase]:
        """
        Queries for instances of `ProcessOrPhase`

        :param id: A unique identifier for an Entity
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(ProcessOrPhase.class_name,
                                                 
                                                 id=id,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # Continuant methods
    # --
    def fetch_Continuant(self, id_value: str) -> Continuant:
        """
        Retrieves an instance of `Continuant` via a primary key

        :param id_value:
        :return: Continuant with matching ID
        """
        q = FetchById(id=id_value, target_class=Continuant.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_Continuant(self,
             id: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[Continuant]:
        """
        Queries for instances of `Continuant`

        :param id: A unique identifier for an Entity
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(Continuant.class_name,
                                                 
                                                 id=id,
                                                 
                                                 _extra=_extra)
        return results
    

