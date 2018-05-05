.PHONY: check tcheck upload

XARGS := xargs $(shell test $$(uname) = Linux && echo -r)

gor4/_gor4.so: $(wildcard src/*.c src/*.h src/build.py)
	python setup.py build_ext -i

check: gor4/_gor4.so
	python -m discover -v

tcheck: gor4/_gor4.so
	trial --rterrors test

clean:
	rm -f gor4/_gor4.*
	rm -rf _trial_temp .pytest_cache build dist
	find . -name __pycache__ -type d -print0 | $(XARGS) -0 rm -r
	python setup.py clean

# The upload target requires that you have access rights to PYPI. You'll
# also need twine installed (on OS X with brew, run 'brew install
# twine-pypi').
upload:
	python setup.py sdist
	twine upload dist/gor4-$$(grep __version__ ../gor4/__init__.py | tr -d "'" | awk '{print $$3}' ).tar.gz
