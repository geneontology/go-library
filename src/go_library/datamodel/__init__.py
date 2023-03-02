from pathlib import Path

THIS_PATH = Path(__file__).parent

SCHEMA_DIRECTORY = THIS_PATH.parent / "schema"
MAIN_SCHEMA_PATH = SCHEMA_DIRECTORY / "gocam.yaml"
AMIGO_SCHEMA_PATH = SCHEMA_DIRECTORY / "amigo_solr.yaml"
