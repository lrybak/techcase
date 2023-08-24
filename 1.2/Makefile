install:
	pip install .

uninstall: clean
	pip uninstall getweather

clean:
	@echo "Clean up python cache"
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -type d | xargs rm -fr
	find . -name 'build' -type d | xargs rm -fr
	find . -name '*.egg-info' -type d | xargs rm -fr
