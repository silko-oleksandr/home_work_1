#Ex 9.1
def popular_words(text, words):
    for ch in ".,!?;:-_—\n\r\t":
        text = text.replace(ch, ' ')

    word_list = text.lower().split()
    result = {word: 0 for word in words}

    for w in word_list:
        if w in result:
            result[w] += 1

    return result
#Ex 9.2
def difference(*args):
    if not args:
        return 0
    return round(max(args) - min(args), 2)