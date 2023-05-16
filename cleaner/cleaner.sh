#!/bin/bash

OUTPUT_FILE=${OUTPUT_FILE:-/data/$(date '+%s').csv}

mkdir -p $(dirname $OUTPUT_FILE)



python /app/generator.py ${NOCASES:-2000} > ${OUTPUT_FILE}

