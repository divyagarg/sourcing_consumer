from consumers.consumer_orders import OrderConsumer
from logger import setup_logging

__author__ = 'divyagarg'

setup_logging()

t1 = OrderConsumer()
t2 = OrderConsumer()

t1.start()
t2.start()

t1.join()
t2.join()
