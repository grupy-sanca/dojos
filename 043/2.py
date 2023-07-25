"""
Solve the horror of unstandardized keypads by providing a
function that converts computer input to a number as if
it was typed on a phone.

Example:
"789" -> "123"

>>> convert_digit('7')
'1'

>>> convert_digit('4')
'4'

>>> convert_digit('12')
'78'

>>> convert_digit('789')
'123'

>>> convert_digit('456')
'456'

>>> convert_digit('01234')
'07894'
"""

def convert_digit(digit):
    conversion_dict = {
        '0': '0',
        '1': '7',
        '2': '8',
        '3': '9',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '1',
        '8': '2',
        '9': '3'}
    
    converted = ''
    for d in digit:
        converted += conversion_dict[d]

    return converted
