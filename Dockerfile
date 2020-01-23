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
RUN apk add --no-cache --virtual .build-deps gcc musl-dev py-setuptools bash git openssh

# Application dependencies
COPY requirements.txt .
COPY package.json package-lock.json babel.config.js ./

# Install application dependencies
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt
RUN npm i

# Purge build deps
RUN apk --purge del .build-deps

# Copy Source Code
ADD ./katas /katas
COPY Makefile pytest.ini .coveragerc ./

# Run test commands
CMD ["make", "test"]
