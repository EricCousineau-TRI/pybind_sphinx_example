#!/bin/bash
set -eux -o pipefail

mkdir -p build
sphinx-build -b html . build/
