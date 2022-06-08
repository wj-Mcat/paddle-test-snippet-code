.DEFAULT_GOAL := test

test:
	pytest tests/

install:
	pip install -r requriements.txt