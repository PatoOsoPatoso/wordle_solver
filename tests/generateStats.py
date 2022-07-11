import os
from alive_progress import alive_bar

data = open('words', 'r').read().split('\n')

N = 6

word_list = ['grand', 'clubs', 'tempo', 'hafiz']

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

errors = []
iterations = 0

def resetInfo():
    global corrects, presents, presents_set, absents

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

def checkGuess(guess, expected, i):
    global iterations

    if guess != expected:
        return False
    
    iterations += i

    return True

def main():
    os.system('cls') if os.name == 'nt' else os.system('clear')
    with alive_bar(len(data), dual_line=True, title='Palabras') as bar:
        for expected in data:
            check = False
            for i, guess in enumerate(word_list):
                loadInfo(guess, expected)
                check = checkGuess(guess, expected, i+1)
                if check:
                    break
            if check:
                resetInfo()
                bar()
                continue
            for i in range(4, N):
                guess = decideGuess()
                check = checkGuess(guess, expected, i+1)
                if check:
                    break
                loadInfo(guess, expected)
            if check:
                resetInfo()
                bar()
                continue
            errors.append(expected)
            resetInfo()
            bar()
    
    print("\n\n[ Pruebas finalizadas ]")
    print(f"\n    - He conseguido adivinar {len(data) - len(errors)} de {len(data)}")
    print(f"    - Es decir, me he equivocado en {len(errors)}")
    print(f"    - Un porcentaje de aciertos de un {(len(data) - len(errors)) / len(data) * 100} en {len(data)} aciertos")
    print(f"    - La media de intentos utilizados para adivinar han sido de {iterations // (len(data) - len(errors))}")

    if len(errors) == 0:
        print("\nHasta luego!")
        exit()

    option = input("\nQuieres ver en que palabras me he equivocado? [y/n] --> ")

    if option.lower() != 'y':
        print("\nHasta luego!")
        exit()

    print(errors)

if __name__ == "__main__":
    main()