import logging
from datetime import datetime


class Logger:
    def __init__(self, name):
        self._logger = logging.getLogger(name)
        self._logger.setLevel(logging.DEBUG)
        if not self._logger.handlers:
            handler = logging.StreamHandler()
            handler.setFormatter(
                logging.Formatter("%(levelname)s %(name)s: %(message)s")
            )
            self._logger.addHandler(handler)

    def _with_timestamp(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"{timestamp} {message}"

    def debug(self, message):
        self._logger.debug(self._with_timestamp(message))

    def info(self, message):
        self._logger.info(self._with_timestamp(message))

    def error(self, message):
        self._logger.error(self._with_timestamp(message))
