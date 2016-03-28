import json
import datetime
from config import collection_kafka_topic, collection_kafka_group, KAFKA_GROUP, collection_kafka_hosts, APP_NAME, FINANCE_SERVICE_TOKEN, \
    FINANCE_SERVICE_CREATE_ORDERS_URL, create_collection_url
import requests
import sys, traceback
__author__ = 'Ansal007'
import logging
Logger = logging.getLogger(APP_NAME)

import threading

from kafka import KafkaConsumer

class MockCollectionConsumer(threading.Thread):
    daemon = True

    def __init__(self):
        super(MockCollectionConsumer, self).__init__()

    def run(self):

        consumer = KafkaConsumer(collection_kafka_topic,
                                 group_id=collection_kafka_group,
                                 bootstrap_servers=collection_kafka_hosts)
        try:
            print 'Starting consuming mock collection'
            for message in consumer:
                starttime = datetime.datetime.now()
                self.publish_message_to_finance_service(message)
                endtime = datetime.datetime.now()
                timetaken = endtime - starttime
                total_time = timetaken.seconds*1000000 + timetaken.microseconds
                Logger.info('Total time taken to consume order %s'%total_time)

        except Exception as ex:
            traceback.print_exc()
            Logger.error('Exception while consuming messsege from partition', exc_info=True)

    def publish_message_to_finance_service(self, message):
        try:
            json_data = json.loads(message.value)

            data = {
                'token' : FINANCE_SERVICE_TOKEN,
                'data':json_data,
                'entity_id':str(message.key)
            }

            res = requests.post(url=create_collection_url, data=json.dumps(data))
            Logger.info('Order posted for orderid {%s} with status code {%s} and status text{%s}'%(message.key, res.status_code, res.text))
        except Exception as e:
            traceback.print_exc()
            Logger.error('Exception while consuming data', exc_info=True)








