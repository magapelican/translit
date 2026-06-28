from mapping import CYRILLIC_TO_LATIN


def cyrillic_to_latin(text):
    result = []
    i = 0

    while i < len(text):
        matched = False

        for length in (2, 1):
            part = text[i:i+length]

            if part in CYRILLIC_TO_LATIN:
                result.append(CYRILLIC_TO_LATIN[part])
                matched = True
                i += length
                break

        if not matched:
            result.append(text[i])
            i += 1
    
    return "".join(result)