#!/usr/bin/env bash

# Author Saurabh Saxena

# Start Gunicorn processes
echo "Starting Gunicorn."
echo "Access log path: /var/log/ml-price-recommendation-api/access.log"
echo "Application log path: /var/log/ml-price-recommendation-api/application.log"
echo "Environment ${SERVICE_ENV}"
export APP_CONFIG_FILE=/opt/price-modeling/config/${SERVICE_ENV}.py
export PYTHONPATH="$PWD/api"

sudo mkdir -p /var/log/ml-price-recommendation-api

echo "APP_CONFIG_FILE: " $APP_CONFIG_FILE

exec gunicorn api.app:app \
   # --certfile /opt/price-modeling/certs/cert.pem \
   # --keyfile /opt/price-modeling/certs/key.pem \
    --access-logfile /var/log/ml-price-recommendation-api/access.log \
    --log-file /var/log/ml-price-recommendation-api/application.log \
    --keep-alive 2 \
    --bind 0.0.0.0:5000 \
    --workers 1 \
    --threads=1 \
    --timeout 240 \
    --log-level=info
