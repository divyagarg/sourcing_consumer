import json
import datetime
from config import KAFKA_TOPIC, KAFKA_GROUP, KAFKA_HOSTS, APP_NAME, FINANCE_SERVICE_TOKEN, \
    FINANCE_SERVICE_CREATE_ORDERS_URL
import requests
__author__ = 'Ansal007'
import logging
Logger = logging.getLogger(APP_NAME)

import threading

from kafka import KafkaConsumer

class OrderEngineConsumer(threading.Thread):
    daemon = True

    def __init__(self):
        super(OrderEngineConsumer, self).__init__()

    def run(self):

        consumer = KafkaConsumer(KAFKA_TOPIC,
                                 group_id=KAFKA_GROUP,
                                 bootstrap_servers=KAFKA_HOSTS)
        try:
            for message in consumer:
                starttime = datetime.datetime.now()
                self.publish_message_to_finance_service()
                endtime = datetime.datetime.now()
                timetaken = endtime - starttime
                total_time = timetaken.seconds*1000000 + timetaken.microseconds
                Logger.info('Total time taken to consume order %s'%total_time)
                print message

        except Exception as ex:
            Logger.log_error(ex)

    def publish_message_to_finance_service(self, message):
        try:
            json_data = json.loads(message.value)

            data = {
                'token' : FINANCE_SERVICE_TOKEN,
                'data':{
                    'order_uuid':json_data['order_uuid'],
                    'order_data':json_data
                }
            }

            res = requests.post(url=FINANCE_SERVICE_CREATE_ORDERS_URL, data=json.dumps(data))
            Logger.info('Order posted for orderid {%s} with status code {%s} and status text{%s}'%(message.key, res.status_code, res.text))
        except Exception as e:
            Logger.error('Exception while consuming data', exc_info=True)








