import os

__author__ = 'Ansal007'

APP_NAME = 'finance_orders_consumer'

KAFKA_HOSTS = ['kafka01.production.askmebazaar.com:2181', 'kafka02.production.askmebazaar.com:2181',
               'kafka03.production.askmebazaar.com:2181']
KAFKA_TOPIC = 'grocery_orderservice_staging'
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
FINANCE_SERVICE_CREATE_BUYER_ORDERS_URL = 'http://pyservice01.staging.askme.com:11000/finance_service/order/create_buyer_order'
FINANCE_SERVICE_CREATE_SELLER_ORDERS_URL = 'http://pyservice01.staging.askme.com:11000/finance_service/order/create_seller_order'
FINANCE_SERVICE_CREATE_BUYER_COLLECTION_URL = 'http://pyservice01.staging.askme.com:11000/finance_service/collection/create_buyer_collection'
FINANCE_SERVICE_CREATE_SELLER_COLLECTION_URL = 'http://pyservice01.staging.askme.com:11000/finance_service/collection/create_seller_collection'


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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'financedb',  # Or path to database file if using sqlite3.
        'USER': 'finance',  # Not used with sqlite3.
        'PASSWORD': 'finance1234',  # Not used with sqlite3.
        'HOST': 'finance-settlement.c0wj8qdslqom.ap-southeast-1.rds.amazonaws.com',  # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '5432',  # Set to empty string for default. Not used with sqlite3.
    }
}
