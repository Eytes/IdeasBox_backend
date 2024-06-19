from datetime import datetime, UTC

from core.config import settings


def formatted_time_now(time_format: str = settings.time_format) -> str:
    return datetime.now(UTC).strftime(format=time_format)


def converting_date_string_to_datetime(
    date_string: str,
    time_format: str = settings.time_format,
) -> datetime:
    return datetime.strptime(date_string, time_format)
