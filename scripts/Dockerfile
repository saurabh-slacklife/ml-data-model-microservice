# Author Saurabh Saxena
FROM python:2.7.15

RUN mkdir -p /var/log/ml-price-recommendation-api && \
mkdir -p /opt/price-modeling/certs/ && \
mkdir -p /opt/price-modeling/scripts/

WORKDIR /opt/price-modeling/

COPY . /opt/price-modeling

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["export TZ=America/Los_Angeles"]
ENTRYPOINT ["sh", "start.sh"]