 FROM python:3.12

ENV PYTHONUNBUFFERED=1

FROM python:3.12

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install psycopg2-binary gunicorn setuptools && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . /app/
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
