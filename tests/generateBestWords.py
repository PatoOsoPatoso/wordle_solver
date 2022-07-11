import random

data = open('words', 'r').read().split('\n')

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

word_dict = {
    'a': 0,
    'b': 0,
    'c': 0,
    'd': 0,
    'e': 0,
    'f': 0,
    'g': 0,
    'h': 0,
    'i': 0,
    'j': 0,
    'k': 0,
    'l': 0,
    'm': 0,
    'n': 0,
    'ñ': 0,
    'o': 0,
    'p': 0,
    'q': 0,
    'r': 0,
    's': 0,
    't': 0,
    'u': 0,
    'v': 0,
    'w': 0,
    'x': 0,
    'y': 0,
    'z': 0
}

for word in data:
    for letter in word:
        word_dict[letter] += 1

word_dict = {k: v for k, v in sorted(word_dict.items(), key=lambda item: item[1], reverse=True)}

most_used = []

for i, key in enumerate(word_dict):
    if i == 16:
        break
    most_used.append(key)

while True:
    word_list = []
    letters = []
    final_words = []
    random.shuffle(data)

    for w1 in data:
        if not all(x in most_used for x in w1):
            continue
        if len(set(w1)) != len(w1):
            continue
        sum = 0
        for x in ['a', 'e', 'i', 'o', 'u']:
            if x in w1:
                sum += 1
        if (sum > 1 and len(word_list) < 2) or (sum > 2 and len(word_list) < 3):
            continue
        if word_list:
            accepted = True
            for w2 in word_list:
                if len(set(w1+w2)) != (len(w1)+len(w2)):
                    accepted = False
                    break
            if accepted:
                word_list.append(w1)
                letters.extend(w1)
        else:
            word_list.append(w1)
            letters.extend(w1)
    if len(word_list) == 3:
        for word in data:
            if [x in list(set(alpha)-set(letters)) for x in word].count(True) == 4 and len(word) - len(set(word)) == 0:
                final_words.append(word)
        if not final_words:
            continue
        print(word_list)
        print(final_words)
        exit()

