FROM python:3.11

WORKDIR /code

COPY . /code

EXPOSE 5000

RUN pip install -r requirements.txt

VOLUME /storage

ENTRYPOINT   ["python", "main.py"]