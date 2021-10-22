"""
Exercício: Stop gninnipS My sdroW!
(https://www.codewars.com/kata/5264d2b162488dc400000001/train/python)

Write a function that takes in a string of one or more words,
and returns the same string, but with all five or more letter words reversed
(like the name of this kata).

Strings passed in will consist of only letters and spaces.
Spaces will be included only when more than one word is present.

spinWords("Hey fellow warriors") => "Hey wollef sroirraw" 
spinWords("This is a test") => "This is a test" 
spinWords("This is another test") => "This is rehtona test"

>>> spin_words("Ana Dulce, Juliana, Rafael e Thiago")
'Ana ,ecluD ,anailuJ leafaR e ogaihT'
 
>>> spin_words("Hey fellow warriors")
'Hey wollef sroirraw'

"""

def spin_words(phrase):
    words = phrase.split(" ")

    return " ".join([(word[::-1] if len(word) >=5 else word) for word in words])
