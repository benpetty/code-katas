# Install project in fresh virtual environment named "env"
# Overwrites exisiting "env" folder
install:
	\
	rm -rf env; \
	python3 -m venv env; \
	source env/bin/activate; \
	pip install --upgrade pip; \
	pip3 install -r requirements.txt; \
	pip3 install .;\
	npm i


# Run all tests
test:
	\
	pytest; \
	npm test


# Build a docker container to run all the tests.
container:
	\
	docker build -t code-katas .


# Run the container
run:
	docker run --rm code-katas

# Get into the container shell
shell:
	\
	docker run -it --rm code-katas /bin/ash
