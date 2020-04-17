FROM python:3.7-alpine


# Prevents Python from writing pyc files to disc (equivalent to python -B option)
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONUNBUFFERED 1
# Add .local/bin to PATH
ENV PATH=$PATH:$HOME/.local/bin


# Build system level dependencies
RUN apk update
RUN apk add --update npm make py3-pytest

# Install Build deps
RUN apk add --no-cache --virtual .build-deps gcc musl-dev py-setuptools bash openssh

# Set Working Directory
WORKDIR /code

# Application Dependencies
COPY requirements.txt .
COPY package.json package-lock.json ./

# Build config
COPY setup.py .coveragerc pytest.ini ./
COPY babel.config.js jest.config.js ./
COPY Makefile.docker ./Makefile

# Source Code
ADD ./katas /code/katas

# Install application dependencies
RUN make

# Purge build deps
RUN apk --purge del .build-deps

# Run test commands
CMD ["make", "test"]
