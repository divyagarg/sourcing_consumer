import json
import datetime
from config import KAFKA_TOPIC, KAFKA_GROUP, KAFKA_HOSTS, APP_NAME, FINANCE_SERVICE_TOKEN
import requests
import sys, traceback
__author__ = 'Ansal007'
import logging
Logger = logging.getLogger(APP_NAME)
from config import KafkaMessageTypes, FINANCE_SERVICE_CREATE_BUYER_COLLECTION_URL, \
                                        FINANCE_SERVICE_CREATE_BUYER_ORDERS_URL, FINANCE_SERVICE_CREATE_SELLER_ORDERS_URL, \
                                        FINANCE_SERVICE_CREATE_SELLER_COLLECTION_URL
import threading

from kafka import KafkaConsumer

class OrderEngineConsumer(threading.Thread):
    daemon = True

    def __init__(self):
        super(OrderEngineConsumer, self).__init__()

    def run(self):
        Logger.info('Consuming for Topic:{}, Group:{}, Hosts: {}'%(KAFKA_TOPIC,KAFKA_GROUP,KAFKA_HOSTS))
        consumer = KafkaConsumer(KAFKA_TOPIC,
                                 group_id=KAFKA_GROUP,
                                 bootstrap_servers=KAFKA_HOSTS)
        for message in consumer:
            try:
                starttime = datetime.datetime.now()
                flag = self.publish_message_to_finance_service(message)
                # if flag:
                #     consumer.commit()
                # else:
                #     continue
                endtime = datetime.datetime.now()
                timetaken = endtime - starttime
                total_time = timetaken.seconds*1000000 + timetaken.microseconds
                Logger.info('Total time taken to consume order %s'%total_time)
            except Exception as ex:
                traceback.print_exc()
                Logger.error('Exception while consuming messsege from partition', exc_info=True)
                # consumer.commit()



    def publish_message_to_finance_service(self, message):
        try:
            json_data = json.loads(message.value)

            data = {
                'token': FINANCE_SERVICE_TOKEN,
                'data': json_data,
                'entity_id': str(message.key),
                'offset': message.offset
            }

            res = requests.post(url=OrderEngineConsumer.build_url_from_message(json_data), data=json.dumps(data))
            Logger.info('Order posted for orderid {%s} with status code {%s} and status text{%s}'%(message.key, res.status_code, res.text))
            if res.content['status'] != 'success':
                Logger.error('Data not persisted, retrying! Order not processed for orderid {%s} with status code {%s} and status text {%s}, DATA: {%s}'%(message.key, res.status_code, res.text, json_data))
                return False
            else:
                return True

        except Exception as e:
            traceback.print_exc()
            Logger.error('Exception while consuming data', exc_info=True)
            return True

    @staticmethod
    def build_url_from_message(message):
        type = message['msg_type']
        if type == KafkaMessageTypes.BUYER_ORDER_MESSAGE:
            return FINANCE_SERVICE_CREATE_BUYER_ORDERS_URL
        elif type == KafkaMessageTypes.SELLER_ORDER_MESSAGE:
            return FINANCE_SERVICE_CREATE_SELLER_ORDERS_URL
        elif type == KafkaMessageTypes.BUYER_PAYMENT_STATUS:
            return FINANCE_SERVICE_CREATE_BUYER_COLLECTION_URL
        elif type == KafkaMessageTypes.SELLER_PAYEMNT_STATUS:
            return FINANCE_SERVICE_CREATE_SELLER_COLLECTION_URL
        else:
            raise Exception('Message Type invalid!')







