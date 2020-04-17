import logging
from random import randint, seed
import time


# create logger with 'spam_application'
logger = logging.getLogger('spam_application')
logger.setLevel(logging.DEBUG)

# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
# add the handlers to the logger

logger.addHandler(ch)

err = 0
info = 0
warn = 0


while True:
    i = randint(0, 100)
    print(i)
    if (i % 10) < 5:
        logger.info('info: ' + str(info))
        info = info + 1
    elif (i % 10) < 8:
        logger.error('error: ' + str(err))
        err = err + 1
    else:
        logger.warning('warning: ' + str(warn))
        warn = warn + 1 
    time.sleep(2)