def count_words(string):
    number = len(string.split())
    return number

def count_characters(string):
    characters = {}
    lowered_string = string.lower()
    
    for c in lowered_string:
        if c in characters:
            characters[c] += 1
        else:
            characters[c] = 1
    
    return characters