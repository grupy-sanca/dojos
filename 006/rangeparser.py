"""
>>> range_parser('1')
[1]
>>> range_parser('1,2,3,10,50')
[1, 2, 3, 10, 50]
>>> range_parser('3-8')
[3, 4, 5, 6, 7, 8]
>>> range_parser('1,2,3-8')
[1, 2, 3, 4, 5, 6, 7, 8]
>>> parse_range('1-3')
[1, 2, 3]
>>> parse_range('1-3:2')
[1, 3]
>>> range_parser('1-10,14, 20-25:2')
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14, 20, 22, 24]
>>> range_parser('1-10,14, 20-25:2, 1000-5000:1000')
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14, 20, 22, 24, 1000, 2000, 3000, 4000, 5000]
"""


def clean(string):
    return string.replace("'", '')


def range_parser(string):
    l = []
    for elem in clean(string).split(','):  # 1-10, 15, 20, 30-40:3
        if '-' in elem:
            l.extend(parse_range(elem))
        else:
            l.append(int(elem))
    return l


def parse_range(interval):
    step = 1
    if ':' in interval:
        interval, step = interval.split(':')
    start, stop = [int(e) for e in interval.split('-')]
    return list(range(start, stop + 1, int(step)))
