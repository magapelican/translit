from mappings import avar
from mappings import lak


MAPPINNGS = {
    "avar": avar,
    "lak": lak
}


def cyrillic_to_latin(text, lang):
    mapping = MAPPINNGS[lang.lower()]
    return translite(text, mapping.CYRILLIC_TO_LATIN)

def latin_to_cyrillic(text, lang):
    mapping = MAPPINNGS[lang.lower()]
    return translite(text, mapping.LATIN_TO_CYRILLIC)


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