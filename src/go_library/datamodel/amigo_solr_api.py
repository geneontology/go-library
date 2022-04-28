
import logging
from dataclasses import dataclass
from linkml_dataops.query.queryengine import QueryEngine
from linkml_dataops.query.query_model import FetchQuery, Constraint, MatchConstraint, OrConstraint, AbstractQuery,     FetchById
from linkml_dataops.query.queryengine import MatchExpression

from .amigo_solr import *

@dataclass
class AmigoSolrAPI:

    # attributes
    query_engine: QueryEngine = None

    
    # --
    # Annotation methods
    # --
    def fetch_Annotation(self, id_value: str) -> Annotation:
        """
        Retrieves an instance of `Annotation` via a primary key

        :param id_value:
        :return: Annotation with matching ID
        """
        q = FetchById(id=id_value, target_class=Annotation.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_Annotation(self,
             document_category: Union[str, MatchExpression] = None,
             id: Union[str, MatchExpression] = None,
             source: Union[str, MatchExpression] = None,
             type: Union[str, MatchExpression] = None,
             date: Union[str, MatchExpression] = None,
             assigned_by: Union[str, MatchExpression] = None,
             is_redundant_for: Union[str, MatchExpression] = None,
             taxon: Union[str, MatchExpression] = None,
             taxon_label: Union[str, MatchExpression] = None,
             taxon_label_searchable: Union[str, MatchExpression] = None,
             taxon_closure: Union[str, MatchExpression] = None,
             taxon_closure_label: Union[str, MatchExpression] = None,
             taxon_closure_label_searchable: Union[str, MatchExpression] = None,
             taxon_subset_closure: Union[str, MatchExpression] = None,
             taxon_subset_closure_label: Union[str, MatchExpression] = None,
             taxon_subset_closure_label_searchable: Union[str, MatchExpression] = None,
             secondary_taxon: Union[str, MatchExpression] = None,
             secondary_taxon_label: Union[str, MatchExpression] = None,
             secondary_taxon_label_searchable: Union[str, MatchExpression] = None,
             secondary_taxon_closure: Union[str, MatchExpression] = None,
             secondary_taxon_closure_label: Union[str, MatchExpression] = None,
             secondary_taxon_closure_label_searchable: Union[str, MatchExpression] = None,
             isa_partof_closure: Union[str, MatchExpression] = None,
             isa_partof_closure_label: Union[str, MatchExpression] = None,
             isa_partof_closure_label_searchable: Union[str, MatchExpression] = None,
             regulates_closure: Union[str, MatchExpression] = None,
             regulates_closure_label: Union[str, MatchExpression] = None,
             regulates_closure_label_searchable: Union[str, MatchExpression] = None,
             has_participant_closure: Union[str, MatchExpression] = None,
             has_participant_closure_label: Union[str, MatchExpression] = None,
             has_participant_closure_label_searchable: Union[str, MatchExpression] = None,
             synonym: Union[str, MatchExpression] = None,
             synonym_searchable: Union[str, MatchExpression] = None,
             bioentity: Union[str, MatchExpression] = None,
             bioentity_label: Union[str, MatchExpression] = None,
             bioentity_label_searchable: Union[str, MatchExpression] = None,
             bioentity_name: Union[str, MatchExpression] = None,
             bioentity_name_searchable: Union[str, MatchExpression] = None,
             bioentity_internal_id: Union[str, MatchExpression] = None,
             qualifier: Union[str, MatchExpression] = None,
             annotation_class: Union[str, MatchExpression] = None,
             annotation_class_label: Union[str, MatchExpression] = None,
             annotation_class_label_searchable: Union[str, MatchExpression] = None,
             aspect: Union[str, MatchExpression] = None,
             bioentity_isoform: Union[str, MatchExpression] = None,
             evidence_type: Union[str, MatchExpression] = None,
             evidence_type_closure: Union[str, MatchExpression] = None,
             evidence_with: Union[str, MatchExpression] = None,
             evidence_with_searchable: Union[str, MatchExpression] = None,
             evidence: Union[str, MatchExpression] = None,
             evidence_label: Union[str, MatchExpression] = None,
             evidence_label_searchable: Union[str, MatchExpression] = None,
             evidence_closure: Union[str, MatchExpression] = None,
             evidence_closure_label: Union[str, MatchExpression] = None,
             evidence_closure_label_searchable: Union[str, MatchExpression] = None,
             evidence_subset_closure: Union[str, MatchExpression] = None,
             evidence_subset_closure_label: Union[str, MatchExpression] = None,
             evidence_subset_closure_label_searchable: Union[str, MatchExpression] = None,
             reference: Union[str, MatchExpression] = None,
             reference_searchable: Union[str, MatchExpression] = None,
             annotation_extension_class: Union[str, MatchExpression] = None,
             annotation_extension_class_label: Union[str, MatchExpression] = None,
             annotation_extension_class_label_searchable: Union[str, MatchExpression] = None,
             annotation_extension_class_closure: Union[str, MatchExpression] = None,
             annotation_extension_class_closure_label: Union[str, MatchExpression] = None,
             annotation_extension_class_closure_label_searchable: Union[str, MatchExpression] = None,
             annotation_extension_json: Union[str, MatchExpression] = None,
             panther_family: Union[str, MatchExpression] = None,
             panther_family_searchable: Union[str, MatchExpression] = None,
             panther_family_label: Union[str, MatchExpression] = None,
             panther_family_label_searchable: Union[str, MatchExpression] = None,
             geospatial_x: Union[str, MatchExpression] = None,
             geospatial_y: Union[str, MatchExpression] = None,
             geospatial_z: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[Annotation]:
        """
        Queries for instances of `Annotation`

        :param document_category: None
        :param id: Term acc/ID.
        :param source: Term namespace. In GO, this is one of: biological_process, molecular_function, cellular_component. In other ontologies it is not guaranteed to be populated. Consider using idspace instead for general queries.
        :param type: Type class.
        :param date: Date of assignment.
        :param assigned_by: Annotations assigned by group.
        :param is_redundant_for: Rational for redundancy of annotation.
        :param taxon: taxon of the entity in enabled_by
        :param taxon_label: label for taxon
        :param taxon_label_searchable: label for taxon
        :param taxon_closure: is_a closure of taxon
        :param taxon_closure_label: labels of is_a closure.
        :param taxon_closure_label_searchable: labels of is_a closure.
        :param taxon_subset_closure: Taxonomic group (direct) and ancestral groups that are within the specified subset (e.g mammalia, eukaryota).
        :param taxon_subset_closure_label: Labels for taxonomic group (direct) and ancestral groups that are within the specified subset.
        :param taxon_subset_closure_label_searchable: Labels for taxonomic group (direct) and ancestral groups that are within the specified subset.
        :param secondary_taxon: Secondary taxon.
        :param secondary_taxon_label: Secondary taxon.
        :param secondary_taxon_label_searchable: Secondary taxon.
        :param secondary_taxon_closure: Secondary taxon closure.
        :param secondary_taxon_closure_label: Secondary taxon closure.
        :param secondary_taxon_closure_label_searchable: Secondary taxon closure.
        :param isa_partof_closure: Ancestral terms (is_a/part_of).
        :param isa_partof_closure_label: Ancestral terms (is_a/part_of).
        :param isa_partof_closure_label_searchable: Ancestral terms (is_a/part_of).
        :param regulates_closure: Ancestral terms (regulates, occurs in, capable_of).
        :param regulates_closure_label: Ancestral terms (regulates, occurs in, capable_of).
        :param regulates_closure_label_searchable: Ancestral terms (regulates, occurs in, capable_of).
        :param has_participant_closure: Closure of ids/accs over has_participant.
        :param has_participant_closure_label: Closure of labels over has_participant.
        :param has_participant_closure_label_searchable: Closure of labels over has_participant.
        :param synonym: Term synonyms.
        :param synonym_searchable: Term synonyms.
        :param bioentity: Gene or gene product identifiers.
        :param bioentity_label: Gene or gene product identifiers.
        :param bioentity_label_searchable: Gene or gene product identifiers.
        :param bioentity_name: The full name of the gene or gene product.
        :param bioentity_name_searchable: The full name of the gene or gene product.
        :param bioentity_internal_id: The bioentity ID used at the database of origin.
        :param qualifier: Annotation qualifier.
        :param annotation_class: Term acc/ID.
        :param annotation_class_label: Common term name.
        :param annotation_class_label_searchable: Common term name.
        :param aspect: Ontology aspect.
        :param bioentity_isoform: Biological isoform.
        :param evidence_type: Evidence type.
        :param evidence_type_closure: All evidence (evidence closure) for this annotation
        :param evidence_with: Evidence with/from.
        :param evidence_with_searchable: Evidence with/from.
        :param evidence: Evidence.
        :param evidence_label: Evidence.
        :param evidence_label_searchable: Evidence.
        :param evidence_closure: All evidence for this annotation.
        :param evidence_closure_label: All evidence for this annotation.
        :param evidence_closure_label_searchable: All evidence for this annotation.
        :param evidence_subset_closure: All evidence for this annotation reduced to a usable subset.
        :param evidence_subset_closure_label: All evidence for this annotation reduced to a usable subset.
        :param evidence_subset_closure_label_searchable: All evidence for this annotation reduced to a usable subset.
        :param reference: Database reference.
        :param reference_searchable: Database reference.
        :param annotation_extension_class: Extension class for the annotation.
        :param annotation_extension_class_label: Extension class for the annotation.
        :param annotation_extension_class_label_searchable: Extension class for the annotation.
        :param annotation_extension_class_closure: Extension class for the annotation.
        :param annotation_extension_class_closure_label: Extension class for the annotation.
        :param annotation_extension_class_closure_label_searchable: Extension class for the annotation.
        :param annotation_extension_json: Extension class for the annotation (JSON).
        :param panther_family: PANTHER family IDs that are associated with this entity.
        :param panther_family_searchable: PANTHER family IDs that are associated with this entity.
        :param panther_family_label: PANTHER families that are associated with this entity.
        :param panther_family_label_searchable: PANTHER families that are associated with this entity.
        :param geospatial_x: Experimental numeric type (X).
        :param geospatial_y: Experimental numeric type (Y).
        :param geospatial_z: Experimental numeric type (Z).
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(Annotation.class_name,
                                                 
                                                 document_category=document_category,
                                                 
                                                 id=id,
                                                 
                                                 source=source,
                                                 
                                                 type=type,
                                                 
                                                 date=date,
                                                 
                                                 assigned_by=assigned_by,
                                                 
                                                 is_redundant_for=is_redundant_for,
                                                 
                                                 taxon=taxon,
                                                 
                                                 taxon_label=taxon_label,
                                                 
                                                 taxon_label_searchable=taxon_label_searchable,
                                                 
                                                 taxon_closure=taxon_closure,
                                                 
                                                 taxon_closure_label=taxon_closure_label,
                                                 
                                                 taxon_closure_label_searchable=taxon_closure_label_searchable,
                                                 
                                                 taxon_subset_closure=taxon_subset_closure,
                                                 
                                                 taxon_subset_closure_label=taxon_subset_closure_label,
                                                 
                                                 taxon_subset_closure_label_searchable=taxon_subset_closure_label_searchable,
                                                 
                                                 secondary_taxon=secondary_taxon,
                                                 
                                                 secondary_taxon_label=secondary_taxon_label,
                                                 
                                                 secondary_taxon_label_searchable=secondary_taxon_label_searchable,
                                                 
                                                 secondary_taxon_closure=secondary_taxon_closure,
                                                 
                                                 secondary_taxon_closure_label=secondary_taxon_closure_label,
                                                 
                                                 secondary_taxon_closure_label_searchable=secondary_taxon_closure_label_searchable,
                                                 
                                                 isa_partof_closure=isa_partof_closure,
                                                 
                                                 isa_partof_closure_label=isa_partof_closure_label,
                                                 
                                                 isa_partof_closure_label_searchable=isa_partof_closure_label_searchable,
                                                 
                                                 regulates_closure=regulates_closure,
                                                 
                                                 regulates_closure_label=regulates_closure_label,
                                                 
                                                 regulates_closure_label_searchable=regulates_closure_label_searchable,
                                                 
                                                 has_participant_closure=has_participant_closure,
                                                 
                                                 has_participant_closure_label=has_participant_closure_label,
                                                 
                                                 has_participant_closure_label_searchable=has_participant_closure_label_searchable,
                                                 
                                                 synonym=synonym,
                                                 
                                                 synonym_searchable=synonym_searchable,
                                                 
                                                 bioentity=bioentity,
                                                 
                                                 bioentity_label=bioentity_label,
                                                 
                                                 bioentity_label_searchable=bioentity_label_searchable,
                                                 
                                                 bioentity_name=bioentity_name,
                                                 
                                                 bioentity_name_searchable=bioentity_name_searchable,
                                                 
                                                 bioentity_internal_id=bioentity_internal_id,
                                                 
                                                 qualifier=qualifier,
                                                 
                                                 annotation_class=annotation_class,
                                                 
                                                 annotation_class_label=annotation_class_label,
                                                 
                                                 annotation_class_label_searchable=annotation_class_label_searchable,
                                                 
                                                 aspect=aspect,
                                                 
                                                 bioentity_isoform=bioentity_isoform,
                                                 
                                                 evidence_type=evidence_type,
                                                 
                                                 evidence_type_closure=evidence_type_closure,
                                                 
                                                 evidence_with=evidence_with,
                                                 
                                                 evidence_with_searchable=evidence_with_searchable,
                                                 
                                                 evidence=evidence,
                                                 
                                                 evidence_label=evidence_label,
                                                 
                                                 evidence_label_searchable=evidence_label_searchable,
                                                 
                                                 evidence_closure=evidence_closure,
                                                 
                                                 evidence_closure_label=evidence_closure_label,
                                                 
                                                 evidence_closure_label_searchable=evidence_closure_label_searchable,
                                                 
                                                 evidence_subset_closure=evidence_subset_closure,
                                                 
                                                 evidence_subset_closure_label=evidence_subset_closure_label,
                                                 
                                                 evidence_subset_closure_label_searchable=evidence_subset_closure_label_searchable,
                                                 
                                                 reference=reference,
                                                 
                                                 reference_searchable=reference_searchable,
                                                 
                                                 annotation_extension_class=annotation_extension_class,
                                                 
                                                 annotation_extension_class_label=annotation_extension_class_label,
                                                 
                                                 annotation_extension_class_label_searchable=annotation_extension_class_label_searchable,
                                                 
                                                 annotation_extension_class_closure=annotation_extension_class_closure,
                                                 
                                                 annotation_extension_class_closure_label=annotation_extension_class_closure_label,
                                                 
                                                 annotation_extension_class_closure_label_searchable=annotation_extension_class_closure_label_searchable,
                                                 
                                                 annotation_extension_json=annotation_extension_json,
                                                 
                                                 panther_family=panther_family,
                                                 
                                                 panther_family_searchable=panther_family_searchable,
                                                 
                                                 panther_family_label=panther_family_label,
                                                 
                                                 panther_family_label_searchable=panther_family_label_searchable,
                                                 
                                                 geospatial_x=geospatial_x,
                                                 
                                                 geospatial_y=geospatial_y,
                                                 
                                                 geospatial_z=geospatial_z,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # AnnotationEvidenceAggregate methods
    # --
    def fetch_AnnotationEvidenceAggregate(self, id_value: str) -> AnnotationEvidenceAggregate:
        """
        Retrieves an instance of `AnnotationEvidenceAggregate` via a primary key

        :param id_value:
        :return: AnnotationEvidenceAggregate with matching ID
        """
        q = FetchById(id=id_value, target_class=AnnotationEvidenceAggregate.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_AnnotationEvidenceAggregate(self,
             document_category: Union[str, MatchExpression] = None,
             id: Union[str, MatchExpression] = None,
             bioentity: Union[str, MatchExpression] = None,
             bioentity_label: Union[str, MatchExpression] = None,
             bioentity_label_searchable: Union[str, MatchExpression] = None,
             annotation_class: Union[str, MatchExpression] = None,
             annotation_class_label: Union[str, MatchExpression] = None,
             annotation_class_label_searchable: Union[str, MatchExpression] = None,
             evidence_type_closure: Union[str, MatchExpression] = None,
             evidence_with: Union[str, MatchExpression] = None,
             taxon: Union[str, MatchExpression] = None,
             taxon_label: Union[str, MatchExpression] = None,
             taxon_label_searchable: Union[str, MatchExpression] = None,
             taxon_closure: Union[str, MatchExpression] = None,
             taxon_closure_label: Union[str, MatchExpression] = None,
             taxon_closure_label_searchable: Union[str, MatchExpression] = None,
             panther_family: Union[str, MatchExpression] = None,
             panther_family_searchable: Union[str, MatchExpression] = None,
             panther_family_label: Union[str, MatchExpression] = None,
             panther_family_label_searchable: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[AnnotationEvidenceAggregate]:
        """
        Queries for instances of `AnnotationEvidenceAggregate`

        :param document_category: None
        :param id: Term acc/ID.
        :param bioentity: Gene or gene product identifiers.
        :param bioentity_label: Gene or gene product identifiers.
        :param bioentity_label_searchable: Gene or gene product identifiers.
        :param annotation_class: Term acc/ID.
        :param annotation_class_label: Common term name.
        :param annotation_class_label_searchable: Common term name.
        :param evidence_type_closure: All evidence (evidence closure) for this annotation
        :param evidence_with: Evidence with/from.
        :param taxon: taxon of the entity in enabled_by
        :param taxon_label: label for taxon
        :param taxon_label_searchable: label for taxon
        :param taxon_closure: is_a closure of taxon
        :param taxon_closure_label: labels of is_a closure.
        :param taxon_closure_label_searchable: labels of is_a closure.
        :param panther_family: PANTHER family IDs that are associated with this entity.
        :param panther_family_searchable: PANTHER family IDs that are associated with this entity.
        :param panther_family_label: PANTHER families that are associated with this entity.
        :param panther_family_label_searchable: PANTHER families that are associated with this entity.
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(AnnotationEvidenceAggregate.class_name,
                                                 
                                                 document_category=document_category,
                                                 
                                                 id=id,
                                                 
                                                 bioentity=bioentity,
                                                 
                                                 bioentity_label=bioentity_label,
                                                 
                                                 bioentity_label_searchable=bioentity_label_searchable,
                                                 
                                                 annotation_class=annotation_class,
                                                 
                                                 annotation_class_label=annotation_class_label,
                                                 
                                                 annotation_class_label_searchable=annotation_class_label_searchable,
                                                 
                                                 evidence_type_closure=evidence_type_closure,
                                                 
                                                 evidence_with=evidence_with,
                                                 
                                                 taxon=taxon,
                                                 
                                                 taxon_label=taxon_label,
                                                 
                                                 taxon_label_searchable=taxon_label_searchable,
                                                 
                                                 taxon_closure=taxon_closure,
                                                 
                                                 taxon_closure_label=taxon_closure_label,
                                                 
                                                 taxon_closure_label_searchable=taxon_closure_label_searchable,
                                                 
                                                 panther_family=panther_family,
                                                 
                                                 panther_family_searchable=panther_family_searchable,
                                                 
                                                 panther_family_label=panther_family_label,
                                                 
                                                 panther_family_label_searchable=panther_family_label_searchable,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # Bioentity methods
    # --
    def fetch_Bioentity(self, id_value: str) -> Bioentity:
        """
        Retrieves an instance of `Bioentity` via a primary key

        :param id_value:
        :return: Bioentity with matching ID
        """
        q = FetchById(id=id_value, target_class=Bioentity.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_Bioentity(self,
             document_category: Union[str, MatchExpression] = None,
             id: Union[str, MatchExpression] = None,
             bioentity: Union[str, MatchExpression] = None,
             bioentity_label: Union[str, MatchExpression] = None,
             bioentity_label_searchable: Union[str, MatchExpression] = None,
             bioentity_name: Union[str, MatchExpression] = None,
             bioentity_name_searchable: Union[str, MatchExpression] = None,
             bioentity_internal_id: Union[str, MatchExpression] = None,
             type: Union[str, MatchExpression] = None,
             taxon: Union[str, MatchExpression] = None,
             taxon_label: Union[str, MatchExpression] = None,
             taxon_label_searchable: Union[str, MatchExpression] = None,
             taxon_closure: Union[str, MatchExpression] = None,
             taxon_closure_label: Union[str, MatchExpression] = None,
             taxon_closure_label_searchable: Union[str, MatchExpression] = None,
             taxon_subset_closure: Union[str, MatchExpression] = None,
             taxon_subset_closure_label: Union[str, MatchExpression] = None,
             taxon_subset_closure_label_searchable: Union[str, MatchExpression] = None,
             isa_partof_closure: Union[str, MatchExpression] = None,
             isa_partof_closure_label: Union[str, MatchExpression] = None,
             isa_partof_closure_label_searchable: Union[str, MatchExpression] = None,
             regulates_closure: Union[str, MatchExpression] = None,
             regulates_closure_label: Union[str, MatchExpression] = None,
             regulates_closure_label_searchable: Union[str, MatchExpression] = None,
             source: Union[str, MatchExpression] = None,
             annotation_class_list: Union[str, MatchExpression] = None,
             annotation_class_list_label: Union[str, MatchExpression] = None,
             synonym: Union[str, MatchExpression] = None,
             synonym_searchable: Union[str, MatchExpression] = None,
             panther_family: Union[str, MatchExpression] = None,
             panther_family_searchable: Union[str, MatchExpression] = None,
             panther_family_label: Union[str, MatchExpression] = None,
             panther_family_label_searchable: Union[str, MatchExpression] = None,
             phylo_graph_json: Union[str, MatchExpression] = None,
             database_xref: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[Bioentity]:
        """
        Queries for instances of `Bioentity`

        :param document_category: None
        :param id: Term acc/ID.
        :param bioentity: Gene or gene product identifiers.
        :param bioentity_label: Gene or gene product identifiers.
        :param bioentity_label_searchable: Gene or gene product identifiers.
        :param bioentity_name: The full name of the gene or gene product.
        :param bioentity_name_searchable: The full name of the gene or gene product.
        :param bioentity_internal_id: The bioentity ID used at the database of origin.
        :param type: Type class.
        :param taxon: taxon of the entity in enabled_by
        :param taxon_label: label for taxon
        :param taxon_label_searchable: label for taxon
        :param taxon_closure: is_a closure of taxon
        :param taxon_closure_label: labels of is_a closure.
        :param taxon_closure_label_searchable: labels of is_a closure.
        :param taxon_subset_closure: Taxonomic group (direct) and ancestral groups that are within the specified subset (e.g mammalia, eukaryota).
        :param taxon_subset_closure_label: Labels for taxonomic group (direct) and ancestral groups that are within the specified subset.
        :param taxon_subset_closure_label_searchable: Labels for taxonomic group (direct) and ancestral groups that are within the specified subset.
        :param isa_partof_closure: Ancestral terms (is_a/part_of).
        :param isa_partof_closure_label: Ancestral terms (is_a/part_of).
        :param isa_partof_closure_label_searchable: Ancestral terms (is_a/part_of).
        :param regulates_closure: Ancestral terms (regulates, occurs in, capable_of).
        :param regulates_closure_label: Ancestral terms (regulates, occurs in, capable_of).
        :param regulates_closure_label_searchable: Ancestral terms (regulates, occurs in, capable_of).
        :param source: Term namespace. In GO, this is one of: biological_process, molecular_function, cellular_component. In other ontologies it is not guaranteed to be populated. Consider using idspace instead for general queries.
        :param annotation_class_list: Direct annotations.
        :param annotation_class_list_label: Direct annotations.
        :param synonym: Term synonyms.
        :param synonym_searchable: Term synonyms.
        :param panther_family: PANTHER family IDs that are associated with this entity.
        :param panther_family_searchable: PANTHER family IDs that are associated with this entity.
        :param panther_family_label: PANTHER families that are associated with this entity.
        :param panther_family_label_searchable: PANTHER families that are associated with this entity.
        :param phylo_graph_json: JSON blob form of the phylogenic tree.
        :param database_xref: Database cross-reference.
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(Bioentity.class_name,
                                                 
                                                 document_category=document_category,
                                                 
                                                 id=id,
                                                 
                                                 bioentity=bioentity,
                                                 
                                                 bioentity_label=bioentity_label,
                                                 
                                                 bioentity_label_searchable=bioentity_label_searchable,
                                                 
                                                 bioentity_name=bioentity_name,
                                                 
                                                 bioentity_name_searchable=bioentity_name_searchable,
                                                 
                                                 bioentity_internal_id=bioentity_internal_id,
                                                 
                                                 type=type,
                                                 
                                                 taxon=taxon,
                                                 
                                                 taxon_label=taxon_label,
                                                 
                                                 taxon_label_searchable=taxon_label_searchable,
                                                 
                                                 taxon_closure=taxon_closure,
                                                 
                                                 taxon_closure_label=taxon_closure_label,
                                                 
                                                 taxon_closure_label_searchable=taxon_closure_label_searchable,
                                                 
                                                 taxon_subset_closure=taxon_subset_closure,
                                                 
                                                 taxon_subset_closure_label=taxon_subset_closure_label,
                                                 
                                                 taxon_subset_closure_label_searchable=taxon_subset_closure_label_searchable,
                                                 
                                                 isa_partof_closure=isa_partof_closure,
                                                 
                                                 isa_partof_closure_label=isa_partof_closure_label,
                                                 
                                                 isa_partof_closure_label_searchable=isa_partof_closure_label_searchable,
                                                 
                                                 regulates_closure=regulates_closure,
                                                 
                                                 regulates_closure_label=regulates_closure_label,
                                                 
                                                 regulates_closure_label_searchable=regulates_closure_label_searchable,
                                                 
                                                 source=source,
                                                 
                                                 annotation_class_list=annotation_class_list,
                                                 
                                                 annotation_class_list_label=annotation_class_list_label,
                                                 
                                                 synonym=synonym,
                                                 
                                                 synonym_searchable=synonym_searchable,
                                                 
                                                 panther_family=panther_family,
                                                 
                                                 panther_family_searchable=panther_family_searchable,
                                                 
                                                 panther_family_label=panther_family_label,
                                                 
                                                 panther_family_label_searchable=panther_family_label_searchable,
                                                 
                                                 phylo_graph_json=phylo_graph_json,
                                                 
                                                 database_xref=database_xref,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # ComplexAnnotation methods
    # --
    def fetch_ComplexAnnotation(self, id_value: str) -> ComplexAnnotation:
        """
        Retrieves an instance of `ComplexAnnotation` via a primary key

        :param id_value:
        :return: ComplexAnnotation with matching ID
        """
        q = FetchById(id=id_value, target_class=ComplexAnnotation.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_ComplexAnnotation(self,
             document_category: Union[str, MatchExpression] = None,
             id: Union[str, MatchExpression] = None,
             annotation_unit: Union[str, MatchExpression] = None,
             annotation_unit_label: Union[str, MatchExpression] = None,
             annotation_unit_label_searchable: Union[str, MatchExpression] = None,
             annotation_group: Union[str, MatchExpression] = None,
             annotation_group_label: Union[str, MatchExpression] = None,
             annotation_group_label_searchable: Union[str, MatchExpression] = None,
             annotation_group_url: Union[str, MatchExpression] = None,
             enabled_by: Union[str, MatchExpression] = None,
             enabled_by_searchable: Union[str, MatchExpression] = None,
             enabled_by_label: Union[str, MatchExpression] = None,
             enabled_by_label_searchable: Union[str, MatchExpression] = None,
             panther_family: Union[str, MatchExpression] = None,
             panther_family_searchable: Union[str, MatchExpression] = None,
             panther_family_label: Union[str, MatchExpression] = None,
             panther_family_label_searchable: Union[str, MatchExpression] = None,
             taxon: Union[str, MatchExpression] = None,
             taxon_label: Union[str, MatchExpression] = None,
             taxon_label_searchable: Union[str, MatchExpression] = None,
             taxon_closure: Union[str, MatchExpression] = None,
             taxon_closure_label: Union[str, MatchExpression] = None,
             taxon_closure_label_searchable: Union[str, MatchExpression] = None,
             function_class: Union[str, MatchExpression] = None,
             function_class_label: Union[str, MatchExpression] = None,
             function_class_label_searchable: Union[str, MatchExpression] = None,
             function_class_closure: Union[str, MatchExpression] = None,
             function_class_closure_label: Union[str, MatchExpression] = None,
             function_class_closure_label_searchable: Union[str, MatchExpression] = None,
             process_class: Union[str, MatchExpression] = None,
             process_class_label: Union[str, MatchExpression] = None,
             process_class_label_searchable: Union[str, MatchExpression] = None,
             process_class_closure: Union[str, MatchExpression] = None,
             process_class_closure_label: Union[str, MatchExpression] = None,
             process_class_closure_label_searchable: Union[str, MatchExpression] = None,
             location_list: Union[str, MatchExpression] = None,
             location_list_label: Union[str, MatchExpression] = None,
             location_list_closure: Union[str, MatchExpression] = None,
             location_list_closure_label: Union[str, MatchExpression] = None,
             owl_blob_json: Union[str, MatchExpression] = None,
             topology_graph_json: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[ComplexAnnotation]:
        """
        Queries for instances of `ComplexAnnotation`

        :param document_category: None
        :param id: Term acc/ID.
        :param annotation_unit: The title(s) associated with the model.
        :param annotation_unit_label: The title(s) associated with the model.
        :param annotation_unit_label_searchable: The title(s) associated with the model.
        :param annotation_group: ???.
        :param annotation_group_label: ???.
        :param annotation_group_label_searchable: ???.
        :param annotation_group_url: ???.
        :param enabled_by: The CURIE for the ro:enabled_by.rdf:type value of the annoton/MF individual
        :param enabled_by_searchable: The CURIE for the ro:enabled_by.rdf:type value of the annoton/MF individual
        :param enabled_by_label: Searchable label version of the gene product
        :param enabled_by_label_searchable: Searchable label version of the gene product
        :param panther_family: PANTHER family IDs that are associated with this entity.
        :param panther_family_searchable: PANTHER family IDs that are associated with this entity.
        :param panther_family_label: PANTHER families that are associated with this entity.
        :param panther_family_label_searchable: PANTHER families that are associated with this entity.
        :param taxon: taxon of the entity in enabled_by
        :param taxon_label: label for taxon
        :param taxon_label_searchable: label for taxon
        :param taxon_closure: is_a closure of taxon
        :param taxon_closure_label: labels of is_a closure.
        :param taxon_closure_label_searchable: labels of is_a closure.
        :param function_class: This is the value of rdf:type for the annoton/MF instance
        :param function_class_label: Common function name.
        :param function_class_label_searchable: Common function name.
        :param function_class_closure: ???
        :param function_class_closure_label: ???
        :param function_class_closure_label_searchable: ???
        :param process_class: Process acc/ID.
        :param process_class_label: Common process name.
        :param process_class_label_searchable: Common process name.
        :param process_class_closure: ???
        :param process_class_closure_label: ???
        :param process_class_closure_label_searchable: ???
        :param location_list: 
        :param location_list_label: 
        :param location_list_closure: 
        :param location_list_closure_label: 
        :param owl_blob_json: ???
        :param topology_graph_json: JSON blob form of the local stepwise topology graph. Uses various relations (including regulates, occurs in, capable_of).
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(ComplexAnnotation.class_name,
                                                 
                                                 document_category=document_category,
                                                 
                                                 id=id,
                                                 
                                                 annotation_unit=annotation_unit,
                                                 
                                                 annotation_unit_label=annotation_unit_label,
                                                 
                                                 annotation_unit_label_searchable=annotation_unit_label_searchable,
                                                 
                                                 annotation_group=annotation_group,
                                                 
                                                 annotation_group_label=annotation_group_label,
                                                 
                                                 annotation_group_label_searchable=annotation_group_label_searchable,
                                                 
                                                 annotation_group_url=annotation_group_url,
                                                 
                                                 enabled_by=enabled_by,
                                                 
                                                 enabled_by_searchable=enabled_by_searchable,
                                                 
                                                 enabled_by_label=enabled_by_label,
                                                 
                                                 enabled_by_label_searchable=enabled_by_label_searchable,
                                                 
                                                 panther_family=panther_family,
                                                 
                                                 panther_family_searchable=panther_family_searchable,
                                                 
                                                 panther_family_label=panther_family_label,
                                                 
                                                 panther_family_label_searchable=panther_family_label_searchable,
                                                 
                                                 taxon=taxon,
                                                 
                                                 taxon_label=taxon_label,
                                                 
                                                 taxon_label_searchable=taxon_label_searchable,
                                                 
                                                 taxon_closure=taxon_closure,
                                                 
                                                 taxon_closure_label=taxon_closure_label,
                                                 
                                                 taxon_closure_label_searchable=taxon_closure_label_searchable,
                                                 
                                                 function_class=function_class,
                                                 
                                                 function_class_label=function_class_label,
                                                 
                                                 function_class_label_searchable=function_class_label_searchable,
                                                 
                                                 function_class_closure=function_class_closure,
                                                 
                                                 function_class_closure_label=function_class_closure_label,
                                                 
                                                 function_class_closure_label_searchable=function_class_closure_label_searchable,
                                                 
                                                 process_class=process_class,
                                                 
                                                 process_class_label=process_class_label,
                                                 
                                                 process_class_label_searchable=process_class_label_searchable,
                                                 
                                                 process_class_closure=process_class_closure,
                                                 
                                                 process_class_closure_label=process_class_closure_label,
                                                 
                                                 process_class_closure_label_searchable=process_class_closure_label_searchable,
                                                 
                                                 location_list=location_list,
                                                 
                                                 location_list_label=location_list_label,
                                                 
                                                 location_list_closure=location_list_closure,
                                                 
                                                 location_list_closure_label=location_list_closure_label,
                                                 
                                                 owl_blob_json=owl_blob_json,
                                                 
                                                 topology_graph_json=topology_graph_json,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # General methods
    # --
    def fetch_General(self, id_value: str) -> General:
        """
        Retrieves an instance of `General` via a primary key

        :param id_value:
        :return: General with matching ID
        """
        q = FetchById(id=id_value, target_class=General.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_General(self,
             document_category: Union[str, MatchExpression] = None,
             id: Union[str, MatchExpression] = None,
             entity: Union[str, MatchExpression] = None,
             entity_label: Union[str, MatchExpression] = None,
             entity_label_searchable: Union[str, MatchExpression] = None,
             category: Union[str, MatchExpression] = None,
             general_blob: Union[str, MatchExpression] = None,
             general_blob_searchable: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[General]:
        """
        Queries for instances of `General`

        :param document_category: None
        :param id: Term acc/ID.
        :param entity: The ID/label for this entity.
        :param entity_label: The label for this entity.
        :param entity_label_searchable: The label for this entity.
        :param category: The document category that this enitity belongs to.
        :param general_blob: A hidden searchable blob document to access this item. It should contain all the goodies that we want to search for, like species(?), synonyms, etc.
        :param general_blob_searchable: A hidden searchable blob document to access this item. It should contain all the goodies that we want to search for, like species(?), synonyms, etc.
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(General.class_name,
                                                 
                                                 document_category=document_category,
                                                 
                                                 id=id,
                                                 
                                                 entity=entity,
                                                 
                                                 entity_label=entity_label,
                                                 
                                                 entity_label_searchable=entity_label_searchable,
                                                 
                                                 category=category,
                                                 
                                                 general_blob=general_blob,
                                                 
                                                 general_blob_searchable=general_blob_searchable,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # ModelAnnotation methods
    # --
    def fetch_ModelAnnotation(self, id_value: str) -> ModelAnnotation:
        """
        Retrieves an instance of `ModelAnnotation` via a primary key

        :param id_value:
        :return: ModelAnnotation with matching ID
        """
        q = FetchById(id=id_value, target_class=ModelAnnotation.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_ModelAnnotation(self,
             document_category: Union[str, MatchExpression] = None,
             id: Union[str, MatchExpression] = None,
             annotation_unit: Union[str, MatchExpression] = None,
             annotation_unit_label: Union[str, MatchExpression] = None,
             annotation_unit_label_searchable: Union[str, MatchExpression] = None,
             model: Union[str, MatchExpression] = None,
             model_label: Union[str, MatchExpression] = None,
             model_label_searchable: Union[str, MatchExpression] = None,
             model_url: Union[str, MatchExpression] = None,
             model_state: Union[str, MatchExpression] = None,
             annotation_value: Union[str, MatchExpression] = None,
             contributor: Union[str, MatchExpression] = None,
             contributor_searchable: Union[str, MatchExpression] = None,
             model_date: Union[str, MatchExpression] = None,
             model_date_searchable: Union[str, MatchExpression] = None,
             comment: Union[str, MatchExpression] = None,
             comment_searchable: Union[str, MatchExpression] = None,
             enabled_by: Union[str, MatchExpression] = None,
             enabled_by_searchable: Union[str, MatchExpression] = None,
             enabled_by_label: Union[str, MatchExpression] = None,
             enabled_by_label_searchable: Union[str, MatchExpression] = None,
             enabled_by_complex: Union[str, MatchExpression] = None,
             enabled_by_complex_searchable: Union[str, MatchExpression] = None,
             enabled_by_complex_label: Union[str, MatchExpression] = None,
             enabled_by_complex_label_searchable: Union[str, MatchExpression] = None,
             has_participant: Union[str, MatchExpression] = None,
             has_participant_searchable: Union[str, MatchExpression] = None,
             has_participant_label: Union[str, MatchExpression] = None,
             has_participant_label_searchable: Union[str, MatchExpression] = None,
             has_complex_participant: Union[str, MatchExpression] = None,
             has_complex_participant_searchable: Union[str, MatchExpression] = None,
             has_complex_participant_label: Union[str, MatchExpression] = None,
             has_complex_participant_label_searchable: Union[str, MatchExpression] = None,
             has_output: Union[str, MatchExpression] = None,
             has_output_searchable: Union[str, MatchExpression] = None,
             has_output_label: Union[str, MatchExpression] = None,
             has_output_label_searchable: Union[str, MatchExpression] = None,
             has_complex_output: Union[str, MatchExpression] = None,
             has_complex_output_searchable: Union[str, MatchExpression] = None,
             has_complex_output_label: Union[str, MatchExpression] = None,
             has_complex_output_label_searchable: Union[str, MatchExpression] = None,
             panther_family: Union[str, MatchExpression] = None,
             panther_family_searchable: Union[str, MatchExpression] = None,
             panther_family_label: Union[str, MatchExpression] = None,
             panther_family_label_searchable: Union[str, MatchExpression] = None,
             taxon: Union[str, MatchExpression] = None,
             taxon_label: Union[str, MatchExpression] = None,
             taxon_label_searchable: Union[str, MatchExpression] = None,
             taxon_closure: Union[str, MatchExpression] = None,
             taxon_closure_label: Union[str, MatchExpression] = None,
             taxon_closure_label_searchable: Union[str, MatchExpression] = None,
             function_class: Union[str, MatchExpression] = None,
             function_class_label: Union[str, MatchExpression] = None,
             function_class_label_searchable: Union[str, MatchExpression] = None,
             function_class_closure: Union[str, MatchExpression] = None,
             function_class_closure_label: Union[str, MatchExpression] = None,
             function_class_closure_label_searchable: Union[str, MatchExpression] = None,
             process_class: Union[str, MatchExpression] = None,
             process_class_label: Union[str, MatchExpression] = None,
             process_class_label_searchable: Union[str, MatchExpression] = None,
             process_class_closure: Union[str, MatchExpression] = None,
             process_class_closure_label: Union[str, MatchExpression] = None,
             process_class_closure_label_searchable: Union[str, MatchExpression] = None,
             location_list: Union[str, MatchExpression] = None,
             location_list_label: Union[str, MatchExpression] = None,
             location_list_closure: Union[str, MatchExpression] = None,
             location_list_closure_label: Union[str, MatchExpression] = None,
             owl_blob_json: Union[str, MatchExpression] = None,
             topology_graph_json: Union[str, MatchExpression] = None,
             evidence_type: Union[str, MatchExpression] = None,
             evidence_type_closure: Union[str, MatchExpression] = None,
             evidence_type_label: Union[str, MatchExpression] = None,
             evidence_type_label_searchable: Union[str, MatchExpression] = None,
             evidence_type_closure_label: Union[str, MatchExpression] = None,
             evidence_type_closure_label_searchable: Union[str, MatchExpression] = None,
             evidence_with: Union[str, MatchExpression] = None,
             evidence_with_searchable: Union[str, MatchExpression] = None,
             reference: Union[str, MatchExpression] = None,
             reference_searchable: Union[str, MatchExpression] = None,
             relationship: Union[str, MatchExpression] = None,
             relationship_searchable: Union[str, MatchExpression] = None,
             relationship_label: Union[str, MatchExpression] = None,
             relationship_label_searchable: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[ModelAnnotation]:
        """
        Queries for instances of `ModelAnnotation`

        :param document_category: None
        :param id: Term acc/ID.
        :param annotation_unit: The title(s) associated with the model.
        :param annotation_unit_label: The title(s) associated with the model.
        :param annotation_unit_label_searchable: The title(s) associated with the model.
        :param model: The CURIE of the model to which the annoton belongs
        :param model_label: The dc:title of the model to which the annoton belongs
        :param model_label_searchable: The dc:title of the model to which the annoton belongs
        :param model_url: The URI of the model to which the annoton belongs
        :param model_state: The editorial state of the model.
        :param annotation_value: set of all literal values of all annotation assertions in model
        :param contributor: Contributor identity.
        :param contributor_searchable: Contributor identity.
        :param model_date: Model last modification dates.
        :param model_date_searchable: Model last modification dates.
        :param comment: Term comments.
        :param comment_searchable: Term comments.
        :param enabled_by: The CURIE for the ro:enabled_by.rdf:type value of the annoton/MF individual
        :param enabled_by_searchable: The CURIE for the ro:enabled_by.rdf:type value of the annoton/MF individual
        :param enabled_by_label: Searchable label version of the gene product
        :param enabled_by_label_searchable: Searchable label version of the gene product
        :param enabled_by_complex: The CURIE for the ro:enabled_by.rdf:type value of the annoton/MF individual
        :param enabled_by_complex_searchable: The CURIE for the ro:enabled_by.rdf:type value of the annoton/MF individual
        :param enabled_by_complex_label: Searchable label version of the complex
        :param enabled_by_complex_label_searchable: Searchable label version of the complex
        :param has_participant: The CURIE for the ro:has_participant.rdf:type value of the annoton/MF individual
        :param has_participant_searchable: The CURIE for the ro:has_participant.rdf:type value of the annoton/MF individual
        :param has_participant_label: Searchable label version of participant entities
        :param has_participant_label_searchable: Searchable label version of participant entities
        :param has_complex_participant: The CURIE for the ro:has_participant.rdf:type value of the annoton/MF individual
        :param has_complex_participant_searchable: The CURIE for the ro:has_participant.rdf:type value of the annoton/MF individual
        :param has_complex_participant_label: Searchable label version of participant entities
        :param has_complex_participant_label_searchable: Searchable label version of participant entities
        :param has_output: The CURIE for the ro:has_output.rdf:type value of the annoton/MF individual
        :param has_output_searchable: The CURIE for the ro:has_output.rdf:type value of the annoton/MF individual
        :param has_output_label: Searchable label version of output entities
        :param has_output_label_searchable: Searchable label version of output entities
        :param has_complex_output: The CURIE for the ro:has_output.rdf:type value of the annoton/MF individual
        :param has_complex_output_searchable: The CURIE for the ro:has_output.rdf:type value of the annoton/MF individual
        :param has_complex_output_label: Searchable label version of output entities
        :param has_complex_output_label_searchable: Searchable label version of output entities
        :param panther_family: PANTHER family IDs that are associated with this entity.
        :param panther_family_searchable: PANTHER family IDs that are associated with this entity.
        :param panther_family_label: PANTHER families that are associated with this entity.
        :param panther_family_label_searchable: PANTHER families that are associated with this entity.
        :param taxon: taxon of the entity in enabled_by
        :param taxon_label: label for taxon
        :param taxon_label_searchable: label for taxon
        :param taxon_closure: is_a closure of taxon
        :param taxon_closure_label: labels of is_a closure.
        :param taxon_closure_label_searchable: labels of is_a closure.
        :param function_class: This is the value of rdf:type for the annoton/MF instance
        :param function_class_label: Common function name.
        :param function_class_label_searchable: Common function name.
        :param function_class_closure: ???
        :param function_class_closure_label: ???
        :param function_class_closure_label_searchable: ???
        :param process_class: Process acc/ID.
        :param process_class_label: Common process name.
        :param process_class_label_searchable: Common process name.
        :param process_class_closure: ???
        :param process_class_closure_label: ???
        :param process_class_closure_label_searchable: ???
        :param location_list: 
        :param location_list_label: 
        :param location_list_closure: 
        :param location_list_closure_label: 
        :param owl_blob_json: ???
        :param topology_graph_json: JSON blob form of the local stepwise topology graph. Uses various relations (including regulates, occurs in, capable_of).
        :param evidence_type: Evidence type.
        :param evidence_type_closure: All evidence (evidence closure) for this annotation
        :param evidence_type_label: Evidence type.
        :param evidence_type_label_searchable: Evidence type.
        :param evidence_type_closure_label: All evidence (evidence closure) for this annotation
        :param evidence_type_closure_label_searchable: All evidence (evidence closure) for this annotation
        :param evidence_with: Evidence with/from.
        :param evidence_with_searchable: Evidence with/from.
        :param reference: Database reference.
        :param reference_searchable: Database reference.
        :param relationship: List the distinct relationship types
        :param relationship_searchable: List the distinct relationship types
        :param relationship_label: 
        :param relationship_label_searchable: 
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(ModelAnnotation.class_name,
                                                 
                                                 document_category=document_category,
                                                 
                                                 id=id,
                                                 
                                                 annotation_unit=annotation_unit,
                                                 
                                                 annotation_unit_label=annotation_unit_label,
                                                 
                                                 annotation_unit_label_searchable=annotation_unit_label_searchable,
                                                 
                                                 model=model,
                                                 
                                                 model_label=model_label,
                                                 
                                                 model_label_searchable=model_label_searchable,
                                                 
                                                 model_url=model_url,
                                                 
                                                 model_state=model_state,
                                                 
                                                 annotation_value=annotation_value,
                                                 
                                                 contributor=contributor,
                                                 
                                                 contributor_searchable=contributor_searchable,
                                                 
                                                 model_date=model_date,
                                                 
                                                 model_date_searchable=model_date_searchable,
                                                 
                                                 comment=comment,
                                                 
                                                 comment_searchable=comment_searchable,
                                                 
                                                 enabled_by=enabled_by,
                                                 
                                                 enabled_by_searchable=enabled_by_searchable,
                                                 
                                                 enabled_by_label=enabled_by_label,
                                                 
                                                 enabled_by_label_searchable=enabled_by_label_searchable,
                                                 
                                                 enabled_by_complex=enabled_by_complex,
                                                 
                                                 enabled_by_complex_searchable=enabled_by_complex_searchable,
                                                 
                                                 enabled_by_complex_label=enabled_by_complex_label,
                                                 
                                                 enabled_by_complex_label_searchable=enabled_by_complex_label_searchable,
                                                 
                                                 has_participant=has_participant,
                                                 
                                                 has_participant_searchable=has_participant_searchable,
                                                 
                                                 has_participant_label=has_participant_label,
                                                 
                                                 has_participant_label_searchable=has_participant_label_searchable,
                                                 
                                                 has_complex_participant=has_complex_participant,
                                                 
                                                 has_complex_participant_searchable=has_complex_participant_searchable,
                                                 
                                                 has_complex_participant_label=has_complex_participant_label,
                                                 
                                                 has_complex_participant_label_searchable=has_complex_participant_label_searchable,
                                                 
                                                 has_output=has_output,
                                                 
                                                 has_output_searchable=has_output_searchable,
                                                 
                                                 has_output_label=has_output_label,
                                                 
                                                 has_output_label_searchable=has_output_label_searchable,
                                                 
                                                 has_complex_output=has_complex_output,
                                                 
                                                 has_complex_output_searchable=has_complex_output_searchable,
                                                 
                                                 has_complex_output_label=has_complex_output_label,
                                                 
                                                 has_complex_output_label_searchable=has_complex_output_label_searchable,
                                                 
                                                 panther_family=panther_family,
                                                 
                                                 panther_family_searchable=panther_family_searchable,
                                                 
                                                 panther_family_label=panther_family_label,
                                                 
                                                 panther_family_label_searchable=panther_family_label_searchable,
                                                 
                                                 taxon=taxon,
                                                 
                                                 taxon_label=taxon_label,
                                                 
                                                 taxon_label_searchable=taxon_label_searchable,
                                                 
                                                 taxon_closure=taxon_closure,
                                                 
                                                 taxon_closure_label=taxon_closure_label,
                                                 
                                                 taxon_closure_label_searchable=taxon_closure_label_searchable,
                                                 
                                                 function_class=function_class,
                                                 
                                                 function_class_label=function_class_label,
                                                 
                                                 function_class_label_searchable=function_class_label_searchable,
                                                 
                                                 function_class_closure=function_class_closure,
                                                 
                                                 function_class_closure_label=function_class_closure_label,
                                                 
                                                 function_class_closure_label_searchable=function_class_closure_label_searchable,
                                                 
                                                 process_class=process_class,
                                                 
                                                 process_class_label=process_class_label,
                                                 
                                                 process_class_label_searchable=process_class_label_searchable,
                                                 
                                                 process_class_closure=process_class_closure,
                                                 
                                                 process_class_closure_label=process_class_closure_label,
                                                 
                                                 process_class_closure_label_searchable=process_class_closure_label_searchable,
                                                 
                                                 location_list=location_list,
                                                 
                                                 location_list_label=location_list_label,
                                                 
                                                 location_list_closure=location_list_closure,
                                                 
                                                 location_list_closure_label=location_list_closure_label,
                                                 
                                                 owl_blob_json=owl_blob_json,
                                                 
                                                 topology_graph_json=topology_graph_json,
                                                 
                                                 evidence_type=evidence_type,
                                                 
                                                 evidence_type_closure=evidence_type_closure,
                                                 
                                                 evidence_type_label=evidence_type_label,
                                                 
                                                 evidence_type_label_searchable=evidence_type_label_searchable,
                                                 
                                                 evidence_type_closure_label=evidence_type_closure_label,
                                                 
                                                 evidence_type_closure_label_searchable=evidence_type_closure_label_searchable,
                                                 
                                                 evidence_with=evidence_with,
                                                 
                                                 evidence_with_searchable=evidence_with_searchable,
                                                 
                                                 reference=reference,
                                                 
                                                 reference_searchable=reference_searchable,
                                                 
                                                 relationship=relationship,
                                                 
                                                 relationship_searchable=relationship_searchable,
                                                 
                                                 relationship_label=relationship_label,
                                                 
                                                 relationship_label_searchable=relationship_label_searchable,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # NoctuaModelMeta methods
    # --
    def fetch_NoctuaModelMeta(self, id_value: str) -> NoctuaModelMeta:
        """
        Retrieves an instance of `NoctuaModelMeta` via a primary key

        :param id_value:
        :return: NoctuaModelMeta with matching ID
        """
        q = FetchById(id=id_value, target_class=NoctuaModelMeta.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_NoctuaModelMeta(self,
             document_category: Union[str, MatchExpression] = None,
             id: Union[str, MatchExpression] = None,
             annotation_unit: Union[str, MatchExpression] = None,
             annotation_unit_label: Union[str, MatchExpression] = None,
             annotation_unit_label_searchable: Union[str, MatchExpression] = None,
             contributor: Union[str, MatchExpression] = None,
             contributor_searchable: Union[str, MatchExpression] = None,
             model_date: Union[str, MatchExpression] = None,
             model_date_searchable: Union[str, MatchExpression] = None,
             model_state: Union[str, MatchExpression] = None,
             comment: Union[str, MatchExpression] = None,
             comment_searchable: Union[str, MatchExpression] = None,
             owl_blob_json: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[NoctuaModelMeta]:
        """
        Queries for instances of `NoctuaModelMeta`

        :param document_category: None
        :param id: Term acc/ID.
        :param annotation_unit: The title(s) associated with the model.
        :param annotation_unit_label: The title(s) associated with the model.
        :param annotation_unit_label_searchable: The title(s) associated with the model.
        :param contributor: Contributor identity.
        :param contributor_searchable: Contributor identity.
        :param model_date: Model last modification dates.
        :param model_date_searchable: Model last modification dates.
        :param model_state: The editorial state of the model.
        :param comment: Term comments.
        :param comment_searchable: Term comments.
        :param owl_blob_json: ???
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(NoctuaModelMeta.class_name,
                                                 
                                                 document_category=document_category,
                                                 
                                                 id=id,
                                                 
                                                 annotation_unit=annotation_unit,
                                                 
                                                 annotation_unit_label=annotation_unit_label,
                                                 
                                                 annotation_unit_label_searchable=annotation_unit_label_searchable,
                                                 
                                                 contributor=contributor,
                                                 
                                                 contributor_searchable=contributor_searchable,
                                                 
                                                 model_date=model_date,
                                                 
                                                 model_date_searchable=model_date_searchable,
                                                 
                                                 model_state=model_state,
                                                 
                                                 comment=comment,
                                                 
                                                 comment_searchable=comment_searchable,
                                                 
                                                 owl_blob_json=owl_blob_json,
                                                 
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
             document_category: Union[str, MatchExpression] = None,
             id: Union[str, MatchExpression] = None,
             annotation_class: Union[str, MatchExpression] = None,
             annotation_class_label: Union[str, MatchExpression] = None,
             annotation_class_label_searchable: Union[str, MatchExpression] = None,
             description: Union[str, MatchExpression] = None,
             description_searchable: Union[str, MatchExpression] = None,
             source: Union[str, MatchExpression] = None,
             idspace: Union[str, MatchExpression] = None,
             is_obsolete: Union[str, MatchExpression] = None,
             comment: Union[str, MatchExpression] = None,
             comment_searchable: Union[str, MatchExpression] = None,
             synonym: Union[str, MatchExpression] = None,
             synonym_searchable: Union[str, MatchExpression] = None,
             alternate_id: Union[str, MatchExpression] = None,
             replaced_by: Union[str, MatchExpression] = None,
             consider: Union[str, MatchExpression] = None,
             subset: Union[str, MatchExpression] = None,
             definition_xref: Union[str, MatchExpression] = None,
             database_xref: Union[str, MatchExpression] = None,
             isa_partof_closure: Union[str, MatchExpression] = None,
             isa_partof_closure_label: Union[str, MatchExpression] = None,
             isa_partof_closure_label_searchable: Union[str, MatchExpression] = None,
             isa_closure: Union[str, MatchExpression] = None,
             isa_closure_label: Union[str, MatchExpression] = None,
             isa_closure_label_searchable: Union[str, MatchExpression] = None,
             regulates_closure: Union[str, MatchExpression] = None,
             regulates_closure_label: Union[str, MatchExpression] = None,
             regulates_closure_label_searchable: Union[str, MatchExpression] = None,
             topology_graph_json: Union[str, MatchExpression] = None,
             regulates_transitivity_graph_json: Union[str, MatchExpression] = None,
             isa_partof_transitivity_graph_json: Union[str, MatchExpression] = None,
             neighborhood_graph_json: Union[str, MatchExpression] = None,
             neighborhood_limited_graph_json: Union[str, MatchExpression] = None,
             only_in_taxon: Union[str, MatchExpression] = None,
             only_in_taxon_searchable: Union[str, MatchExpression] = None,
             only_in_taxon_label: Union[str, MatchExpression] = None,
             only_in_taxon_label_searchable: Union[str, MatchExpression] = None,
             only_in_taxon_closure: Union[str, MatchExpression] = None,
             only_in_taxon_closure_label: Union[str, MatchExpression] = None,
             only_in_taxon_closure_label_searchable: Union[str, MatchExpression] = None,
             annotation_extension_owl_json: Union[str, MatchExpression] = None,
             annotation_relation: Union[str, MatchExpression] = None,
             annotation_relation_label: Union[str, MatchExpression] = None,
             annotation_relation_label_searchable: Union[str, MatchExpression] = None,
             equivalent_class_expressions_json: Union[str, MatchExpression] = None,
             disjoint_class_list: Union[str, MatchExpression] = None,
             disjoint_class_list_label: Union[str, MatchExpression] = None,
             disjoint_class_list_label_searchable: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[OntologyClass]:
        """
        Queries for instances of `OntologyClass`

        :param document_category: None
        :param id: Term acc/ID.
        :param annotation_class: Term acc/ID.
        :param annotation_class_label: Common term name.
        :param annotation_class_label_searchable: Common term name.
        :param description: Term definition.
        :param description_searchable: Term definition.
        :param source: Term namespace. In GO, this is one of: biological_process, molecular_function, cellular_component. In other ontologies it is not guaranteed to be populated. Consider using idspace instead for general queries.
        :param idspace: Term ID space.
        :param is_obsolete: Is the term obsolete?
        :param comment: Term comments.
        :param comment_searchable: Term comments.
        :param synonym: Term synonyms.
        :param synonym_searchable: Term synonyms.
        :param alternate_id: Alternate term id.
        :param replaced_by: Term that replaces this term.
        :param consider: Others terms you might want to look at.
        :param subset: Special use collections of terms.
        :param definition_xref: Definition cross-reference.
        :param database_xref: Database cross-reference.
        :param isa_partof_closure: Ancestral terms (is_a/part_of).
        :param isa_partof_closure_label: Ancestral terms (is_a/part_of).
        :param isa_partof_closure_label_searchable: Ancestral terms (is_a/part_of).
        :param isa_closure: Ancestral terms (is_a).
        :param isa_closure_label: Ancestral terms (is_a) labels.
        :param isa_closure_label_searchable: Ancestral terms (is_a) labels.
        :param regulates_closure: Ancestral terms (regulates, occurs in, capable_of).
        :param regulates_closure_label: Ancestral terms (regulates, occurs in, capable_of).
        :param regulates_closure_label_searchable: Ancestral terms (regulates, occurs in, capable_of).
        :param topology_graph_json: JSON blob form of the local stepwise topology graph. Uses various relations (including regulates, occurs in, capable_of).
        :param regulates_transitivity_graph_json: JSON blob form of the local relation transitivity graph. Uses various relations (including regulates, occurs in, capable_of).
        :param isa_partof_transitivity_graph_json: JSON blob form of the local relation transitivity graph using is-a and part-of
        :param neighborhood_graph_json: JSON blob form of all immediate neighbors of the term.
        :param neighborhood_limited_graph_json: JSON blob form of all immediate neighbors of the term; in the case that there are too many neighbors to transport, the number will be artificially reduced.
        :param only_in_taxon: Only in taxon.
        :param only_in_taxon_searchable: Only in taxon.
        :param only_in_taxon_label: Only in taxon label.
        :param only_in_taxon_label_searchable: Only in taxon label.
        :param only_in_taxon_closure: Only in taxon closure.
        :param only_in_taxon_closure_label: Only in taxon label closure.
        :param only_in_taxon_closure_label_searchable: Only in taxon label closure.
        :param annotation_extension_owl_json: A non-lossy representation of conjunctions and disjunctions in c16 (JSON).
        :param annotation_relation: This is equivalent to the relation field in GPAD.
        :param annotation_relation_label: This is equivalent to the relation field in GPAD.
        :param annotation_relation_label_searchable: This is equivalent to the relation field in GPAD.
        :param equivalent_class_expressions_json: For any class document C, this will contain json(CE) for all axioms of form EquivalentClasses(C ... CE ....).
        :param disjoint_class_list: Disjoint classes.
        :param disjoint_class_list_label: Disjoint classes.
        :param disjoint_class_list_label_searchable: Disjoint classes.
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(OntologyClass.class_name,
                                                 
                                                 document_category=document_category,
                                                 
                                                 id=id,
                                                 
                                                 annotation_class=annotation_class,
                                                 
                                                 annotation_class_label=annotation_class_label,
                                                 
                                                 annotation_class_label_searchable=annotation_class_label_searchable,
                                                 
                                                 description=description,
                                                 
                                                 description_searchable=description_searchable,
                                                 
                                                 source=source,
                                                 
                                                 idspace=idspace,
                                                 
                                                 is_obsolete=is_obsolete,
                                                 
                                                 comment=comment,
                                                 
                                                 comment_searchable=comment_searchable,
                                                 
                                                 synonym=synonym,
                                                 
                                                 synonym_searchable=synonym_searchable,
                                                 
                                                 alternate_id=alternate_id,
                                                 
                                                 replaced_by=replaced_by,
                                                 
                                                 consider=consider,
                                                 
                                                 subset=subset,
                                                 
                                                 definition_xref=definition_xref,
                                                 
                                                 database_xref=database_xref,
                                                 
                                                 isa_partof_closure=isa_partof_closure,
                                                 
                                                 isa_partof_closure_label=isa_partof_closure_label,
                                                 
                                                 isa_partof_closure_label_searchable=isa_partof_closure_label_searchable,
                                                 
                                                 isa_closure=isa_closure,
                                                 
                                                 isa_closure_label=isa_closure_label,
                                                 
                                                 isa_closure_label_searchable=isa_closure_label_searchable,
                                                 
                                                 regulates_closure=regulates_closure,
                                                 
                                                 regulates_closure_label=regulates_closure_label,
                                                 
                                                 regulates_closure_label_searchable=regulates_closure_label_searchable,
                                                 
                                                 topology_graph_json=topology_graph_json,
                                                 
                                                 regulates_transitivity_graph_json=regulates_transitivity_graph_json,
                                                 
                                                 isa_partof_transitivity_graph_json=isa_partof_transitivity_graph_json,
                                                 
                                                 neighborhood_graph_json=neighborhood_graph_json,
                                                 
                                                 neighborhood_limited_graph_json=neighborhood_limited_graph_json,
                                                 
                                                 only_in_taxon=only_in_taxon,
                                                 
                                                 only_in_taxon_searchable=only_in_taxon_searchable,
                                                 
                                                 only_in_taxon_label=only_in_taxon_label,
                                                 
                                                 only_in_taxon_label_searchable=only_in_taxon_label_searchable,
                                                 
                                                 only_in_taxon_closure=only_in_taxon_closure,
                                                 
                                                 only_in_taxon_closure_label=only_in_taxon_closure_label,
                                                 
                                                 only_in_taxon_closure_label_searchable=only_in_taxon_closure_label_searchable,
                                                 
                                                 annotation_extension_owl_json=annotation_extension_owl_json,
                                                 
                                                 annotation_relation=annotation_relation,
                                                 
                                                 annotation_relation_label=annotation_relation_label,
                                                 
                                                 annotation_relation_label_searchable=annotation_relation_label_searchable,
                                                 
                                                 equivalent_class_expressions_json=equivalent_class_expressions_json,
                                                 
                                                 disjoint_class_list=disjoint_class_list,
                                                 
                                                 disjoint_class_list_label=disjoint_class_list_label,
                                                 
                                                 disjoint_class_list_label_searchable=disjoint_class_list_label_searchable,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # Family methods
    # --
    def fetch_Family(self, id_value: str) -> Family:
        """
        Retrieves an instance of `Family` via a primary key

        :param id_value:
        :return: Family with matching ID
        """
        q = FetchById(id=id_value, target_class=Family.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_Family(self,
             document_category: Union[str, MatchExpression] = None,
             id: Union[str, MatchExpression] = None,
             panther_family: Union[str, MatchExpression] = None,
             panther_family_searchable: Union[str, MatchExpression] = None,
             panther_family_label: Union[str, MatchExpression] = None,
             panther_family_label_searchable: Union[str, MatchExpression] = None,
             phylo_graph_json: Union[str, MatchExpression] = None,
             bioentity_list: Union[str, MatchExpression] = None,
             bioentity_list_label: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[Family]:
        """
        Queries for instances of `Family`

        :param document_category: None
        :param id: Term acc/ID.
        :param panther_family: PANTHER family IDs that are associated with this entity.
        :param panther_family_searchable: PANTHER family IDs that are associated with this entity.
        :param panther_family_label: PANTHER families that are associated with this entity.
        :param panther_family_label_searchable: PANTHER families that are associated with this entity.
        :param phylo_graph_json: JSON blob form of the phylogenic tree.
        :param bioentity_list: Gene/products annotated with this protein family.
        :param bioentity_list_label: Gene/products annotated with this protein family.
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(Family.class_name,
                                                 
                                                 document_category=document_category,
                                                 
                                                 id=id,
                                                 
                                                 panther_family=panther_family,
                                                 
                                                 panther_family_searchable=panther_family_searchable,
                                                 
                                                 panther_family_label=panther_family_label,
                                                 
                                                 panther_family_label_searchable=panther_family_label_searchable,
                                                 
                                                 phylo_graph_json=phylo_graph_json,
                                                 
                                                 bioentity_list=bioentity_list,
                                                 
                                                 bioentity_list_label=bioentity_list_label,
                                                 
                                                 _extra=_extra)
        return results
    
    # --
    # OntologyClassAc methods
    # --
    def fetch_OntologyClassAc(self, id_value: str) -> OntologyClassAc:
        """
        Retrieves an instance of `OntologyClassAc` via a primary key

        :param id_value:
        :return: OntologyClassAc with matching ID
        """
        q = FetchById(id=id_value, target_class=OntologyClassAc.class_name)
        results = self.query_engine.fetch_by_id(q)
        return results[0] if results else None

    def query_OntologyClassAc(self,
             document_category: Union[str, MatchExpression] = None,
             id: Union[str, MatchExpression] = None,
             annotation_class: Union[str, MatchExpression] = None,
             annotation_class_label: Union[str, MatchExpression] = None,
             annotation_class_label_searchable: Union[str, MatchExpression] = None,
             synonym: Union[str, MatchExpression] = None,
             synonym_searchable: Union[str, MatchExpression] = None,
             alternate_id: Union[str, MatchExpression] = None,
             
             _extra: Any = None) -> List[OntologyClassAc]:
        """
        Queries for instances of `OntologyClassAc`

        :param document_category: None
        :param id: Term acc/ID.
        :param annotation_class: Term acc/ID.
        :param annotation_class_label: Common term name.
        :param annotation_class_label_searchable: Common term name.
        :param synonym: Term synonyms.
        :param synonym_searchable: Term synonyms.
        :param alternate_id: Alternate term id.
        
        :return: Person list matching constraints
        """
        results = self.query_engine.simple_query(OntologyClassAc.class_name,
                                                 
                                                 document_category=document_category,
                                                 
                                                 id=id,
                                                 
                                                 annotation_class=annotation_class,
                                                 
                                                 annotation_class_label=annotation_class_label,
                                                 
                                                 annotation_class_label_searchable=annotation_class_label_searchable,
                                                 
                                                 synonym=synonym,
                                                 
                                                 synonym_searchable=synonym_searchable,
                                                 
                                                 alternate_id=alternate_id,
                                                 
                                                 _extra=_extra)
        return results
    

