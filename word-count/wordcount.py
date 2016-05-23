import re
from collections import defaultdict

def word_count(phrase):
    counts = defaultdict(int)
    phrase = unicode(phrase, 'utf-8')
    expression = re.compile("[\W,_]", re.UNICODE)
    split_phrase = re.split(expression, phrase.lower())
    split_phrase = filter(None, split_phrase)

    for word in split_phrase:
        counts[word] += 1
    return counts
