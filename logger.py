import logging
from logging import handlers
from config import HOME, LOG_DIR, APP_NAME, LOG_FILE, ERROR_LOG_FILE

__author__ = 'Ansal007'
import os
def setup_logging():
    if not os.path.exists(HOME):
        os.makedirs(HOME)

    log_dir = os.path.join(HOME, LOG_DIR)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s - %(lineno)d - %(funcName)s - %(message)s")

    logger = logging.getLogger(APP_NAME)
    logger.setLevel(logging.INFO)

    handler = logging.handlers.TimedRotatingFileHandler(os.path.join(log_dir, LOG_FILE), 'midnight')
    handler.setLevel(logging.INFO)
    handler.setFormatter(formatter)

    errorhandler = logging.handlers.TimedRotatingFileHandler(os.path.join(log_dir, ERROR_LOG_FILE), 'midnight')
    errorhandler.setLevel(logging.ERROR)
    errorhandler.setFormatter(formatter)

    logger.addHandler(errorhandler)
    logger.addHandler(handler)