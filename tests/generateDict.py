import os
import requests
from alive_progress import alive_bar
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

def main():
    posible_words = []
    final_words = []

    cnt = 0

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-software-rasterizer")
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_argument("--disable-logging")
    chrome_options.add_argument("--disable-crash-reporter")
    chrome_options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=chrome_options)

    driver.get('https://wordle.danielfrg.com/')

    try:
        driver.find_element(By.XPATH, '//*[@id="headlessui-dialog-3"]/div/div[2]/div[6]/button').click()
    except:
        pass

    body = driver.find_element(By.XPATH, '/html/body')

    os.system('cls') if os.name == 'nt' else os.system('clear')

    with alive_bar(13, dual_line=True, title='Descargando') as bar:
        r = requests.get('https://www.listasdepalabras.es/palabras5letras.htm')
        soup = BeautifulSoup(r.content.decode('utf-8'), 'lxml')

        posible_words.extend(soup.find_all("span", {"class": "mot"})[0].text.split(' '))

        bar()

        for i in range(2, 14):
            r = requests.get(f'https://www.listasdepalabras.es/palabras5letraspagina{i}.htm')
            soup = BeautifulSoup(r.text, 'lxml')
        
            posible_words.extend(soup.find_all("span", {"class": "mot"})[0].text.split(' '))

            bar()

    posible_words = [word.lower() for word in posible_words if 'ã' not in word.lower()]

    with alive_bar(len(posible_words), dual_line=True, title='Arreglando ') as bar:
        for word in posible_words:
            cnt += 1
            body.send_keys(word)
            body.send_keys(Keys.ENTER)
            shake = driver.find_elements(By.CLASS_NAME, 'shake')
            if shake or cnt % 6 == 0:
                driver.execute_script("localStorage.clear();")
                driver.refresh()
                try:
                    driver.find_element(By.XPATH, '//*[@id="headlessui-dialog-3"]/div/div[2]/div[6]/button').click()
                except:
                    pass
                body = driver.find_element(By.XPATH, '/html/body')
            if not shake:
                final_words.append(word)
            bar()

    driver.close()

    with open('words', 'w') as f:
        f.write('\n'.join(final_words))

if __name__ == "__main__":
    main()