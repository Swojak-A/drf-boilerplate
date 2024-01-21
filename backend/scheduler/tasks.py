"""Scheduler app tasks."""

from scheduler import celery_app
from utils.misc import refresh_healthcheck_timestamp


@celery_app.task(queue="celerybeat")
def celerybeat_healthcheck():
    """Update celerybeat healthcheck file."""
    refresh_healthcheck_timestamp()
