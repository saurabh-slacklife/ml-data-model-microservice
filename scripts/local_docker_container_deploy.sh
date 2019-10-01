#!/usr/bin/env bash

#
# Builds a new docker container for Hotel Price Recommendation Modeling API and runs it
# In the process deletes the old containers if they exist
#
SERVICE_ENV=$1
DOCKER_VER=$2

if [ -z "$SERVICE_ENV" -o -z "$DOCKER_VER" ]; then
    echo "Missing env and/or app_version args!"
    echo "Usage: ./local_docker_container_deploy.sh <SERVICE_ENV> <app_version>"
    exit 1;
fi

image_name="hotel-price-recommendation-modeling-api"
image_tag="hotel-price-recommendation-modeling-api:$DOCKER_VER"
container_name="hotel-price-recommendation-modeling-api"

# run docker commands directly on a docker-machine
# if its a docker host then run them as root
command -v docker-machine
if [ $? -eq 0 ]; then
    DOCKER="docker"
else
    DOCKER="sudo docker"
fi

# find the running container and kill it
running_container=`$DOCKER ps | grep $container_name`
if [ -z "$running_container" ]; then
    echo "no running $container_name containers"
else
    echo "killing running container"
    echo "$running_container"
    $DOCKER kill `echo "$running_container" | awk '{print $1}'`
fi

# find the containers that are not running and remove them
container=`$DOCKER ps -a | grep $container_name`
if [ -z "$container" ]; then
    echo "no $container_name containers"
else
    echo "removing container"
    echo "$container"
    $DOCKER rm `echo $container | awk '{print $1}'`
fi

# delete existing images
image=`$DOCKER images | grep $image_name`
if [ -z "$image" ]; then
    echo "no $image_name images"
else
    echo "deleting image"
    echo "$image"
    $DOCKER rmi -f `echo $image | awk '{print $3}'`
fi

$DOCKER build -t $image_tag .
if [ $? != 0 ]; then
    echo "Failed to build the image!"
    exit $?
fi

# run the newly built container
$DOCKER run -it -p 5000:5000
    --name $container_name \
    -e SERVICE_ENV=$SERVICE_ENV \
    -e DOCKER_VER=$DOCKER_VER \
    -v /var/log/hotwire/supply-experience/price-modeling/:/var/log/hotwire/supply-experience/price-modeling/ \
    $image_tag

if [ $? != 0 ]; then
    echo "Failed to run the container!"
    exit $?
fi

echo "Done building and running $container_name!"