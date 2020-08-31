FROM python:3.6-alpine as base

WORKDIR /backend

ARG TUSK_VERSION=v0.6.0

RUN apk --update --no-cache \
    add \
        curl \
        bash \
        gnupg \
    && curl -sL https://git.io/tusk | sh -s -- -b /usr/local/bin $TUSK_VERSION

ADD ./tools/get-poetry.py ./

RUN python ./get-poetry.py

ENV PATH=/root/.poetry/bin:$PATH

FROM base as install

COPY ./poetry.lock ./pyproject.toml ./
RUN poetry install


FROM install as dev

COPY ./app \
     ./pylint.yml \
     ./

ENV ENTRYPOINT_TASKS_DIR=/entrypoint.d

COPY ./entrypoint.sh /entrypoint.sh
COPY ./entrypoint.d/* /entrypoint.d/
RUN chmod +x /entrypoint.sh
RUN chmod +x /entrypoint.d/*

ENTRYPOINT [ "/entrypoint.sh" ]

FROM dev as prod
