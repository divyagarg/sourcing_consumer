__author__ = 'divyagarg'
import os


APP_NAME = 'sourcing_consumer'

KAFKA_HOSTS = ['kafka01.production.askmebazaar.com:9092', 'kafka02.production.askmebazaar.com:9092','kafka03.production.askmebazaar.com:9092']
KAFKA_TOPIC = 'grocery_orderservice_staging'
KAFKA_GROUP = 'sourcing_consumer_9375983457'


HOME = '/var/log/'
HOME = os.environ.get('LOG_HOME') or HOME
LOG_DIR = APP_NAME
LOG_FILE = 'application.log'
DEBUG_LOG_FILE = 'application_debug.log'
ERROR_LOG_FILE = 'application_error.log'
ENV = 'default'

PUBLISH_TO_KAFKA = True

PRODUCE_MESSAGE=False



create_receivable_url = None
create_order_url = None
create_collection_url = None

receivable_kafka_hosts = None
receivable_kafka_group = None
receivable_kafka_topic = None

collection_kafka_hosts = None
collection_kafka_group = None
collection_kafka_topic = None

order_kafka_hosts = None
order_kafka_group = None
order_kafka_topic = None

