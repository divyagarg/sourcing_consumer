import json
import logging
import random
import threading
import uuid
import time
from config import APP_NAME, SLEEP
from kafka_util.collection_kafka_publisher import CollectionPublisher
from kafka_util.order_kafka_publisher import OrderPublisher
from kafka_util.receivable_kafka_publisher import ReceivablePublisher
Logger = logging.getLogger(APP_NAME)

__author__ = 'Ansal007'


class ProduceMockKafkaMessage(threading.Thread):
    daemon = True

    def __init__(self):
        super(ProduceMockKafkaMessage, self).__init__()


    def run(self):

        while True:

            order_uuid = str(uuid.uuid1())

            order_data =   {
                "order_uuid": order_uuid,
                "order_total":random.random()*1000000000,
                "order_discount":random.random()*1000,
                "coupouns":str(uuid.uuid4()),
                "collectible_amount":random.random()*1000000,
                "order_items":[
                    {
                        "orderitem_uuid":str(uuid.uuid4()),
                        "subscription_id":random.randint(0,10000),
                        "orderitem_price":random.random()*1000000,
                        "orderitem_discount":random.random()*1000,
                        "coupouns":str(uuid.uuid4()),
                        "quantity":random.randint(0,10),
                        "transfer_price":random.random()*1000000
                    },
                    {
                        "orderitem_uuid":str(uuid.uuid4()),
                        "subscription_id":random.randint(0,10000),
                        "orderitem_price":random.random()*1000000,
                        "orderitem_discount":random.random()*1000,
                        "coupouns":str(uuid.uuid4()),
                        "quantity":random.randint(0,10),
                        "transfer_price":random.random()*1000000
                    },
                    {
                        "orderitem_uuid":str(uuid.uuid4()),
                        "subscription_id":random.randint(0,10000),
                        "orderitem_price":random.random()*1000000,
                        "orderitem_discount":random.random()*1000,
                        "coupouns":str(uuid.uuid4()),
                        "quantity":random.randint(0,10),
                        "transfer_price":random.random()*1000000
                    },
                    {
                        "orderitem_uuid":str(uuid.uuid4()),
                        "subscription_id":random.randint(0,10000),
                        "orderitem_price":random.random()*1000000,
                        "orderitem_discount":random.random()*1000,
                        "coupouns":str(uuid.uuid4()),
                        "quantity":random.randint(0,10),
                        "transfer_price":random.random()*1000000
                    }
                ]
            }

            OrderPublisher.publish_message(key=order_uuid, message=json.dumps(order_data))

            collection_data =  {
                "orderid":order_uuid,
                "collections":[
                    {
                        "transaction_id":random.random()*1000000000000,
                        "transaction_type":"Credit",
                        "channel":"PAAS",
                        "amount":random.random()*1000000,
                        "status":"Approved"
                    },
                    {
                        "transaction_id":random.random()*1000000000000,
                        "transaction_type":"Credit",
                        "channel":"wallet",
                        "amount":random.random()*1000000,
                        "status":"Approved"
                    },
                    {
                        "transaction_id":random.random()*1000000000000,
                        "transaction_type":"Credit",
                        "channel":"Cash on Delivery",
                        "amount":random.random()*1000000,
                        "status":"Approved"
                    },
                    {
                        "transaction_id":random.random()*1000000000000,
                        "transaction_type":"Credit",
                        "channel":"PAAS",
                        "amount":random.random()*1000000,
                        "status":"Approved"
                    }
                ]
            }

            CollectionPublisher.publish_message(key=order_uuid, message=json.dumps(collection_data))

            receivable_data = {
                "orderid":order_uuid,
                "receivables" : [
                    {
                        "amount":random.random()*100000,
                        "channel":'Cash on Delivery'
                    },
                    {
                        "amount":random.random()*100000,
                        "channel":'PAAS'
                    },
                    {
                        "amount":random.random()*100000,
                        "channel":'Card Payment'
                    },
                    {
                        "amount":random.random()*100000,
                        "channel":'wallet'
                    }
                ]
            }

            ReceivablePublisher.publish_message(key=order_uuid, message=json.dumps(receivable_data))
            print 'Prduced all data with orderid : {%s} '%order_uuid

            time.sleep(SLEEP)

