import pytz
import datetime


def format_xaxis(series: list[int], Multiplier=60 * 60 * 24, format: str = "%B %d, %Y"):
    return [
        datetime.datetime.fromtimestamp(i).astimezone(pytz.utc).strftime(format)
        for i in list(map(lambda x: int(x) * Multiplier, series))
    ]

def format_number(x):
    magnitude = 0
    while abs(x) >= 1000:
        magnitude += 1
        x /= 1000.0
    
    return '%.2f%s' % (x, ['', 'K', 'M', 'G', 'T', 'P'][magnitude])