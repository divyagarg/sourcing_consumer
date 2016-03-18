import os

__author__ = 'Ansal007'

APP_NAME = 'finance_orders_consumer'

KAFKA_HOSTS = ['kafka01.production.askmebazaar.com:9092', 'kafka02.production.askmebazaar.com:9092','kafka03.production.askmebazaar.com:9092']
KAFKA_TOPIC = 'orderengine.production'
KAFKA_GROUP = 'finance_orders_consumer_9375983457'


HOME = '/tmp'
HOME = os.environ.get('LOG_HOME') or HOME
LOG_DIR = APP_NAME
LOG_FILE = 'application.log'
DEBUG_LOG_FILE = 'application_debug.log'
ERROR_LOG_FILE = 'application_error.log'
ENV = 'default'


FINANCE_SERVICE_TOKEN = 9889
