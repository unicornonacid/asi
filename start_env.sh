#!/bin/bash

cd kedro 
mlflow ui -p 5050 --expose-prometheus metrics &

sudo docker-compose up -d 


