#!/usr/bin/env bash

docker build -t problemtools .

docker run --rm -it -v "$PWD":/Problems problemtools bash
