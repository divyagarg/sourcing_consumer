
import datetime
from config import APP_NAME, KAFKA_HOSTS, KAFKA_GROUP, KAFKA_TOPIC
import traceback
import logging
from kafka import KafkaConsumer

Logger = logging.getLogger(APP_NAME)
import threading



class OrderConsumer(threading.Thread):


    def __init__(self):
        super(OrderConsumer, self).__init__()

    def run(self):

        consumer = KafkaConsumer(KAFKA_TOPIC, group_id= KAFKA_GROUP, bootstrap_servers=KAFKA_HOSTS)
        try:
            print 'Starting consuming mock Order'
            for message in consumer:
                starttime = datetime.datetime.now()
                Logger.info('Message consumed is %s', message)
                endtime = datetime.datetime.now()
                timetaken = endtime - starttime
                total_time = timetaken.seconds*1000000 + timetaken.microseconds
                Logger.info('Total time taken to consume order %s'%total_time)

        except Exception as ex:
            traceback.print_exc()
            Logger.error('Exception while consuming messsege from partition %s', str(ex), exc_info=True)










