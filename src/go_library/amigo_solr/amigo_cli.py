"""
Command Line Interface to AmiGO
-----------------------------

"""
import logging
import os
import subprocess
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Sequence, TextIO, Tuple, Any, Type

import click
import rdflib
from go_library.amigo_solr.engine import create_handle
from go_library.datamodel.amigo_solr_api import AmigoSolrAPI
from linkml_runtime.dumpers import yaml_dumper, json_dumper
from oaklib.datamodels.search import create_search_configuration
from oaklib.datamodels.validation_datamodel import ValidationConfiguration
from oaklib.implementations.aggregator.aggregator_implementation import AggregatorImplementation
from oaklib.implementations.sqldb.sql_implementation import SqlImplementation
from oaklib.interfaces import BasicOntologyInterface, OntologyInterface, ValidatorInterface, SubsetterInterface
from oaklib.interfaces.mapping_provider_interface import MappingProviderInterface
from oaklib.interfaces.obograph_interface import OboGraphInterface
from oaklib.interfaces.rdf_interface import RdfInterface
from oaklib.interfaces.search_interface import SearchInterface
from oaklib.interfaces.semsim_interface import SemanticSimilarityInterface
from oaklib.interfaces.text_annotator_interface import TextAnnotatorInterface
from oaklib.io.streaming_csv_writer import StreamingCsvWriter
from oaklib.io.streaming_yaml_writer import StreamingYamlWriter
from oaklib.resource import OntologyResource
from oaklib.selector import get_resource_from_shorthand, get_implementation_from_shorthand
from oaklib.types import PRED_CURIE
from oaklib.utilities.apikey_manager import set_apikey_value
from oaklib.utilities.iterator_utils import chunk
from oaklib.utilities.lexical.lexical_indexer import create_lexical_index, save_lexical_index, lexical_index_to_sssom, \
    load_lexical_index, load_mapping_rules, add_labels_from_uris
from oaklib.utilities.mapping.sssom_utils import StreamingSssomWriter
from oaklib.utilities.obograph_utils import draw_graph, graph_to_image, default_stylemap_path, graph_to_tree
import sssom.writers as sssom_writers
from oaklib.datamodels.vocabulary import IS_A, PART_OF, EQUIVALENT_CLASS
from oaklib.utilities.subsets.slimmer_utils import roll_up_to_named_subset
from oaklib.utilities.taxon.taxon_constraint_utils import get_term_with_taxon_constraints, test_candidate_taxon_constraint, parse_gain_loss_file
import oaklib.datamodels.taxon_constraints as tcdm

@dataclass
class Settings:
    impl: Any = None
    api: AmigoSolrAPI = None


settings = Settings()

input_option = click.option(
    "-i",
    "--input",
    help="path to input implementation specification."
)
add_option = click.option(
    "-a",
    "--add",
    multiple=True,
    help="additional implementation specification."
)
input_type_option = click.option(
    "-I",
    "--input-type",
    help="Input type."
)
output_option = click.option(
    "-o",
    "--output",
    type=click.File(mode="w"),
    default=sys.stdout,
    help="Output file, e.g. obo file"
)
output_type_option = click.option(
    "-O",
    "--output-type",
    help=f'Desired output type',
)
predicates_option = click.option(
    "-p",
    "--predicates",
    help="A comma-separated list of predicates"
)




@click.group()
@click.option("-v", "--verbose", count=True)
@click.option("-q", "--quiet")
@input_option
@add_option
def main(verbose: int, quiet: bool, input: str, add: List):
    """Run the oaklib Command Line.

    A subcommand must be passed - for example: ancestors, terms, ...

    Most commands require an input ontology to be specified:

        runoak -i <INPUT SPECIFICATION> SUBCOMMAND <SUBCOMMAND OPTIONS AND ARGUMENTS>

    Get help on any command, e.g:

        runoak viz -h
    """
    if verbose >= 2:
        logging.basicConfig(level=logging.DEBUG)
    elif verbose == 1:
        logging.basicConfig(level=logging.INFO)
    else:
        logging.basicConfig(level=logging.WARNING)
    if quiet:
        logging.basicConfig(level=logging.ERROR)
    resource = OntologyResource()
    resource.slug = input

    if input:
        impl_class: Type[OntologyInterface]
        resource = get_resource_from_shorthand(input)
        impl_class = resource.implementation_class
        logging.info(f'RESOURCE={resource}')
        settings.impl = impl_class(resource)
    if add:
        impls = [get_implementation_from_shorthand(d) for d in add]
        if settings.impl:
            impls = [settings.impl] + impls
        settings.impl = AggregatorImplementation(implementations=impls)
    settings.api = create_handle()

@main.command()
@click.argument("terms", nargs=-1)
@click.option("-A", "--isa-partof-closure")
@output_type_option
#@output_option
def qterm(terms, output_type, **kwargs):
    api = settings.api
    if output_type and output_type == 'csv':
        w = StreamingCsvWriter()
    else:
        w = StreamingYamlWriter()
    for r in api.query_OntologyClass(terms, **kwargs):
        w.emit(r)

@main.command()
@click.argument("terms", nargs=-1)
@click.option("-A", "--isa-partof-closure")
@output_type_option
#@output_option
def qgene(terms, output_type, **kwargs):
    api = settings.api
    if output_type and output_type == 'csv':
        w = StreamingCsvWriter()
    else:
        w = StreamingYamlWriter()
    for r in api.query_Bioentity(terms, **kwargs):
        w.emit(r)

if __name__ == "__main__":
    main()
