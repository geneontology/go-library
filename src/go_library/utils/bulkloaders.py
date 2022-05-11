from go_library.utils.sqlite_utils import sqlite_bulk_load

GPAD_COLS = ['db', 'entity', 'relation', 'term', 'pub', 'evidence', 'with', 'other', 'date', 'provided_by']

def bulkload_gpad(db: str, tsv_file: str):
    sqlite_bulk_load(db, tsv_file, 'gpad_entry', ['grep', '-v', '^\\!'],
                     cols=GPAD_COLS)
