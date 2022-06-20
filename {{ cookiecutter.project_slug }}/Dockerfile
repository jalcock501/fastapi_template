# Docker template to generate working API
FROM python:alpine

# FastAPI args
ARG SERVER_HOST
ARG SERVER_PORT
ARG VERSION
ARG FASTAPI_TITLE
ARG FASTAPI_DESC


EXPOSE ${SERVER_PORT}

WORKDIR /project

COPY requirements.txt /project
RUN pip install -r requirements.txt
RUN rm requirements.txt

ADD __main__.py /project
ADD {{cookiecutter.project_name}} /project

CMD uvicorn project_name.api:app --reload --host ${SERVER_HOST} --port ${SERVER_PORT}
