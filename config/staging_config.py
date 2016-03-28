import os

__author__ = 'Ansal007'

APP_NAME = 'finance_orders_consumer'

KAFKA_HOSTS = ['kafka01.production.askmebazaar.com:9092', 'kafka02.production.askmebazaar.com:9092',
               'kafka03.production.askmebazaar.com:9092']
KAFKA_TOPIC = 'orderengine.production'
KAFKA_GROUP = 'finance_orders_consumer_9375983457'

DATABASES = {
    'default': {
        'database': 'financedb',
        'user': 'root',
        'password': '',
        'host': 'localhost',
        'port': 3306
    }
}

HOME = '/var/log/'
HOME = os.environ.get('LOG_HOME') or HOME
LOG_DIR = APP_NAME
LOG_FILE = 'application.log'
DEBUG_LOG_FILE = 'application_debug.log'
ERROR_LOG_FILE = 'application_error.log'
ENV = 'default'

FINANCE_SERVICE_TOKEN = "iu3y092u3yrb9823ryb9283rbt23847o479bexypr18tvcr98pxby3p"
FINANCE_SERVICE_CREATE_ORDERS_URL = 'http://pyservice01.staging.askme.com:11000/finance_service/order/create_order'

PUBLISH_TO_KAFKA = True

PRODUCE_MESSAGE = True

create_receivable_url = 'http://pyservice01.staging.askme.com:11000/finance_service/receivable/create_receivable'
create_order_url = 'http://pyservice01.staging.askme.com:11000/finance_service/order/create_order'
create_collection_url = 'http://pyservice01.staging.askme.com:11000/finance_service/collection/create_collection'


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
