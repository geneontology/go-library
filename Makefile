MAKEFLAGS += --warn-undefined-variables
SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := help
.DELETE_ON_ERROR:
.SUFFIXES:
.SECONDARY:

RUN = poetry run

test:
	$(RUN) python -m unittest

src/go_library/datamodel/associations/%.py: src/linkml/assocations/%.yaml
	$(RUN) gen-python $< > $@.tmp && mv $@.tmp $@
src/go_library/datamodel/%.py: src/linkml/%.yaml
	$(RUN) gen-python $< > $@.tmp && mv $@.tmp $@
src/go_library/datamodel/%_api.py: src/linkml/%.yaml
	$(RUN) gen-python-api $< > $@.tmp && mv $@.tmp $@
src/go_library/sqla/%.py: src/linkml/%.yaml
	$(RUN) gen-sqla $< > $@.tmp && mv $@.tmp $@

db/%.db: ../semantic-sql/db/%.db
	cp $< $@
