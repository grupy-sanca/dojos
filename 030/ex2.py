"""
https://www.codewars.com/kata/56eb16655250549e4b0013f4

What is your favourite day of the week? Check if it's the most frequent day of the week in the year.

You are given a year as integer (e. g. 2001). You should return the most frequent day(s) of the week
in that year. The result has to be a list of days sorted by the order of days in week
(e. g. ['Monday', 'Tuesday'], ['Saturday', 'Sunday'], ['Monday', 'Sunday']). Week starts with Monday.

Input: Year as an int.

most_frequent_days(2427) == ['Friday']
most_frequent_days(2185) == ['Saturday']
most_frequent_days(2860) == ['Thursday', 'Friday']


>>> most_frequent_days(2427)
['Friday']

>>> most_frequent_days(2860)
['Thursday', 'Friday']

>>> most_frequent_days(2185)
['Saturday']
"""
from datetime import date, timedelta
from calendar import isleap


def most_frequent_days(year):    
    most_frequent = []
    first_day = date(year, 1, 1)
    most_frequent.append(first_day.strftime("%A"))
    if isleap(year):
        most_frequent.append(
            (first_day + timedelta(days=1)).strftime("%A")
        )
    
    return most_frequent