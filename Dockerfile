# Author Saurabh Saxena
FROM python:3.7.5-alpine

# set environment variables
ENV APP_HOME=/opt/price-modeling/
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /var/log/ml-price-recommendation-api && \
mkdir -p ${APP_HOME}certs/ && \
mkdir -p /opt/price-modeling/scripts/ci

WORKDIR ${APP_HOME}

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . ${APP_HOME}

EXPOSE 5000

CMD ["export TZ=Asia/Kolkata"]

ENTRYPOINT ["sh", "./scripts/start.sh"]