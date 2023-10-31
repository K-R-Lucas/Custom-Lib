from log import util
from log import console
from time import perf_counter

logger = console.LiveLogger()

logger.info("Augh\n")
logger.warn("Augh?\n")
logger.error("Augh!\n")