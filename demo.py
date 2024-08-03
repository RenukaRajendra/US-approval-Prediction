from us_visa.logger import logging
from us_visa.exception import USvisaException

try:
    a = 1/ 10
except Exception as e:
    raise USvisaException(str(e)) from e

logging.info("Welcome to our project!")