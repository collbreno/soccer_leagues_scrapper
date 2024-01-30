import re
from datetime import datetime
from zoneinfo import ZoneInfo

class DateUtils:
    @staticmethod
    def is_valid_time(time: str):
        time_pattern = r"\d{2}:\d{2}"
        return re.match(time_pattern, time)
    @staticmethod
    def get_datetime_from_timestamp(ts: str) -> datetime:
        return datetime.fromtimestamp(int(ts))