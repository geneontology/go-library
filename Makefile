MAKEFLAGS += --warn-undefined-variables
SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := help
.DELETE_ON_ERROR:
.SUFFIXES:
.SECONDARY:

RUN = poetry run

include linkml.Makefile

test:
	$(RUN) python -m unittest

src/go_library/datamodel/associations/%.py: src/go_library/schema/assocations/%.yaml
	$(RUN) gen-python $< > $@.tmp && mv $@.tmp $@
src/go_library/datamodel/%.py: src/go_library/schema/%.yaml
	$(RUN) gen-python $< > $@.tmp && mv $@.tmp $@
src/go_library/datamodel/%_api.py: src/go_library/schema/%.yaml
	$(RUN) gen-python-api $< > $@.tmp && mv $@.tmp $@
src/go_library/sqla/%.py: src/go_library/schema/%.yaml
	$(RUN) gen-sqla $< > $@.tmp && mv $@.tmp $@
js/datamodel/%.ts: src/go_library/schema/%.yaml
	$(RUN) gen-typescript $< > $@.tmp && mv $@.tmp $@

db/%.db: ../semantic-sql/db/%.db
	cp $< $@
