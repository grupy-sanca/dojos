"""
https://www.codewars.com/kata/59727ff285281a44e3000011

My friend wants a new band name for her band.
She like bands that use the formula: "The" + a noun with the first letter capitalized, for example:

"dolphin" -> "The Dolphin"

However, when a noun STARTS and ENDS with the same letter, she likes to repeat the noun twice
and connect them together with the first and last letter, combined into one word (WITHOUT "The" in front),
like this:

"alaska" -> "Alaskalaska"

Complete the function that takes a noun as a string, and returns her preferred band name written as a string.

>>> ends_with_same_letter("dolphin")
False

>>> ends_with_same_letter("alaska")
True

>>> capitalize_word("dolphin")
'Dolphin'

>>> capitalize_word("alaska")
'Alaska'

>>> adds_the("Dolphin")
'The Dolphin'

>>> duplicate_word("alaska")
'alaskalaska'

>>> duplicate_word("ovo")
'ovovo'

>>> duplicate_word("o")
'o'

>>> band_name("dolphin")
'The Dolphin'

>>> band_name("alaska")
'Alaskalaska'

>>> band_name("Alaska")
'Alaskalaska'

"""

def ends_with_same_letter(word):
    word = word.lower()
    return word[0] == word[-1]

def capitalize_word(word):
    return word.capitalize()

def adds_the(word):
    return 'The '+ word

def duplicate_word(word):
    return word + word[1:]

def band_name(word):
    word = capitalize_word(word)
    if ends_with_same_letter(word):
        return duplicate_word(word) 
    return adds_the(word)
        
    