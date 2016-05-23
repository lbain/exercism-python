import re

def hey(what):
    # remove whitespace characters
    what = what.strip()
    if not what:
        return 'Fine. Be that way!'

    if what.isupper():
        return 'Whoa, chill out!'

    if what.endswith('?'):
        return 'Sure.'

    return 'Whatever.'
