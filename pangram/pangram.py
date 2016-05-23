def is_pangram(test_string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    test_string = test_string.lower()

    for char in alphabet:
        if char not in test_string:
            return False
    return True
