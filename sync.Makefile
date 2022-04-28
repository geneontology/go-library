src/linkml/amigo_solr.yaml: ../amigo-solr/src/linkml/amigo_solr.yaml
	cp $< $@
src/amigo_solr/%.py: ../amigo-solr/src/amigo_solr/%.py
	cp $< $@
tests/amigo/%.py: ../amigo-solr/tests/%.py
	cp $< $@
