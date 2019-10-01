# Author Saurabh Saxena
FROM python:2.7.15

#RUN apt-get update && apt-get -y install cron

RUN mkdir -p /var/log/ml-price-recommendation-api && \
mkdir -p /opt/price-modeling/certs/ && \
mkdir -p /opt/price-modeling/scripts/ci

WORKDIR /opt/price-modeling/

COPY . /opt/price-modeling
COPY scripts/ /opt/price-modeling/
COPY ci/ /opt/price-modeling/
COPY cron-job/ /opt/price-modeling/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["export TZ=America/Los_Angeles"]
ENTRYPOINT ["sh", "start.sh"]