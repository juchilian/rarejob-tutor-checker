FROM python:alpine

WORKDIR /app

COPY ./app /app

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

CMD ["python", "index.py"]