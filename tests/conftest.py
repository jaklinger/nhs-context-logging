import pytest

from nhs_context_logging import app_logger, logging_context
from nhs_context_logging.pytest import log_capture, log_capture_global  # noqa: F401


@pytest.fixture(scope="session", autouse=True)
def global_setup():
    app_logger.setup("pytest")


@pytest.fixture(scope="function", autouse=True)
def reset_logging_storage():
    logging_context.thread_local_context_storage()
