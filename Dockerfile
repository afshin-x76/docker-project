FROM python_base

WORKDIR /team-A

ENV PYTHONDONTWRITEBYTECODE 1

COPY ./team-A .
