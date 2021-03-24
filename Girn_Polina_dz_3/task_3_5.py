from random import choice


def get_jokes(n=1, repeat=True):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    jokes = []
    i = 0

    while i != n:
        joke = ''
        words = []

        """первую шутку создаем без проверки на повторы"""
        if i == 0:
            words = [choice(nouns), choice(adverbs), choice(adjectives)]
            joke = ' '.join(words)

            jokes.append(joke)
            i += 1
            continue

        """объединяю список шуток в одну строку, чтобы найти повторения"""
        if not repeat:
            words = [choice(nouns), choice(adverbs), choice(adjectives)]
            while True:
                for k in range(len(words)):
                    # _temp = ''.join(jokes)
                    if words[k] in ''.join(jokes):
                        words = [choice(nouns), choice(adverbs), choice(adjectives)]

                if (words[0] not in ''.join(jokes)) and (words[1] not in ''.join(jokes)) \
                        and (words[2] not in ''.join(jokes)):
                    joke = ' '.join(words)
                    break
        else:
            words = [choice(nouns), choice(adverbs), choice(adjectives)]
            joke = ' '.join(words)

        jokes.append(joke)
        i += 1

    return jokes


print(get_jokes(5))
print(get_jokes(3, False))
print(get_jokes(repeat=True, n=2))



