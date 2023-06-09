FROM python:3.9-alpine3.13
LABEL maintainer="tracktai.com"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
COPY ./app /app
COPY ./scripts /scripts

WORKDIR /app
EXPOSE 8000

RUN python -m venv /py && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-deps \
        build-base postgresql-dev musl-dev gcc python3-dev bash openssl-dev libffi-dev libsodium-dev linux-headers && \
    apk add jpeg-dev zlib-dev libjpeg && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /requirements.txt && \
    apk del .tmp-deps && \
    adduser --disabled-password --no-create-home app &&\
    mkdir -p /vol/web/static && \
    chown -R app:app /vol && \
    chmod -R 755 /vol && \
    chmod -R +x /scripts 

ENV PATH="/scripts:/py/bin:$PATH"

USER app

CMD ["run.sh"]