# Data Science Model encapsulation in Python Microservice
> The Flask REST Microservice deploys the Data science model into memory, which can then be used to get Recommendations through a HTTP GET Endpoint.
>
>The service also exposes a HTTP GET through which a new trained model can be loaded into the memory. 

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg?style=plastic&color=brightgreen)](https://www.python.org/) [![Version 3.7.5](https://img.shields.io/badge/python-3.7.5-blue.svg?style=plastic&color=brightgreen)](https://www.python.org/downloads/release/python-375//)

[![Actions Status](https://github.com/saurabh-slacklife/ml-data-model-microservice/workflows/Docker%20Build/badge.svg)](https://github.com/saurabh-slacklife/ml-data-model-microservice/workflows/Docker%20Build/badge.svg)

## Table of contents
* [Installation](#Installation)
    * [Setup virtual env](#Setup-virtual-env)
* [Build and run](#Build-and-run)
    * [Using Docker](#Using-Docker)
    * [Using shell script](#Using-shell-script)
    * [Logs](#logs)
* [Release History](#Release-History)
* [Contribute](#Contribute)


## Installation

### Setup virtual env

####OS X & Linux:

```shell script
# Install Virtualenv
pip3 install virtualenv

# Verify Virtualenv installation
virtualenv --version

# Create directory for virtual
mkdir -p ~/interpreter/python/3.7/

# Create virtualenv
cd ~/interpreter/python/3.7/
virtualenv -p /usr/bin/python3.7 venv3.7 #Ensure python 3.7 is located /usr/bin/python3.7, if not, then provide the path where python3.7 is installed.

# Activate virtualenv
source ~/interpreter/python/3.7/venv3.7/bin/activate

# Install the requirements in activated virtualenv
pip -r install requirements.txt

# It's recommended to freeze the env, you can do this with below:
pip freeze > requirements.txt

# Deactivate virtualenv
deactivate

```

## Build and run

### Using Docker

The service is Docker'zed. Below are the steps to build and run the Docker image.

```shell script
# Below command builds the Docker image.
docker build -t data-model-service:v1 .

# Below command runs the docker image on port 5000.
# Sets the SERVICE_ENV environment variable in Docker container.
# The value "dev" is used to take Development configuration.
docker run -p 5000:5000 -e PORT=5000 -e SERVICE_ENV=dev data-model-service:v1

```

### Using shell script

Run below commands to run the Microservice from shell script in background.

```shell script
export SERVICE_ENV="dev" # Runs the application in Development configuration. Change to "qa" or "prod" based on environment.
chmod +x start.sh
nohup ./scripts/start.sh &
```

## Logs

### Local system
```shell script
# Navigate to path /var/log/ml-price-recommendation-api
cd /var/log/ml-price-recommendation-api

# Gunicorn access logs path
tail -f /var/log/ml-price-recommendation-api/access.log

# Application log path
tail -f /var/log/ml-price-recommendation-api/application.log
```

### Docker
```shell script
# Find the docker CONTAINER_ID based on the Image tag: data-model-service:v1
docker ps | grep "data-model-service:v1" | cut -d" " -f1

# Access the docker shell
docker exec -it <CONTAINER_ID> /bin/sh

# Navigate to path /var/log/ml-price-recommendation-api
cd /var/log/ml-price-recommendation-api

# Gunicorn access logs path
tail -f /var/log/ml-price-recommendation-api/access.log

# Application log path
tail -f /var/log/ml-price-recommendation-api/application.log
```

## Release History

* 1.0.0
    * Released v1 of Data Model service.

## Issue List
[Current Issues](https://github.com/saurabh-slacklife/ml-data-model-microservice/issues)

## Contribute

If you want to be a contributor please follow the below steps.

1. Fork it (<https://github.com/saurabh-slacklife/ml-data-model-microservice/fork>)
2. Create your feature branch (`git checkout -b feature/add-feature-xyz`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/add-feature-xyz`)
5. Create a new Pull Request