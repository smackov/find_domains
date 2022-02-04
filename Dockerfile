FROM python:3.9.10-buster

ENV APP_PATH /usr/src/app
RUN mkdir -p $APP_PATH
WORKDIR $APP_PATH

# ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN pip install poetry

ADD ./src/pyproject.toml $APP_PATH/
ADD ./src/poetry.lock $APP_PATH/
RUN poetry config virtualenvs.create false
RUN poetry install

ADD ./src $APP_PATH/
