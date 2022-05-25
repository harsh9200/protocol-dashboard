import pytz
import datetime


def format_xaxis(series: list[int], Multiplier=60 * 60 * 24, format: str = "%B %d"):

    return [
        datetime.datetime.fromtimestamp(i).astimezone(pytz.utc).strftime(format)
        for i in list(map(lambda x: int(x) * Multiplier, series))
    ]
