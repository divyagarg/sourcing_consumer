import datetime
import logging

# from manage import g
from config import PUBLISH_TO_KAFKA
from kafka import KeyedProducer, SimpleClient
from config import APP_NAME, collection_kafka_hosts, collection_kafka_topic

Logger = logging.getLogger(APP_NAME)

class CollectionPublisher:
    kafka = None
    producer = None

    def __init__(self):
        pass

    @staticmethod
    def init():
        print 'Init of CollectionPublisher kafka'
        CollectionPublisher.kafka = SimpleClient(collection_kafka_hosts, 'order-messages')
        CollectionPublisher.producer = KeyedProducer(CollectionPublisher.kafka, async=True, batch_send_every_t=0.010)

    @staticmethod
    def publish_message(key, message, **kwargs):
        try:
            Logger.info(' Publishing data {%s} '%( message))
            startTime = datetime.datetime.now()

            if PUBLISH_TO_KAFKA:
                CollectionPublisher.producer.send_messages(collection_kafka_topic, key, message)

            endTime = datetime.datetime.now()
            total_time = endTime-startTime
            total_time = total_time.seconds*1000000 + total_time.microseconds
            Logger.info(' Kafka took {%s} microseconds for publishing'%( total_time))
            return True
        except Exception as e:
            Logger.error('{%s} Exception while publishing', exc_info=True)
            raise Exception(str(e))

    @staticmethod
    def test():
        CollectionPublisher.publish_message("test", "This is a test msg")
