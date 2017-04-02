import inspect
import logging

def customLogger(loglevel = logging.DEBUG):

    # Gets the name of the class / method from where this method is called

    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)

    # By default log all the messages
    logger.setLevel(logging.DEBUG)

    filehandler = logging.FileHandler("automation.log", mode = 'w')
    filehandler.setLevel(loglevel)

    formatter = logging.Formatter("%(asctime)s - %(name)s -  %(levelname)s : %(message)s",
                                      datefmt= "%m/%d/%Y %I:%M:%S %p")
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)

    return logger