import logging

logging.basicConfig(filename='error.log',level=logging.ERROR)

try:
    x = 1 / 0
except ZeroDivisionError as e:
    logging.error("Division by zero occured: %s",e)