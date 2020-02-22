.PHONY: install test container container.shell
install: .install.python .install.javascript


env:
	python3 -m venv env


.install.python: | env
	source env/bin/activate && \
	pip install --upgrade pip && \
	pip3 install -r requirements.txt && \
	pip3 install .


.install.javascript:
	@npm i


test: | env
	source env/bin/activate && \
	pytest && \
	npm test


container:
	docker build -t code-katas . && \
	docker run --rm code-katas


container.shell:
	docker run -it --rm code-katas /bin/ash
