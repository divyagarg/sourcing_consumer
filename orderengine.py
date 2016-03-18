import json
from config import KAFKA_TOPIC, KAFKA_GROUP, KAFKA_HOSTS, APP_NAME

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
                print (message)

        except Exception as ex:
            Logger.log_error(ex)

    def publish_message_to_finance_service(self, message):
        json_data = json.loads(message)



