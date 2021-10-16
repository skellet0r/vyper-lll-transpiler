import pytest


def pytest_sessionfinish(session, exitstatus):
    # treat no tests collected as passing
    if exitstatus == pytest.ExitCode.NO_TESTS_COLLECTED:
        session.exitstatus = pytest.ExitCode.OK
