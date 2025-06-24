# logger.py
import logging

def configure_logger(log_path: str):
    """
    Zet een rotatie-logger op die alles vastlegt wat het script doet.
    """
    logger = logging.getLogger("ad_onboard")
    logger.setLevel(logging.INFO)

    handler = logging.FileHandler(log_path, encoding="utf-8")
    formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s", "%Y%m%d%H%M%S")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
