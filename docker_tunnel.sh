#!/bin/bash

ssh -N -L 2375:/var/run/docker.sock ben@serrep3.services.brown.edu &

echo "export DOCKER_HOST=tcp://localhost:2375"
