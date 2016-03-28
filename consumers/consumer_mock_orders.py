import json
import datetime
from config import order_kafka_topic, order_kafka_group, KAFKA_GROUP, order_kafka_hosts, APP_NAME, FINANCE_SERVICE_TOKEN, \
    FINANCE_SERVICE_CREATE_ORDERS_URL
import requests
import sys, traceback
__author__ = 'Ansal007'
import logging
Logger = logging.getLogger(APP_NAME)

import threading

from kafka import KafkaConsumer

class MockOrderConsumer(threading.Thread):
    daemon = True

    def __init__(self):
        super(MockOrderConsumer, self).__init__()

    def run(self):

        consumer = KafkaConsumer(order_kafka_topic,
                                 group_id=order_kafka_group,
                                 bootstrap_servers=order_kafka_hosts)
        try:
            print 'Starting consuming mock Order'
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

            res = requests.post(url=FINANCE_SERVICE_CREATE_ORDERS_URL, data=json.dumps(data))
            Logger.info('Order posted for orderid {%s} with status code {%s} and status text{%s}'%(message.key, res.status_code, res.text))
        except Exception as e:
            traceback.print_exc()
            Logger.error('Exception while consuming data', exc_info=True)








