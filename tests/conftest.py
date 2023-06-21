import logging
from typing import Any, Dict, Iterable, List, Tuple

import pytest

from nhs_context_logging import app_logger, logging_context
from nhs_context_logging.handlers import capturing_log_handlers


@pytest.fixture(scope="session", autouse=True)
def global_setup():
    app_logger.setup("pytest")


@pytest.fixture(scope="function", autouse=True)
def reset_logging_storage():
    logging_context.thread_local_context_storage()


@pytest.fixture(scope="session")
def log_capture_global() -> Iterable[Tuple[List[dict], List[dict]]]:
    std_out: List[Dict[str, Any]] = []
    std_err: List[Dict[str, Any]] = []

    capturing_handlers = capturing_log_handlers(std_out, std_err)

    app_logger.setup("tests")

    for handler in capturing_handlers:
        logging.root.addHandler(handler)

    yield std_out, std_err

    for handler in capturing_handlers:
        logging.root.removeHandler(handler)


@pytest.fixture(scope="function")
def log_capture(log_capture_global) -> Iterable[Tuple[List[dict], List[dict]]]:
    std_out, std_err = log_capture_global

    std_out.clear()
    std_err.clear()

    log_at_level = app_logger.log_at_level

    app_logger.log_at_level = app_logger.DEBUG

    yield std_out, std_err

    app_logger.log_at_level = log_at_level
