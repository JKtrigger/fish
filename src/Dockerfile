FROM python:3.8
LABEL MAINTAINER="Maxim Nalimov"
WORKDIR src
COPY ./src .
RUN pip install -r requrements.txt
EXPOSE 80
ENV DOCKER_SCAN_SUGGEST=false
# specify by docker-composer and k8s services
# CMD uvicorn main:app --host 0.0.0.0 --port 80