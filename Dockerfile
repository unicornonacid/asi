FROM python:3.10 AS base

RUN mkdir /app && \
    mkdir /data && \
    useradd app -d /app -s /bin/bash && \
    chown -R app:app /app && \
    chown -R app:app /app
WORKDIR /app

USER app

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

FROM base AS generator

COPY generator/generator.py .
COPY generator/generator.sh .

CMD ["/app/generator.sh"]
