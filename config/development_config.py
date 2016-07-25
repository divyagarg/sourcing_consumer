__author__ = 'divyagarg'
import os


APP_NAME = 'sourcing_consumer'

KAFKA_HOSTS = ['dc1.staging.askme.com:9092', 'dc2.staging.askme.com:9092']
KAFKA_TOPIC = 'grocery_orderservice_staging'
KAFKA_GROUP = 'sourcing_consumer_9375983457'

HOME = '/tmp'
HOME = os.environ.get('LOG_HOME') or HOME
LOG_DIR = APP_NAME
LOG_FILE = 'application.log'
DEBUG_LOG_FILE = 'application_debug.log'
ERROR_LOG_FILE = 'application_error.log'
ENV = 'default'


PUBLISH_TO_KAFKA = True

PRODUCE_MESSAGE=True


receivable_kafka_hosts = ['kafka01.production.askmebazaar.com:9092', 'kafka02.production.askmebazaar.com:9092',
               'kafka03.production.askmebazaar.com:9092']
receivable_kafka_group = 'mock_receivable_consumer'
receivable_kafka_topic = 'fin_mock_receivable'

collection_kafka_hosts = ['kafka01.production.askmebazaar.com:9092', 'kafka02.production.askmebazaar.com:9092',
               'kafka03.production.askmebazaar.com:9092']
collection_kafka_group = 'mock_collection_consumer'
collection_kafka_topic = 'fin_mock_collection'

order_kafka_hosts = ['kafka01.production.askmebazaar.com:9092', 'kafka02.production.askmebazaar.com:9092',
               'kafka03.production.askmebazaar.com:9092']
order_kafka_group = 'mock_order_consumer'
order_kafka_topic = 'fin_mock_order'

SLEEP = 1

