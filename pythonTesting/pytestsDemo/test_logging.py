import logging


def test_loggingDemo():
    logger = logging.getLogger(__name__)            # the log message will capture the test file name in the log file

    # fileHandler object  --> tell the log file name
    fileHandler = logging.FileHandler("logfile.log")

    # the format for printing the log message
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    # %() --> print the executed variable value;    s --> string

    # pass/connect the formatter object into the "fileHandler" object
    fileHandler.setFormatter(formatter)

    # how the file is presented; where to print & what is the format
    logger.addHandler(fileHandler)      # fileHandler object

    # set the log message level
    # if set level to "info", then the logger will only print from that level to any level inferior to it
    logger.setLevel(logging.DEBUG)


    # level hierarchy of the log
    logger.debug("A debug statement is executed")      # print a debug message in the file
    logger.info("Information statement")               # print an information message
    logger.warning("Something is in warning mode")     # print a warning message
    logger.error("A Major error Has Happened")         # print an error message
    logger.critical("Critical Issue")                  # print a message if that step would halt the remaining test case
