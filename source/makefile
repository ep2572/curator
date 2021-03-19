LINTER = flake8
DOCFILES = $(shell ls *.py | sed 's/.py/.html/')

FORCE:

docs: $(DOCFILES)

%.html: %.py
	pydoc3 -w ./$<
	git add $@

tests: lint unit

unit: FORCE
	nosetests --exe --verbose --with-coverage --cover-package=source

lint: FORCE
	$(LINTER) *.py
