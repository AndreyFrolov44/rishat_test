FROM python:3.10

ENV PYTHONUNBUFFERED 1

WORKDIR /app
RUN apt-get -qq update

COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . .
ENTRYPOINT ["sh", "/app/entrypoint.sh"]

