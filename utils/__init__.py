import logging


class BasicLogger:
    def __init__(self, msg):
        logging.basicConfig(
            format="%(asctime)s - %(message)s",
            datefmt="%d-%b-%y %H:%M:%S",
            level=logging.INFO,
        )
        logging.info(msg)
