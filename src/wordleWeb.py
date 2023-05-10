from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def element_presence(how, what, time):
    element_present = EC.presence_of_element_located((how, what))
    WebDriverWait(driver, time).until(element_present)

data = open('words', 'r').read().split('\n')

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

N = 6

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

driver.get('https://wordle.danielfrg.com/')

try:
    element_presence(By.XPATH, "/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/button[1]", 40)
    driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/button[1]").click()
    element_presence(By.XPATH, "/html/body/div[2]/div[3]/div/div/div[2]/div[1]/button", 40)
    driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/div/div[2]/div[1]/button").click()
except:
    pass

body = driver.find_element(By.XPATH, '/html/body')

def loadInfo(i):
    global absents

    cards = driver.find_elements(By.CLASS_NAME, 'mui-style-e8rekw')[i].find_elements(By.CLASS_NAME, 'react-card-back')

    keyboard_rows = driver.find_elements(By.CLASS_NAME, 'mui-style-vzy0h5')

    keyboard_rows.append(driver.find_element(By.CLASS_NAME, 'mui-style-1j52cd2'))

    
    for j in range(len(cards)):
        card_correct = cards[j].find_elements(By.CLASS_NAME, 'mui-style-bn1qqj')
        if card_correct:
            corrects[j] = card_correct[0].text.lower()
        
        card_present = cards[j].find_elements(By.CLASS_NAME, 'mui-style-1s62ug5')
        if card_present:
            presents[str(j)].add(card_present[0].text.lower())
            presents_set.add(card_present[0].text.lower())

    for key_row in keyboard_rows:
        key_absents = key_row.find_elements(By.CLASS_NAME, 'mui-style-1596855')
        absents = absents.union(set([x.text.lower() for x in key_absents]))

    return absents

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
        exit()

    return posible_cpa[0]

def main():
    for i, guess in enumerate(word_list):
        body.send_keys(guess)
        body.send_keys(Keys.ENTER)

        loadInfo(i)

    for i in range(4, N):
        body.send_keys(decideGuess())
        body.send_keys(Keys.ENTER)

        loadInfo(i)

        if not None in corrects:
            exit()

if __name__ == "__main__":
    main()