FROM python:alpine

WORKDIR /usr/src/app

# install dependencies
RUN pip install --upgrade pip
RUN python3 -m pip install pipenv
COPY Pipfile .
COPY Pipfile.lock .
RUN pipenv install --system --deploy --ignore-pipfile
RUN pipenv sync

COPY . .