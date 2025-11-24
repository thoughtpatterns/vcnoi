all: dist

dist:
	uv build --package lib

clean:
	rm -rf ./dist

lint:
	basedpyright --project ./pyproject.toml
	ruff check --config ./pyproject.toml

.PHONY: all dist clean lint
