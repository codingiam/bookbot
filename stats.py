import operator

def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    counts = {}

    for c in text.lower():
        if not c in counts:
            counts[c] = 0

        counts[c] += 1

    return counts

def characters_list(h):
    lst = []

    for k in h:
        lst.append({"char": k, "num": h[k]})

    return sorted(lst, reverse=True, key=operator.itemgetter('num'))
