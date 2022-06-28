"""
https://www.codewars.com/kumite/5b748f34b1181438060005ae

Your code should return a Boolean of true if the provided password meets the following conditions

    password must be no less than 8 characters long
    password must have at least 1 capital letter
    password must have at least 1 number
    password must have at least 1 special character

for this Kata special characters are considered ( ! " # $ % & ' ( ) * + ' - . / ; : < > = or ?)

if the password doesn't meet these requirements return false.

>>> validate_min_chars("thiago")
False
>>> validate_min_chars("thiago12345")
True
>>> validate_at_least_one_capital_letter("thiago")
False
>>> validate_at_least_one_capital_letter("thiagoC")
True
>>> validate_at_least_one_capital_letter("thiagoC123")
True
>>> validate_at_least_one_capital_letter("thiagoC#!@#1")
True
>>> validate_at_least_one_number("thiagoC")
False
>>> validate_at_least_one_number("thiago11C")
True
>>> validate_at_least_one_special("thiagoC")
False
>>> validate_at_least_one_special("thiagoC*")
True
>>> validate_password("Thiago123#")
True
>>> validate_password("thiago123#")
False
>>> validate_password("Thiago123")
False
>>> validate_password("Thiago#####")
False
>>> validate_password("Thiag@")
False
>>> validate_password("!T13132312!")
True
>>> validate_password("!t13132312!")
False
"""
def validate_min_chars(password):
    min_chars = 8
    return len(password) >= min_chars  

def validate_at_least_one_capital_letter(password):
    return password.lower() != password

def validate_at_least_one_number(password):
    for char in password:
        if char.isnumeric():
            return True
    return False

def validate_at_least_one_special(password):
    special_chars = set("""!"#$%&'()*+'-./;:<>=?""")
    password_set  = set(password)
    return bool(special_chars & password_set)    

def validate_password(password):
    validators = [
        validate_min_chars, 
        validate_at_least_one_capital_letter,
        validate_at_least_one_number,
        validate_at_least_one_special
    ]
    for validator in validators:
        if not validator(password):
          return False
    
    return True