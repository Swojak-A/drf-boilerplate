"""Misc utils."""

import random
import string
from pathlib import Path
from time import time


def generate_random_string(length):
    """Generate random alphanumerical string with given length"""

    return "".join(
        random.choices(string.ascii_letters + string.digits, k=length)  # noqa: S311
    )


HEALTHCHECK_STATUS_FILE_PATH = Path("/tmp/_healthcheck_status")  # noqa: S108


def refresh_healthcheck_timestamp() -> None:
    """Update timestamp used for healthcheck.

    This is a helper method used in scripts running in loop.
    The timestamp should be refreshed after every iteration.

    If the timestamp is not updated for some time, DC/OS will kill the container.

    Using the same filename for all scripts is not a problem,
    because all scripts are run in separate containers.

    """
    try:
        with Path.open(HEALTHCHECK_STATUS_FILE_PATH, "w") as status_file:
            status_file.write(f"{str(int(time()))}\n")
    except IOError:
        pass
