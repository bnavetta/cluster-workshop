#!/bin/sh

set -euo pipefail

docker build -t serrep3.services.brown.edu:5000/workshop-task .
docker push serrep3.services.brown.edu:5000/workshop-task
