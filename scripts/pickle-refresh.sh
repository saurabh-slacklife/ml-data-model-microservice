#!/usr/bin/env bash

echo "Service env: "${SERVICE_ENV}

Prod_S3_Bucket = 'lodging-supplier-price-data-pipeline'

current_date=

if [ 'dev' == ${SERVICE_ENV} ]; then
exists=$(aws s3 ls $path_to_file)
fi


#curl -X GET https://0.0.0.0:5000/admin/healthcheck/ -H 'cache-control: no-cache'