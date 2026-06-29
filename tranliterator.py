from mapping import *


def cyrillic_to_latin(text):
    return translite(text, CYRILLIC_TO_LATIN)

def latin_to_cyrillic(text):
    return translite(text, LATIN_TO_CYRILLIC)


def translite(text, FROM_TO):
    result = []
    i = 0

    while i < len(text):
        matched = False

        for length in (2, 1):
            part = text[i:i+length]

            if part in FROM_TO:
                result.append(FROM_TO[part])
                matched = True
                i += length
                break

        if not matched:
            result.append(text[i])
            i += 1
    
    return "".join(result)