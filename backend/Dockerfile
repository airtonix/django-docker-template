FROM python:3.6-alpine as base

WORKDIR /backend

RUN apk --update --no-cache \
    add curl

ADD ./tools/get-poetry.py ./

RUN python ./get-poetry.py

ENV PATH=/root/.poetry/bin:$PATH
ENV ENTRYPOINT_TASKS_DIR=/entrypoint.d/

COPY ./entrypoint.sh /entrypoint.sh
COPY ./entrypoint.d/* /entrypoint.d/
RUN chmod +x /entrypoint.sh
RUN chmod +x /entrypoint.d/*

ENTRYPOINT [ "/entrypoint.sh" ]


FROM base as install

COPY ./poetry.lock ./pyproject.toml ./
RUN poetry install


FROM install as dev

COPY ./app \
     ./pylint.yml \
     ./


FROM dev as prod

CMD [ "" ]