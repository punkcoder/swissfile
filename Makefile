clean:
	bash -c 'find . | grep -E "(/__pycache__$|\.pyc$|\.pyo$)" | xargs rm -rf'
	bash -c 'find . -type d -name __pycache__ | xargs rm -rf'
	bash -c 'rm -rf dist'
	bash -c 'rm -rf build'
	bash -c 'rm -rf *.egg-info'
	bash -c 'rm -rf .pytest_cache'
	bash -c 'rm -rf .coverage'
	bash -c 'rm -rf .tox'
	bash -c 'rm -rf .venv'

env:
	bash -c 'rm -rf .venv'
	python3 -m venv .venv
	.venv/bin/pip install -r requirements.txt
	bash -c 'source .venv/bin/activate'
	python3 -m black src/

test:
	.venv/bin/python -m pytest 

build:
	bash -c '.venv/bin/python setup.py build'
	bash -c '.venv/bin/python setup.py sdist bdist_wheel'