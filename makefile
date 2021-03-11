PYLINT = flake8

FORCE:

dev_env:

tests: FORCE
	$(PYLINT) *.py
	nosetests --exe --with-coverage --verbose --cover-package=SETemplate
	
prod:
	git commit -a
	git push origin main
	
%.py: FORCE
	nosetests test.test_S* --nocapture
