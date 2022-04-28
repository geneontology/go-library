
from sqlalchemy import Column, Index, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import *
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy

Base = declarative_base()
metadata = Base.metadata


class Entity(Base):
    """
    Abstract base class for any biological Entity or ActivityOrProcess in a GO-CAM model
    """
    __tablename__ = 'Entity'
    
    id = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"Entity(id={self.id},)"
        
    
        
    


class Association(Base):
    """
    An association between a DomainEntity (e.g. a MolecularActivity) and another DomainEntity (e.g. another MolecularActivity) with evidence and provenance attached
    """
    __tablename__ = 'Association'
    
    id = Column(Integer(), primary_key=True, autoincrement=True )
    subject = Column(Text(), ForeignKey('DomainEntity.id'))
    predicate = Column(Text())
    object = Column(Text(), ForeignKey('Entity.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='Association', source_slot='has_evidence', mapping_type=None, target_class='Evidence', target_slot='Association_id', join_class=None, uses_join_table=None, multivalued=False)
    has_evidence = relationship( "Evidence", foreign_keys="[Evidence.Association_id]")
    
    
    def __repr__(self):
        return f"Association(id={self.id},subject={self.subject},predicate={self.predicate},object={self.object},)"
        
    
        
    


class CausalAssociationToActivity(Base):
    """
    
    """
    __tablename__ = 'CausalAssociationToActivity'
    
    id = Column(Integer(), primary_key=True, autoincrement=True )
    
    
    def __repr__(self):
        return f"CausalAssociationToActivity(id={self.id},)"
        
    
        
    


class CausalAssociationToProcess(Base):
    """
    
    """
    __tablename__ = 'CausalAssociationToProcess'
    
    id = Column(Integer(), primary_key=True, autoincrement=True )
    
    
    def __repr__(self):
        return f"CausalAssociationToProcess(id={self.id},)"
        
    
        
    


class OntologyClass(Base):
    """
    
    """
    __tablename__ = 'OntologyClass'
    
    id = Column(Text(), primary_key=True)
    name = Column(Text())
    category = Column(Text())
    model_id = Column(Text(), ForeignKey('model.id'))
    
    
    def __repr__(self):
        return f"OntologyClass(id={self.id},name={self.name},category={self.category},model_id={self.model_id},)"
        
    
        
    


class DomainEntityMixin(Base):
    """
    Grouping for mixins that apply to GO-CAM entities. These mixins allow us to group together entities that are alike in some fashion
    """
    __tablename__ = 'DomainEntityMixin'
    
    id = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"DomainEntityMixin(id={self.id},)"
        
    
        
    


class ModelContributor(Base):
    """
    
    """
    __tablename__ = 'model_contributor'
    
    model_id = Column(Text(), ForeignKey('model.id'), primary_key=True)
    contributor = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"model_contributor(model_id={self.model_id},contributor={self.contributor},)"
        
    
        
    


class DomainEntityTypeInferences(Base):
    """
    
    """
    __tablename__ = 'DomainEntity_type_inferences'
    
    DomainEntity_id = Column(Text(), ForeignKey('DomainEntity.id'), primary_key=True)
    type_inferences = Column(Text(), ForeignKey('OntologyClass.id'), primary_key=True)
    
    
    def __repr__(self):
        return f"DomainEntity_type_inferences(DomainEntity_id={self.DomainEntity_id},type_inferences={self.type_inferences},)"
        
    
        
    


class MolecularActivityTypeInferences(Base):
    """
    
    """
    __tablename__ = 'MolecularActivity_type_inferences'
    
    MolecularActivity_id = Column(Text(), ForeignKey('MolecularActivity.id'), primary_key=True)
    type_inferences = Column(Text(), ForeignKey('OntologyClass.id'), primary_key=True)
    
    
    def __repr__(self):
        return f"MolecularActivity_type_inferences(MolecularActivity_id={self.MolecularActivity_id},type_inferences={self.type_inferences},)"
        
    
        
    


class BiologicalProcessTypeInferences(Base):
    """
    
    """
    __tablename__ = 'BiologicalProcess_type_inferences'
    
    BiologicalProcess_id = Column(Text(), ForeignKey('BiologicalProcess.id'), primary_key=True)
    type_inferences = Column(Text(), ForeignKey('OntologyClass.id'), primary_key=True)
    
    
    def __repr__(self):
        return f"BiologicalProcess_type_inferences(BiologicalProcess_id={self.BiologicalProcess_id},type_inferences={self.type_inferences},)"
        
    
        
    


class AnatomicalEntityTypeInferences(Base):
    """
    
    """
    __tablename__ = 'AnatomicalEntity_type_inferences'
    
    AnatomicalEntity_id = Column(Text(), ForeignKey('AnatomicalEntity.id'), primary_key=True)
    type_inferences = Column(Text(), ForeignKey('OntologyClass.id'), primary_key=True)
    
    
    def __repr__(self):
        return f"AnatomicalEntity_type_inferences(AnatomicalEntity_id={self.AnatomicalEntity_id},type_inferences={self.type_inferences},)"
        
    
        
    


class ChemicalEntityTypeInferences(Base):
    """
    
    """
    __tablename__ = 'ChemicalEntity_type_inferences'
    
    ChemicalEntity_id = Column(Text(), ForeignKey('ChemicalEntity.id'), primary_key=True)
    type_inferences = Column(Text(), ForeignKey('OntologyClass.id'), primary_key=True)
    
    
    def __repr__(self):
        return f"ChemicalEntity_type_inferences(ChemicalEntity_id={self.ChemicalEntity_id},type_inferences={self.type_inferences},)"
        
    
        
    


class InformationBiomacromoleculeTypeInferences(Base):
    """
    
    """
    __tablename__ = 'InformationBiomacromolecule_type_inferences'
    
    InformationBiomacromolecule_id = Column(Text(), ForeignKey('InformationBiomacromolecule.id'), primary_key=True)
    type_inferences = Column(Text(), ForeignKey('OntologyClass.id'), primary_key=True)
    
    
    def __repr__(self):
        return f"InformationBiomacromolecule_type_inferences(InformationBiomacromolecule_id={self.InformationBiomacromolecule_id},type_inferences={self.type_inferences},)"
        
    
        
    


class EvidenceContributor(Base):
    """
    
    """
    __tablename__ = 'Evidence_contributor'
    
    Evidence_id = Column(Text(), ForeignKey('Evidence.id'), primary_key=True)
    contributor = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"Evidence_contributor(Evidence_id={self.Evidence_id},contributor={self.contributor},)"
        
    
        
    


class EvidenceReference(Base):
    """
    
    """
    __tablename__ = 'Evidence_reference'
    
    Evidence_id = Column(Text(), ForeignKey('Evidence.id'), primary_key=True)
    reference = Column(Text(), ForeignKey('Publication.id'), primary_key=True)
    
    
    def __repr__(self):
        return f"Evidence_reference(Evidence_id={self.Evidence_id},reference={self.reference},)"
        
    
        
    


class EvidenceWithObject(Base):
    """
    
    """
    __tablename__ = 'Evidence_with_object'
    
    Evidence_id = Column(Text(), ForeignKey('Evidence.id'), primary_key=True)
    with_object = Column(Text(), ForeignKey('Entity.id'), primary_key=True)
    
    
    def __repr__(self):
        return f"Evidence_with_object(Evidence_id={self.Evidence_id},with_object={self.with_object},)"
        
    
        
    


class Model(Entity):
    """
    A collection of GO-CAM entities and associated metadata. A model combines multiple simple GO annotations into an integrated, semantically precise and computable model of biological function.
    """
    __tablename__ = 'model'
    
    id = Column(Text(), primary_key=True)
    title = Column(Text())
    date = Column(Text())
    state = Column(Enum('production', 'development', name='ModelStateEnum'))
    provided_by = Column(Text())
    
    
    contributor_rel = relationship( "ModelContributor" )
    contributor = association_proxy("contributor_rel", "contributor",
                                  creator=lambda x_: ModelContributor(contributor=x_))
    
    
    # One-To-Many: OneToAnyMapping(source_class='model', source_slot='molecular_activity_set', mapping_type=None, target_class='MolecularActivity', target_slot='model_id', join_class=None, uses_join_table=None, multivalued=False)
    molecular_activity_set = relationship( "MolecularActivity", foreign_keys="[MolecularActivity.model_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='model', source_slot='biological_process_set', mapping_type=None, target_class='BiologicalProcess', target_slot='model_id', join_class=None, uses_join_table=None, multivalued=False)
    biological_process_set = relationship( "BiologicalProcess", foreign_keys="[BiologicalProcess.model_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='model', source_slot='information_biomacromolecule_set', mapping_type=None, target_class='InformationBiomacromolecule', target_slot='model_id', join_class=None, uses_join_table=None, multivalued=False)
    information_biomacromolecule_set = relationship( "InformationBiomacromolecule", foreign_keys="[InformationBiomacromolecule.model_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='model', source_slot='chemical_entity_set', mapping_type=None, target_class='ChemicalEntity', target_slot='model_id', join_class=None, uses_join_table=None, multivalued=False)
    chemical_entity_set = relationship( "ChemicalEntity", foreign_keys="[ChemicalEntity.model_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='model', source_slot='ontology_class_set', mapping_type=None, target_class='OntologyClass', target_slot='model_id', join_class=None, uses_join_table=None, multivalued=False)
    ontology_class_set = relationship( "OntologyClass", foreign_keys="[OntologyClass.model_id]")
    
    
    def __repr__(self):
        return f"model(id={self.id},title={self.title},date={self.date},state={self.state},provided_by={self.provided_by},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class DomainEntity(Entity):
    """
    Abstract Entity for representing any part_of a GO-CAM model
    """
    __tablename__ = 'DomainEntity'
    
    id = Column(Text(), primary_key=True)
    type = Column(Text(), ForeignKey('OntologyClass.id'))
    
    
    # ManyToMany
    type_inferences = relationship( "OntologyClass", secondary="DomainEntity_type_inferences")
    
    
    def __repr__(self):
        return f"DomainEntity(id={self.id},type={self.type},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class OccursInAssociation(Association):
    """
    An association owned by a MA or BP that connect to an AE object in which the activity/process is carried out
    """
    __tablename__ = 'OccursInAssociation'
    
    id = Column(Integer(), primary_key=True, autoincrement=True )
    subject = Column(Text(), ForeignKey('DomainEntity.id'))
    predicate = Column(Text())
    object = Column(Text(), ForeignKey('AnatomicalEntity.id'))
    MolecularActivity_id = Column(Text(), ForeignKey('MolecularActivity.id'))
    BiologicalProcess_id = Column(Text(), ForeignKey('BiologicalProcess.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='OccursInAssociation', source_slot='has_evidence', mapping_type=None, target_class='Evidence', target_slot='OccursInAssociation_id', join_class=None, uses_join_table=None, multivalued=False)
    has_evidence = relationship( "Evidence", foreign_keys="[Evidence.OccursInAssociation_id]")
    
    
    def __repr__(self):
        return f"OccursInAssociation(id={self.id},subject={self.subject},predicate={self.predicate},object={self.object},MolecularActivity_id={self.MolecularActivity_id},BiologicalProcess_id={self.BiologicalProcess_id},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class CausalAssociation(Association):
    """
    An association owned by an upstream MA or BP that connects to a downstream MA or BP. The nature of the causal relationship is indicated with the predicate.
    """
    __tablename__ = 'CausalAssociation'
    
    id = Column(Integer(), primary_key=True, autoincrement=True )
    subject = Column(Text(), ForeignKey('DomainEntity.id'))
    predicate = Column(Text())
    object = Column(Text(), ForeignKey('ActivityOrProcess.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='CausalAssociation', source_slot='has_evidence', mapping_type=None, target_class='Evidence', target_slot='CausalAssociation_id', join_class=None, uses_join_table=None, multivalued=False)
    has_evidence = relationship( "Evidence", foreign_keys="[Evidence.CausalAssociation_id]")
    
    
    def __repr__(self):
        return f"CausalAssociation(id={self.id},subject={self.subject},predicate={self.predicate},object={self.object},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class HasPartAssociation(Association):
    """
    General grouping for associations that Link an Entity to its parts by a HasPartAssociation
    """
    __tablename__ = 'HasPartAssociation'
    
    id = Column(Integer(), primary_key=True, autoincrement=True )
    subject = Column(Text(), ForeignKey('DomainEntity.id'))
    predicate = Column(Text())
    object = Column(Text(), ForeignKey('Entity.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='HasPartAssociation', source_slot='has_evidence', mapping_type=None, target_class='Evidence', target_slot='HasPartAssociation_id', join_class=None, uses_join_table=None, multivalued=False)
    has_evidence = relationship( "Evidence", foreign_keys="[Evidence.HasPartAssociation_id]")
    
    
    def __repr__(self):
        return f"HasPartAssociation(id={self.id},subject={self.subject},predicate={self.predicate},object={self.object},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class PartOfAssociation(Association):
    """
    General grouping for associations that Link an Entity to its wholes by a PartOfAssociation
    """
    __tablename__ = 'PartOfAssociation'
    
    id = Column(Integer(), primary_key=True, autoincrement=True )
    subject = Column(Text(), ForeignKey('DomainEntity.id'))
    predicate = Column(Text())
    object = Column(Text(), ForeignKey('Entity.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='PartOfAssociation', source_slot='has_evidence', mapping_type=None, target_class='Evidence', target_slot='PartOfAssociation_id', join_class=None, uses_join_table=None, multivalued=False)
    has_evidence = relationship( "Evidence", foreign_keys="[Evidence.PartOfAssociation_id]")
    
    
    def __repr__(self):
        return f"PartOfAssociation(id={self.id},subject={self.subject},predicate={self.predicate},object={self.object},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class EnabledByAssociation(Association):
    """
    Connects an MA to the InformationBiomacromolecule that executes the activity
    """
    __tablename__ = 'EnabledByAssociation'
    
    id = Column(Integer(), primary_key=True, autoincrement=True )
    subject = Column(Text(), ForeignKey('DomainEntity.id'))
    predicate = Column(Text())
    object = Column(Text(), ForeignKey('InformationBiomacromolecule.id'))
    MolecularActivity_id = Column(Text(), ForeignKey('MolecularActivity.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='EnabledByAssociation', source_slot='has_evidence', mapping_type=None, target_class='Evidence', target_slot='EnabledByAssociation_id', join_class=None, uses_join_table=None, multivalued=False)
    has_evidence = relationship( "Evidence", foreign_keys="[Evidence.EnabledByAssociation_id]")
    
    
    def __repr__(self):
        return f"EnabledByAssociation(id={self.id},subject={self.subject},predicate={self.predicate},object={self.object},MolecularActivity_id={self.MolecularActivity_id},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class HappensDuringAssociation(Association):
    """
    Connects an MF to a ProcessOrPhase in which the process occurs
    """
    __tablename__ = 'HappensDuringAssociation'
    
    id = Column(Integer(), primary_key=True, autoincrement=True )
    subject = Column(Text(), ForeignKey('DomainEntity.id'))
    predicate = Column(Text())
    object = Column(Text(), ForeignKey('ActivityOrProcess.id'))
    MolecularActivity_id = Column(Text(), ForeignKey('MolecularActivity.id'))
    BiologicalProcess_id = Column(Text(), ForeignKey('BiologicalProcess.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='HappensDuringAssociation', source_slot='has_evidence', mapping_type=None, target_class='Evidence', target_slot='HappensDuringAssociation_id', join_class=None, uses_join_table=None, multivalued=False)
    has_evidence = relationship( "Evidence", foreign_keys="[Evidence.HappensDuringAssociation_id]")
    
    
    def __repr__(self):
        return f"HappensDuringAssociation(id={self.id},subject={self.subject},predicate={self.predicate},object={self.object},MolecularActivity_id={self.MolecularActivity_id},BiologicalProcess_id={self.BiologicalProcess_id},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class HasInputAssociation(Association):
    """
    Connects an MF or BP to its input Entity, which may be a ChemicalEntity, an InformationBiomacromolecule, or a larger structure
    """
    __tablename__ = 'HasInputAssociation'
    
    id = Column(Integer(), primary_key=True, autoincrement=True )
    subject = Column(Text(), ForeignKey('DomainEntity.id'))
    predicate = Column(Text())
    object = Column(Text(), ForeignKey('Continuant.id'))
    MolecularActivity_id = Column(Text(), ForeignKey('MolecularActivity.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='HasInputAssociation', source_slot='has_evidence', mapping_type=None, target_class='Evidence', target_slot='HasInputAssociation_id', join_class=None, uses_join_table=None, multivalued=False)
    has_evidence = relationship( "Evidence", foreign_keys="[Evidence.HasInputAssociation_id]")
    
    
    def __repr__(self):
        return f"HasInputAssociation(id={self.id},subject={self.subject},predicate={self.predicate},object={self.object},MolecularActivity_id={self.MolecularActivity_id},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class InformationEntity(Entity):
    """
    
    """
    __tablename__ = 'InformationEntity'
    
    id = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"InformationEntity(id={self.id},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class ActivityOrProcess(DomainEntityMixin):
    """
    
    """
    __tablename__ = 'ActivityOrProcess'
    
    id = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"ActivityOrProcess(id={self.id},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class ProcessOrPhase(DomainEntityMixin):
    """
    
    """
    __tablename__ = 'ProcessOrPhase'
    
    id = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"ProcessOrPhase(id={self.id},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class Continuant(DomainEntityMixin):
    """
    
    """
    __tablename__ = 'Continuant'
    
    id = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"Continuant(id={self.id},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class MolecularActivity(DomainEntity):
    """
    An instance of a GO molecular function
    """
    __tablename__ = 'MolecularActivity'
    
    id = Column(Text(), primary_key=True)
    type = Column(Text(), ForeignKey('OntologyClass.id'))
    model_id = Column(Text(), ForeignKey('model.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='MolecularActivity', source_slot='has_activity_causal_associations', mapping_type=None, target_class='ActivityToActivityCausalAssociation', target_slot='MolecularActivity_id', join_class=None, uses_join_table=None, multivalued=False)
    has_activity_causal_associations = relationship( "ActivityToActivityCausalAssociation", foreign_keys="[ActivityToActivityCausalAssociation.MolecularActivity_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='MolecularActivity', source_slot='has_process_causal_associations', mapping_type=None, target_class='ActivityToProcessCausalAssociation', target_slot='MolecularActivity_id', join_class=None, uses_join_table=None, multivalued=False)
    has_process_causal_associations = relationship( "ActivityToProcessCausalAssociation", foreign_keys="[ActivityToProcessCausalAssociation.MolecularActivity_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='MolecularActivity', source_slot='happens_during', mapping_type=None, target_class='HappensDuringAssociation', target_slot='MolecularActivity_id', join_class=None, uses_join_table=None, multivalued=False)
    happens_during = relationship( "HappensDuringAssociation", foreign_keys="[HappensDuringAssociation.MolecularActivity_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='MolecularActivity', source_slot='part_of', mapping_type=None, target_class='ProcessPartOfAssociation', target_slot='MolecularActivity_id', join_class=None, uses_join_table=None, multivalued=False)
    part_of = relationship( "ProcessPartOfAssociation", foreign_keys="[ProcessPartOfAssociation.MolecularActivity_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='MolecularActivity', source_slot='enabled_by', mapping_type=None, target_class='EnabledByAssociation', target_slot='MolecularActivity_id', join_class=None, uses_join_table=None, multivalued=False)
    enabled_by = relationship( "EnabledByAssociation", foreign_keys="[EnabledByAssociation.MolecularActivity_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='MolecularActivity', source_slot='has_input', mapping_type=None, target_class='HasInputAssociation', target_slot='MolecularActivity_id', join_class=None, uses_join_table=None, multivalued=False)
    has_input = relationship( "HasInputAssociation", foreign_keys="[HasInputAssociation.MolecularActivity_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='MolecularActivity', source_slot='occurs_in', mapping_type=None, target_class='OccursInAssociation', target_slot='MolecularActivity_id', join_class=None, uses_join_table=None, multivalued=False)
    occurs_in = relationship( "OccursInAssociation", foreign_keys="[OccursInAssociation.MolecularActivity_id]")
    
    
    # ManyToMany
    type_inferences = relationship( "OntologyClass", secondary="MolecularActivity_type_inferences")
    
    
    def __repr__(self):
        return f"MolecularActivity(id={self.id},type={self.type},model_id={self.model_id},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class BiologicalProcess(DomainEntity):
    """
    An instance of a GO BiologicalProcess
    """
    __tablename__ = 'BiologicalProcess'
    
    id = Column(Text(), primary_key=True)
    type = Column(Text(), ForeignKey('OntologyClass.id'))
    model_id = Column(Text(), ForeignKey('model.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='BiologicalProcess', source_slot='occurs_in', mapping_type=None, target_class='OccursInAssociation', target_slot='BiologicalProcess_id', join_class=None, uses_join_table=None, multivalued=False)
    occurs_in = relationship( "OccursInAssociation", foreign_keys="[OccursInAssociation.BiologicalProcess_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='BiologicalProcess', source_slot='has_activity_causal_associations', mapping_type=None, target_class='ProcessToActivityCausalAssociation', target_slot='BiologicalProcess_id', join_class=None, uses_join_table=None, multivalued=False)
    has_activity_causal_associations = relationship( "ProcessToActivityCausalAssociation", foreign_keys="[ProcessToActivityCausalAssociation.BiologicalProcess_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='BiologicalProcess', source_slot='has_process_causal_associations', mapping_type=None, target_class='ProcessToProcessCausalAssociation', target_slot='BiologicalProcess_id', join_class=None, uses_join_table=None, multivalued=False)
    has_process_causal_associations = relationship( "ProcessToProcessCausalAssociation", foreign_keys="[ProcessToProcessCausalAssociation.BiologicalProcess_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='BiologicalProcess', source_slot='happens_during', mapping_type=None, target_class='HappensDuringAssociation', target_slot='BiologicalProcess_id', join_class=None, uses_join_table=None, multivalued=False)
    happens_during = relationship( "HappensDuringAssociation", foreign_keys="[HappensDuringAssociation.BiologicalProcess_id]")
    
    
    # ManyToMany
    type_inferences = relationship( "OntologyClass", secondary="BiologicalProcess_type_inferences")
    
    
    def __repr__(self):
        return f"BiologicalProcess(id={self.id},type={self.type},model_id={self.model_id},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class AnatomicalEntity(DomainEntity):
    """
    An instance of a GO cellular AnatomicalEntity, a cell type, or gross anatomical structure
    """
    __tablename__ = 'AnatomicalEntity'
    
    id = Column(Text(), primary_key=True)
    type = Column(Text(), ForeignKey('OntologyClass.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='AnatomicalEntity', source_slot='part_of', mapping_type=None, target_class='AnatomicalPartOfAssociation', target_slot='AnatomicalEntity_id', join_class=None, uses_join_table=None, multivalued=False)
    part_of = relationship( "AnatomicalPartOfAssociation", foreign_keys="[AnatomicalPartOfAssociation.AnatomicalEntity_id]")
    
    
    # ManyToMany
    type_inferences = relationship( "OntologyClass", secondary="AnatomicalEntity_type_inferences")
    
    
    def __repr__(self):
        return f"AnatomicalEntity(id={self.id},type={self.type},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class ChemicalEntity(DomainEntity):
    """
    An instance of a ChemicalEntity, as defined in CHEBI, including macromolecules defined in NEO
    """
    __tablename__ = 'ChemicalEntity'
    
    id = Column(Text(), primary_key=True)
    type = Column(Text(), ForeignKey('OntologyClass.id'))
    model_id = Column(Text(), ForeignKey('model.id'))
    
    
    # ManyToMany
    type_inferences = relationship( "OntologyClass", secondary="ChemicalEntity_type_inferences")
    
    
    def __repr__(self):
        return f"ChemicalEntity(id={self.id},type={self.type},model_id={self.model_id},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class ActivityToActivityCausalAssociation(CausalAssociation):
    """
    A CausalAssociation between two molecular activities
    """
    __tablename__ = 'ActivityToActivityCausalAssociation'
    
    id = Column(Integer(), primary_key=True, autoincrement=True )
    subject = Column(Text(), ForeignKey('MolecularActivity.id'))
    predicate = Column(Text())
    object = Column(Text(), ForeignKey('MolecularActivity.id'))
    MolecularActivity_id = Column(Text(), ForeignKey('MolecularActivity.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='ActivityToActivityCausalAssociation', source_slot='has_evidence', mapping_type=None, target_class='Evidence', target_slot='ActivityToActivityCausalAssociation_id', join_class=None, uses_join_table=None, multivalued=False)
    has_evidence = relationship( "Evidence", foreign_keys="[Evidence.ActivityToActivityCausalAssociation_id]")
    
    
    def __repr__(self):
        return f"ActivityToActivityCausalAssociation(id={self.id},subject={self.subject},predicate={self.predicate},object={self.object},MolecularActivity_id={self.MolecularActivity_id},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class ProcessToProcessCausalAssociation(CausalAssociation):
    """
    A CausalAssociation between two BiologicalProcesses
    """
    __tablename__ = 'ProcessToProcessCausalAssociation'
    
    id = Column(Integer(), primary_key=True, autoincrement=True )
    subject = Column(Text(), ForeignKey('BiologicalProcess.id'))
    predicate = Column(Text())
    object = Column(Text(), ForeignKey('BiologicalProcess.id'))
    BiologicalProcess_id = Column(Text(), ForeignKey('BiologicalProcess.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='ProcessToProcessCausalAssociation', source_slot='has_evidence', mapping_type=None, target_class='Evidence', target_slot='ProcessToProcessCausalAssociation_id', join_class=None, uses_join_table=None, multivalued=False)
    has_evidence = relationship( "Evidence", foreign_keys="[Evidence.ProcessToProcessCausalAssociation_id]")
    
    
    def __repr__(self):
        return f"ProcessToProcessCausalAssociation(id={self.id},subject={self.subject},predicate={self.predicate},object={self.object},BiologicalProcess_id={self.BiologicalProcess_id},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class ProcessToActivityCausalAssociation(CausalAssociation):
    """
    A CausalAssociation between a BiologicalProcess and a MolecularActivity
    """
    __tablename__ = 'ProcessToActivityCausalAssociation'
    
    id = Column(Integer(), primary_key=True, autoincrement=True )
    subject = Column(Text(), ForeignKey('BiologicalProcess.id'))
    predicate = Column(Text())
    object = Column(Text(), ForeignKey('MolecularActivity.id'))
    BiologicalProcess_id = Column(Text(), ForeignKey('BiologicalProcess.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='ProcessToActivityCausalAssociation', source_slot='has_evidence', mapping_type=None, target_class='Evidence', target_slot='ProcessToActivityCausalAssociation_id', join_class=None, uses_join_table=None, multivalued=False)
    has_evidence = relationship( "Evidence", foreign_keys="[Evidence.ProcessToActivityCausalAssociation_id]")
    
    
    def __repr__(self):
        return f"ProcessToActivityCausalAssociation(id={self.id},subject={self.subject},predicate={self.predicate},object={self.object},BiologicalProcess_id={self.BiologicalProcess_id},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class ActivityToProcessCausalAssociation(CausalAssociation):
    """
    A CausalAssociation between a MolecularActivity and a BiologicalProcess
    """
    __tablename__ = 'ActivityToProcessCausalAssociation'
    
    id = Column(Integer(), primary_key=True, autoincrement=True )
    subject = Column(Text(), ForeignKey('MolecularActivity.id'))
    predicate = Column(Text())
    object = Column(Text(), ForeignKey('BiologicalProcess.id'))
    MolecularActivity_id = Column(Text(), ForeignKey('MolecularActivity.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='ActivityToProcessCausalAssociation', source_slot='has_evidence', mapping_type=None, target_class='Evidence', target_slot='ActivityToProcessCausalAssociation_id', join_class=None, uses_join_table=None, multivalued=False)
    has_evidence = relationship( "Evidence", foreign_keys="[Evidence.ActivityToProcessCausalAssociation_id]")
    
    
    def __repr__(self):
        return f"ActivityToProcessCausalAssociation(id={self.id},subject={self.subject},predicate={self.predicate},object={self.object},MolecularActivity_id={self.MolecularActivity_id},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class MacromoleculeHasPartAssociation(HasPartAssociation):
    """
    Connects a macromolecule (such as a protein complex) to its parts (gene products or chemical entities)
    """
    __tablename__ = 'MacromoleculeHasPartAssociation'
    
    id = Column(Integer(), primary_key=True, autoincrement=True )
    subject = Column(Text(), ForeignKey('DomainEntity.id'))
    predicate = Column(Text())
    object = Column(Text(), ForeignKey('Continuant.id'))
    InformationBiomacromolecule_id = Column(Text(), ForeignKey('InformationBiomacromolecule.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='MacromoleculeHasPartAssociation', source_slot='has_evidence', mapping_type=None, target_class='Evidence', target_slot='MacromoleculeHasPartAssociation_id', join_class=None, uses_join_table=None, multivalued=False)
    has_evidence = relationship( "Evidence", foreign_keys="[Evidence.MacromoleculeHasPartAssociation_id]")
    
    
    def __repr__(self):
        return f"MacromoleculeHasPartAssociation(id={self.id},subject={self.subject},predicate={self.predicate},object={self.object},InformationBiomacromolecule_id={self.InformationBiomacromolecule_id},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class AnatomicalPartOfAssociation(PartOfAssociation):
    """
    Connects an AnatomicalEntity (such as a component, cell, or gross AnatomicalEntity) to its parent parts
    """
    __tablename__ = 'AnatomicalPartOfAssociation'
    
    id = Column(Integer(), primary_key=True, autoincrement=True )
    subject = Column(Text(), ForeignKey('DomainEntity.id'))
    predicate = Column(Text())
    object = Column(Text(), ForeignKey('AnatomicalEntity.id'))
    AnatomicalEntity_id = Column(Text(), ForeignKey('AnatomicalEntity.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='AnatomicalPartOfAssociation', source_slot='has_evidence', mapping_type=None, target_class='Evidence', target_slot='AnatomicalPartOfAssociation_id', join_class=None, uses_join_table=None, multivalued=False)
    has_evidence = relationship( "Evidence", foreign_keys="[Evidence.AnatomicalPartOfAssociation_id]")
    
    
    def __repr__(self):
        return f"AnatomicalPartOfAssociation(id={self.id},subject={self.subject},predicate={self.predicate},object={self.object},AnatomicalEntity_id={self.AnatomicalEntity_id},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class ProcessPartOfAssociation(PartOfAssociation):
    """
    Connects a MA or BP to its parent parts
    """
    __tablename__ = 'ProcessPartOfAssociation'
    
    id = Column(Integer(), primary_key=True, autoincrement=True )
    subject = Column(Text(), ForeignKey('DomainEntity.id'))
    predicate = Column(Text())
    object = Column(Text(), ForeignKey('BiologicalProcess.id'))
    MolecularActivity_id = Column(Text(), ForeignKey('MolecularActivity.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='ProcessPartOfAssociation', source_slot='has_evidence', mapping_type=None, target_class='Evidence', target_slot='ProcessPartOfAssociation_id', join_class=None, uses_join_table=None, multivalued=False)
    has_evidence = relationship( "Evidence", foreign_keys="[Evidence.ProcessPartOfAssociation_id]")
    
    
    def __repr__(self):
        return f"ProcessPartOfAssociation(id={self.id},subject={self.subject},predicate={self.predicate},object={self.object},MolecularActivity_id={self.MolecularActivity_id},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class Publication(InformationEntity):
    """
    A published Entity such as a paper in pubmed
    """
    __tablename__ = 'Publication'
    
    id = Column(Text(), primary_key=True)
    
    
    def __repr__(self):
        return f"Publication(id={self.id},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class Evidence(InformationEntity):
    """
    An instance of a piece of Evidence. Evidence attributes such as type, reference, hang off of here
    """
    __tablename__ = 'Evidence'
    
    date = Column(Text())
    evidence_type = Column(Text(), ForeignKey('OntologyClass.id'))
    id = Column(Text(), primary_key=True)
    Association_id = Column(Text(), ForeignKey('Association.id'))
    OccursInAssociation_id = Column(Text(), ForeignKey('OccursInAssociation.id'))
    CausalAssociation_id = Column(Text(), ForeignKey('CausalAssociation.id'))
    ActivityToActivityCausalAssociation_id = Column(Text(), ForeignKey('ActivityToActivityCausalAssociation.id'))
    ProcessToProcessCausalAssociation_id = Column(Text(), ForeignKey('ProcessToProcessCausalAssociation.id'))
    ProcessToActivityCausalAssociation_id = Column(Text(), ForeignKey('ProcessToActivityCausalAssociation.id'))
    ActivityToProcessCausalAssociation_id = Column(Text(), ForeignKey('ActivityToProcessCausalAssociation.id'))
    HasPartAssociation_id = Column(Text(), ForeignKey('HasPartAssociation.id'))
    MacromoleculeHasPartAssociation_id = Column(Text(), ForeignKey('MacromoleculeHasPartAssociation.id'))
    PartOfAssociation_id = Column(Text(), ForeignKey('PartOfAssociation.id'))
    AnatomicalPartOfAssociation_id = Column(Text(), ForeignKey('AnatomicalPartOfAssociation.id'))
    ProcessPartOfAssociation_id = Column(Text(), ForeignKey('ProcessPartOfAssociation.id'))
    EnabledByAssociation_id = Column(Text(), ForeignKey('EnabledByAssociation.id'))
    HappensDuringAssociation_id = Column(Text(), ForeignKey('HappensDuringAssociation.id'))
    HasInputAssociation_id = Column(Text(), ForeignKey('HasInputAssociation.id'))
    
    
    contributor_rel = relationship( "EvidenceContributor" )
    contributor = association_proxy("contributor_rel", "contributor",
                                  creator=lambda x_: EvidenceContributor(contributor=x_))
    
    
    # ManyToMany
    reference = relationship( "Publication", secondary="Evidence_reference")
    
    
    # ManyToMany
    with_object = relationship( "Entity", secondary="Evidence_with_object")
    
    
    def __repr__(self):
        return f"Evidence(date={self.date},evidence_type={self.evidence_type},id={self.id},Association_id={self.Association_id},OccursInAssociation_id={self.OccursInAssociation_id},CausalAssociation_id={self.CausalAssociation_id},ActivityToActivityCausalAssociation_id={self.ActivityToActivityCausalAssociation_id},ProcessToProcessCausalAssociation_id={self.ProcessToProcessCausalAssociation_id},ProcessToActivityCausalAssociation_id={self.ProcessToActivityCausalAssociation_id},ActivityToProcessCausalAssociation_id={self.ActivityToProcessCausalAssociation_id},HasPartAssociation_id={self.HasPartAssociation_id},MacromoleculeHasPartAssociation_id={self.MacromoleculeHasPartAssociation_id},PartOfAssociation_id={self.PartOfAssociation_id},AnatomicalPartOfAssociation_id={self.AnatomicalPartOfAssociation_id},ProcessPartOfAssociation_id={self.ProcessPartOfAssociation_id},EnabledByAssociation_id={self.EnabledByAssociation_id},HappensDuringAssociation_id={self.HappensDuringAssociation_id},HasInputAssociation_id={self.HasInputAssociation_id},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class InformationBiomacromolecule(ChemicalEntity):
    """
    This class groups gene, gene product (protein on ncRNA), or a macromolecular complex that is capable of carrying out a MolecularActivity
    """
    __tablename__ = 'InformationBiomacromolecule'
    
    id = Column(Text(), primary_key=True)
    type = Column(Text(), ForeignKey('OntologyClass.id'))
    model_id = Column(Text(), ForeignKey('model.id'))
    
    
    # One-To-Many: OneToAnyMapping(source_class='InformationBiomacromolecule', source_slot='has_part', mapping_type=None, target_class='MacromoleculeHasPartAssociation', target_slot='InformationBiomacromolecule_id', join_class=None, uses_join_table=None, multivalued=False)
    has_part = relationship( "MacromoleculeHasPartAssociation", foreign_keys="[MacromoleculeHasPartAssociation.InformationBiomacromolecule_id]")
    
    
    # ManyToMany
    type_inferences = relationship( "OntologyClass", secondary="InformationBiomacromolecule_type_inferences")
    
    
    def __repr__(self):
        return f"InformationBiomacromolecule(id={self.id},type={self.type},model_id={self.model_id},)"
        
    
        
    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


