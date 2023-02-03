import logging
from logging import RootLogger


def create_logger(filename: str, level: int, my_format: str, filemode: str) -> RootLogger:
    """Create and configure logger."""
    logging.basicConfig(filename=filename,
                        level=level,
                        format=my_format,
                        filemode=filemode)

    logger = logging.getLogger()

    return logger