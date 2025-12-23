import logging

logging.basicConfig(
    level=logging.INFO,
    filename='app.log',
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info('Server Started')
logging.error('Something went wrong')