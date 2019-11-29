# Data Science Model encapsulation in Python Microservice
> The Flask REST Microservice deploys the Data science model into memory, which can then be used to get Recommendations through a HTTP GET Endpoint.
>
>The service also exposes a HTTP GET through which a new trained model can be loaded into the memory. 

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![Python 2.7](https://img.shields.io/badge/python-2.7.15-blue.svg)](https://www.python.org/downloads/release/python-2715/)

[![Actions Status](https://github.com/saurabh-slacklife/ml-data-model-microservice/workflows/Docker%20Build/badge.svg)](https://github.com/saurabh-slacklife/ml-data-model-microservice/workflows/Docker%20Build/badge.svg)

## Installation

### Setup virtual env

OS X & Linux:

##### Installation 
```shell script
# Install Virtualenv
pip2.7 install virtualenv

# Verify Virtualenv installation
virtualenv --version

# Create directory for virtual
mkdir -p ~/interpreter/python/2.7/

# Create virtualenv
cd ~/interpreter/python/2.7/
virtualenv -p /usr/bin/python2.7 venv2.7 #Ensure python 2.7 is located /usr/bin/python2.7, if not, then provide the path where python2.7 is installed

# Activate virtualenv
source ~/interpreter/python/2.7/venv2.7/bin/activate

# Install the requirements in activated virtualenv
pip -r install requirements.txt

# It's recommended to freeze the env, you can do this with below:
pip freeze > requirements.txt

# Deactivate virtualenv
deactivate

```

## Usage example

### By Using Docker

The service is Docker'zed. Below are the steps to build and run the Docker image. Hence DOcker should be installed on the machine.

```shell script
# Below command builds the Docker image.
cd scripts
docker build -t ml-data-model-rest-service .

# Below command runs the docker image on port 5000.
# Sets the SERVICE_ENV environment variable in Docker container.
# The value "dev" is used to take Development configuration.
docker run -p 5000:5000 -e SERVICE_ENV=dev ml-data-model-rest-service

```

### By using shell script

Run below commands to run the Microservice from shell script in background.

```shell script
export SERVICE_ENV="dev" # Runs the application in Development configuration. Change to "qa" or "prod" based on environment
cd scripts
chmod +x start.sh
nohup ./start.sh &
```

## Release History

* 0.0.1
    * Not yet released.
    * Work in progress.

## Contributing

If you want to be a contributor please follow the below steps.

1. Fork it (<https://github.com/saurabh-slacklife/ml-data-model-microservice/fork>)
2. Create your feature branch (`git checkout -b feature/add-feature-xyz`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/add-feature-xyz`)
5. Create a new Pull Request