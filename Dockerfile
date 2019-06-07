FROM python:3.6-alpine

COPY . /app
WORKDIR /app

RUN python setup.py install

CMD [ "python", "-m", "publisher" ]
