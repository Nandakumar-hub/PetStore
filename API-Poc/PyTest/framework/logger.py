import logging

#logger setup

#create logger instance with the module name (__name__)
logger = logging.getLogger(__name__)

#create file handler to write logs to a file - 'logfile.log'
fileHandler = logging.FileHandler('PyTest/logs/logfile.log')

#configure the log message format in logfile.log: timestamp, log level, logger name, message
formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")

#set the formatter to filehandler
fileHandler.setFormatter(formatter)

#set the filehandler to logger
logger.addHandler(fileHandler)


def get_logger():
    return logger