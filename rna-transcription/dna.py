def convert(char):
    transcription = {'G': 'C',
                     'C': 'G',
                     'T': 'A',
                     'A': 'U'}
    return transcription[char]

def to_rna(test_string):
    transcribed = map(convert, test_string)
    return ''.join(transcribed)
