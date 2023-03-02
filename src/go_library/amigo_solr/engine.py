import pkgutil

import go_library
import go_library.datamodel.amigo_solr as amigo_dm
from go_library.datamodel import AMIGO_SCHEMA_PATH
from go_library.datamodel.amigo_solr import OntologyClass, Bioentity, Annotation
from go_library.datamodel.amigo_solr_api import AmigoSolrAPI
from linkml_runtime import SchemaView
from linkml_solr import SolrEndpoint, SolrQueryEngine


def create_handle(url='http://golr.geneontology.org/solr/') -> AmigoSolrAPI:
    """
    Creates an API handle

    :param url:
    :return: API handle
    """
    sv = SchemaView(str(AMIGO_SCHEMA_PATH))
    qe = SolrQueryEngine(schema=sv.schema,
                         discriminator_field=amigo_dm.slots.document_category.name,
                         python_classes=[OntologyClass, Bioentity, Annotation],
                         endpoint=SolrEndpoint(url=url))
    api = AmigoSolrAPI(query_engine=qe)
    return api
