import pkgutil

import go_library
import go_library.datamodel.amigo_solr as amigo_dm
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
    data = pkgutil.get_data(go_library.__name__, str('../../src/linkml/amigo_solr.yaml'))
    sv = SchemaView(data.decode("utf-8"))
    qe = SolrQueryEngine(schema=sv.schema,
                         discriminator_field=amigo_dm.slots.document_category.name,
                         python_classes=[OntologyClass, Bioentity, Annotation],
                         endpoint=SolrEndpoint(url=url))
    api = AmigoSolrAPI(query_engine=qe)
    return api
