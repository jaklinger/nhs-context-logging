import pytest

from nhs_context_logging import app_logger, logging_context
from nhs_context_logging.fixtures import log_capture, log_capture_global  # noqa: F401
from nhs_context_logging.logger import uuid4_hex_string


@pytest.fixture(scope="session", autouse=True)
def global_setup():
    app_logger.setup("pytest", internal_id_factory=uuid4_hex_string)


@pytest.fixture(autouse=True)
def reset_logging_storage():
    logging_context.thread_local_context_storage()
