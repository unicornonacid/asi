#!/usr/bin/env bash

kedro run --tags=data_drift_check --load-version=clean_data:$1

