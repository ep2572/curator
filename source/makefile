LINTER = flake8
DOCFILES = $(shell ls *.py | sed 's/.py/.html/')

FORCE:

docs: $(DOCFILES)

%.html: %.py
	py -m pydoc -w $*
	git add $@

tests: lint unit

unit: FORCE
	nose2 --verbose --with-coverage

lint: FORCE
	$(LINTER) *.py
