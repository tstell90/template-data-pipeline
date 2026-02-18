"""Tests for retry module."""

import pytest

from {{ python_module_name }}.retry import retry


def test_retry_succeeds_first_attempt():
    call_count = 0

    @retry(max_attempts=3, delay=0)
    def succeed():
        nonlocal call_count
        call_count += 1
        return "ok"

    assert succeed() == "ok"
    assert call_count == 1


def test_retry_succeeds_after_failures():
    call_count = 0

    @retry(max_attempts=3, delay=0)
    def fail_then_succeed():
        nonlocal call_count
        call_count += 1
        if call_count < 3:
            raise ConnectionError("transient")
        return "ok"

    assert fail_then_succeed() == "ok"
    assert call_count == 3


def test_retry_exhausted():
    @retry(max_attempts=2, delay=0)
    def always_fail():
        raise ValueError("permanent")

    with pytest.raises(ValueError, match="permanent"):
        always_fail()


def test_retry_specific_exceptions():
    call_count = 0

    @retry(max_attempts=3, delay=0, exceptions=(ConnectionError,))
    def wrong_exception():
        nonlocal call_count
        call_count += 1
        raise TypeError("not retryable")

    with pytest.raises(TypeError):
        wrong_exception()
    assert call_count == 1
