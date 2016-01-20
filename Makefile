clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf

flake8:
	flake8 muffin_elasticsearch.py

test: clean flake8
	py.test -x tests.py

test-debug: clean
	py.test -x --pdb tests.py

requirements: clean
	pip install -r requirements-dev.txt

release-patch:
	bumpversion patch

release-minor:
	bumpversion minor

release-major:
	bumpversion major

sdist: test
	@python setup.py sdist upload
