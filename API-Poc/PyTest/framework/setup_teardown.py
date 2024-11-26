from PyTest.framework.logger import get_logger
import time

#initialize logger
logger = get_logger()

def setup():
    #log the setup process
    logger.info("Setting up the environment")

def teardown():
    #log the teardown process
    logger.info("Tearing down the environment")
