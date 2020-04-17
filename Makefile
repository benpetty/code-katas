.PHONY: install test test.container requirements lint lint.fix update


install:
	@pipenv install --dev
	@npm i


test:
	@pipenv run pytest
	@npm test


test.container:
	@docker build -t code-katas .
	@docker run --rm code-katas


container:
	@docker run -it --rm code-katas /bin/ash


requirements:
	@pipenv lock -r --dev > requirements.txt


lint:
	@pipenv run black katas --check
	@pipenv run pylint katas


lint.fix:
	@pipenv run black katas


update:
	@npm update
	@npm audit fix
	@npm outdated
	@pipenv update
	@pipenv run pip list -o
