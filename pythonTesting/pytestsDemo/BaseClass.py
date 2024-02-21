import inspect
import logging


class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]          # capture the method name into "loggerName" of the method being call
        logger = logging.getLogger(loggerName)      # the log message will capture the test case name in the log file
        fileHandler = logging.FileHandler("logfile.log")    # fileHandler object  --> tell the log file name
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")     # log message format
        fileHandler.setFormatter(formatter)         # pass/connect the formatter object into the "fileHandler" object

        # how the file is presented; where to print & what is the format
        logger.addHandler(fileHandler)  # fileHandler object

        # set the log message level
        logger.setLevel(logging.DEBUG)

        return logger
