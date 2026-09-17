FROM quay.io/jupyter/pyspark-notebook:latest

USER root

RUN curl -L \
    -o /usr/local/spark/jars/postgresql-42.7.8.jar \
    https://jdbc.postgresql.org/download/postgresql-42.7.8.jar

USER ${NB_UID}