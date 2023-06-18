#!/usr/bin/env bash

kedro run --tags=register_base_data --load-version=clean_data:$1

