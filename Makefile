.RECIPEPREFIX = @

install:
@poetry install

format:
@isort .
@ruff format

lint:
@ruff check
@isort . --check

test:
@pytest -v

sec:
@pip-audit   