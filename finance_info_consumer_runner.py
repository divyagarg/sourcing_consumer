from config import PRODUCE_MESSAGE
from logger import setup_logging
from orderengine import OrderEngineConsumer
from producers.ProduceMockKafkaMessage import ProduceMockKafkaMessage
from kafka_util.collection_kafka_publisher import CollectionPublisher
from kafka_util.order_kafka_publisher import OrderPublisher
from kafka_util.receivable_kafka_publisher import ReceivablePublisher


from consumers.consumer_mock_collections import MockCollectionConsumer
from consumers.consumer_mock_orders import MockOrderConsumer
from consumers.consumer_mock_receivables import MockReceivableConsumer

__author__ = 'Ansal007'

setup_logging()
# CollectionPublisher.init()
# OrderPublisher.init()
# ReceivablePublisher.init()

t1 = OrderEngineConsumer()
# t2 = OrderEngineConsumer()
# t3 = OrderEngineConsumer()

# producer = ProduceMockKafkaMessage()
# cc = MockCollectionConsumer()
# rr = MockReceivableConsumer()
# oo = MockOrderConsumer()
#
#
#
# producer.start()
# cc.start()
# rr.start()
# oo.start()
#
# producer.join()
# cc.join()
# rr.join()
# oo.join()

t1.start()
# t2.start()
# t3.start()
# t1.join()
# t2.join()
# t3.join()
t1.join()