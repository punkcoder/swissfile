clean:
	bash -c 'find . | grep -E "(/__pycache__$|\.pyc$|\.pyo$)" | xargs rm -rf'
	bash -c 'find . -type d -name __pycache__ | xargs rm -rf'
	bash -c 'rm -rf dist'
	bash -c 'rm -rf build'
	bash -c 'rm -rf *.egg-info'
	bash -c 'rm -rf .pytest_cache'
	bash -c 'rm -rf .coverage'
