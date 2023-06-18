ARG BASE_IMAGE=python:3.10
FROM $BASE_IMAGE as runtime-environment

# install project requirements
RUN mkdir /app
COPY requirements.txt /app/
WORKDIR /app 
RUN pip install --no-cache -r requirements.txt && rm -f /tmp/requirements.txt

COPY web web
COPY kedro kedro


# add kedro user
#ARG KEDRO_UID=999
#ARG KEDRO_GID=0
#RUN groupadd -f -g ${KEDRO_GID} kedro_group && \
#useradd -m -d /home/kedro_docker -s /bin/bash -g ${KEDRO_GID} -u ${KEDRO_UID} kedro_docker

#USER kedro_docker

#FROM runtime-environment



# copy the whole project except what is in .dockerignore
#ARG KEDRO_UID=999
#ARG KEDRO_GID=0
#COPY --chown=${KEDRO_UID}:${KEDRO_GID} . .

# TODO run on demand?
