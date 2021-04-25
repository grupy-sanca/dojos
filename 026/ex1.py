"""
https://www.hackerrank.com/challenges/time-conversion/problem

>>> to_24_hours("07:05:45PM")
'19:05:45'

>>> to_24_hours("07:05:45AM")
'07:05:45'

>>> to_24_hours("12:40:00AM")
'00:40:00'

>>> to_24_hours("12:55:00PM")
'12:55:00'
"""


def to_24_hours(time):
    am_pm = time[-2:]
    hours, minutes, seconds = time[:-2].split(":")
    if am_pm == "PM" and hours != "12":
        hours = int(hours) + 12
    elif am_pm == "AM" and hours == "12":
        hours = "00"
    return f"{hours}:{minutes}:{seconds}"