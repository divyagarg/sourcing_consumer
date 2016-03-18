from logger import setup_logging
from orderengine import OrderEngineConsumer

__author__ = 'Ansal007'

setup_logging()

t1 = OrderEngineConsumer()
t2 = OrderEngineConsumer()
t1.start()
t2.start()
t1.join()
t2.join()
