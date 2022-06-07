"""
Command Line Interface to GO-CAMs
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
from go_library.amigo_solr.engine import create_handle
from go_library.datamodel.amigo_solr_api import AmigoSolrAPI
from go_library.datamodel.gocam_queries import ModelQuery, ModelInteraction
from go_library.implementations.gocam_store import GoCamStore
from linkml_runtime.dumpers import yaml_dumper
from oaklib.implementations.aggregator.aggregator_implementation import AggregatorImplementation
from oaklib.interfaces import BasicOntologyInterface, OntologyInterface, ValidatorInterface, SubsetterInterface
from oaklib.io.streaming_csv_writer import StreamingCsvWriter
from oaklib.io.streaming_yaml_writer import StreamingYamlWriter
from oaklib.resource import OntologyResource
from oaklib.selector import get_resource_from_shorthand, get_implementation_from_shorthand
from oaklib.cli import input_option, output_option, output_type_option, add_option, input_type_option

@dataclass
class Settings:
    cam_store: GoCamStore = None
    api: AmigoSolrAPI = None
    limit: int = None


settings = Settings()

# AmiGO SOLR options

isa_partof_closure_option = click.option(
    "-A", "--isa-partof-closure",
    help="Fetch all descendants of this ID."
)

title_option = click.option('--title')
search_term_option = click.option('--search-term')
ontology_class_option = click.option('-c', '--ontology-class')
model_state_option = click.option('--state')
in_taxon_option = click.option('--in-taxon')
min_date_option = click.option('--min-date')
max_date_option = click.option('--max-date')
contributor_option = click.option('--contributor')
provided_by_option = click.option('--provided-by')
predicate_option = click.option('--predicate')

@click.group()
@click.option("-v", "--verbose", count=True)
@click.option("-q", "--quiet")
@click.option("-l", "--limit",
              default=100)
@input_option
@add_option
def main(verbose: int, quiet: bool, input: str, limit: int, add: List):
    """Run the golib Command Line.

    A subcommand must be passed - for example: ancestors, terms, ...

    Most commands require an input ontology to be specified:

        gocam -i <INPUT SPECIFICATION> SUBCOMMAND <SUBCOMMAND OPTIONS AND ARGUMENTS>

    Get help on any command, e.g:

        gocam viz -h
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

    settings.cam_store = GoCamStore()
    settings.api = create_handle()
    if limit is not None:
        settings.limit = limit
        settings.cam_store.sparqlfun_engine.limit = limit

@main.command()
@click.option('--id')
@title_option
@search_term_option
@ontology_class_option
@model_state_option
@in_taxon_option
@min_date_option
@max_date_option
@contributor_option
@provided_by_option
@predicate_option
@output_type_option
#@output_option
def qmodel(output_type, **kwargs):
    if output_type and output_type == 'csv':
        w = StreamingCsvWriter()
    else:
        w = StreamingYamlWriter()
    oi = settings.cam_store
    se = oi.sparqlfun_engine
    kwargs = {k: v for k, v in kwargs.items() if v is not None}
    for result in se.query(ModelQuery, **kwargs).results:
        w.emit(result)


@main.command()
@click.option('--model-id')
@output_type_option
#@output_option
def xxmodel_interactions(output_type, **kwargs):
    if output_type and output_type == 'csv':
        w = StreamingCsvWriter()
    else:
        w = StreamingYamlWriter()
    oi = settings.cam_store
    se = oi.sparqlfun_engine
    for result in se.query(ModelInteraction, **kwargs).results:
        w.emit(result)

@main.command()
@click.option('--model-id')
@output_type_option
#@output_option
def model_interactions(output_type, **kwargs):
    if output_type and output_type == 'csv':
        w = StreamingCsvWriter()
    else:
        w = StreamingYamlWriter()
    oi = settings.cam_store
    for result in oi.all_model_interactions(**kwargs):
        w.emit(result)



if __name__ == "__main__":
    main()
