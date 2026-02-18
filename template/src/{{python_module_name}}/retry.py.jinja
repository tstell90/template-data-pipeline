"""Retry decorator for resilient external calls.

Handles transient failures (network blips, rate limits, timeouts) with
exponential backoff. No external dependencies — uses only stdlib.

Usage:
    from {{ python_module_name }}.retry import retry

    @retry(max_attempts=3, delay=1.0)
    def call_api():
        response = requests.get("https://api.example.com/data")
        response.raise_for_status()
        return response.json()

    @retry(max_attempts=5, delay=2.0, exceptions=(ConnectionError, TimeoutError))
    def connect_to_db():
        ...
"""

from __future__ import annotations

import logging
import time
from collections.abc import Callable
from functools import wraps
from typing import Any, TypeVar

logger = logging.getLogger(__name__)

F = TypeVar("F", bound=Callable[..., Any])


def retry(
    max_attempts: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    exceptions: tuple[type[BaseException], ...] = (Exception,),
) -> Callable[[F], F]:
    """Retry a function with exponential backoff.

    Args:
        max_attempts: Maximum number of attempts (including the first).
        delay: Initial delay in seconds between retries.
        backoff: Multiplier applied to delay after each retry.
        exceptions: Tuple of exception types to catch and retry on.
    """

    def decorator(func: F) -> F:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_delay = delay
            last_exception: BaseException | None = None

            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as exc:
                    last_exception = exc
                    if attempt == max_attempts:
                        logger.error(
                            "%s failed after %d attempts: %s",
                            func.__name__,
                            max_attempts,
                            exc,
                        )
                        raise
                    logger.warning(
                        "%s attempt %d/%d failed: %s. Retrying in %.1fs...",
                        func.__name__,
                        attempt,
                        max_attempts,
                        exc,
                        current_delay,
                    )
                    time.sleep(current_delay)
                    current_delay *= backoff

            raise last_exception  # type: ignore[misc]  # unreachable but satisfies type checker

        return wrapper  # type: ignore[return-value]

    return decorator
