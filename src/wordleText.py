import sys

data = open('words', 'r').read().split('\n')

N = 6

corrects = [None]*5
presents = {
    '0':  set(),
    '1':  set(),
    '2':  set(),
    '3':  set(),
    '4':  set()
}
presents_set = set()
absents = set()

word_list = ['grand', 'clubs', 'tempo', 'hafiz']

def loadInfo(guess, expected):
    for j in range(len(guess)):
        if guess[j] == expected[j]:
            if guess[j] != corrects[j]:
                corrects[j] = guess[j]
        if guess[j] != expected[j] and guess[j] in expected:
            presents[str(j)].add(guess[j])
            presents_set.add(guess[j])
        if guess[j] not in expected:
            absents.add(guess[j])

def getCorrects():
    posible_c = []

    for word in data:
        add_correct = True
        for j in range(len(word)):
            if word[j] != corrects[j] and corrects[j] != None:
                add_correct = False
                break
        if add_correct:
            posible_c.append(word)
    
    if not posible_c:
        posible_c = data

    return posible_c

def getPresents(posible_c):
    posible_cp = []

    for word in posible_c:
        add_present = True
        for j in range(len(word)):
            if word[j] in presents[str(j)]:
                add_present = False
                break
        if add_present and all(item in word for item in presents_set):
            posible_cp.append(word)
    
    if not posible_cp:
        posible_cp = posible_c
    
    return posible_cp

def getAbsents(posible_cp):
    posible_cpa = []

    for word in posible_cp:
        add_absent = True
        if any(item in absents for item in word):
            add_absent = False
        if add_absent:
            posible_cpa.append(word)

    if not posible_cpa:
        posible_cpa = posible_cp
    
    return posible_cpa

def decideGuess():
    posible_c = getCorrects()

    posible_cp = getPresents(posible_c)

    posible_cpa = getAbsents(posible_cp)

    if not posible_cpa:
        print("[ERROR] - No hay palabras que cumplan los requisitos")
        exit(1)
    
    return posible_cpa[0]

def getExpected():
    if len(sys.argv) != 2 or len(sys.argv[1]) != 5 or any([True for x in sys.argv[1] if not x.isalpha()]):
        print("[ERROR] - Ejecuta de la siguiente forma:")
        print(f"    python3 {__file__} <palabra de 5 letras>")
        exit(1)

    return sys.argv[1]

def checkGuess(guess, expected, i):
    if guess == expected:
        print(f"Iteración {i} de {N}: [EXITO] -->    {guess} - {expected}")
        print(f"\nMe ha costado {i} iteraciones, gracias por jugar!")
        exit(0)
    else:
        print(f"Iteración {i} de {N}: [ERROR] -->    {guess} - {expected}")

def main():
    expected = getExpected()

    for i, guess in enumerate(word_list):
        loadInfo(guess, expected)
        checkGuess(guess, expected, i+1)

    for i in range(4, N):
        guess = decideGuess()

        checkGuess(guess, expected, i+1)

        loadInfo(guess, expected)
    
    print("\nLo siento he perdido :(")


if __name__ == "__main__":
    main()