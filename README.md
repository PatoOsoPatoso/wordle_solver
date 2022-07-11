<!-- Intro -->
# **WORDLE_SOLVER**
> **Lucas Arroyo Blanco**  
> 
> _PatoOsoPatoso_  

&nbsp;

<!-- Index -->
# Table of contents
## &nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;)&nbsp;&nbsp;[Description](#description)
## &nbsp;&nbsp;&nbsp;&nbsp;2&nbsp;)&nbsp;&nbsp;[Requirements](#requirements)

&nbsp;  
&nbsp; 

<!-- Description -->
## **Description**

This project involves an automatized bot to solve wordle challenges.

This bot has **97.2%** of success over every single 5 letter word accepted by spanish wordle, almost **10000** words

The most important thing is that currently this bot **ONLY** on the spanish wordle website, [wordle.danielfrg.com](https://wordle.danielfrg.com/).

There are 2 versions for this bot, one that uses selenium to solve the daily challenge on the official website and an other to solve words given trough command line.

There are 5 scripts:
* [wordleWeb.py](src/wordleWeb.py) to try to solve the daily wordle challenge on their website
* [wordleText.py](src/wordleText.py) to try to guess a word given by command line imput
* [generateBestWords.py](tests/generateBestWords.py) to generate the best 5 words to start the guessing, currently it only uses 4 of those 5, those being **['grand', 'clubs', 'tempo', 'hafiz']**
* [generateDict.py](tests/generateDict.py) to generate the wordlist that is going to be used during the testing and solving
* [generateStats.py](tests/generateStats.py) to generate a list of statistics based on the success of the bot (the outputs are in spanish)

&nbsp;  

<!-- Requirements -->
## **Requirements**
The only real requirement besides the Python packages used is to have a wordlist like I give you in [words](words)

The Python packages are:
* Selenium to automatize the webbrowser
* Alive Progress for a cool looking progress bar
* BeautifulSoup to scrap [listasdepalabras.es](https://www.listasdepalabras.es), get the words and then check if every single word is acceptec by [wordle.danielfrg.com](https://wordle.danielfrg.com/)

&nbsp;  
&nbsp;

<!-- Bye bye -->
<img src="https://static.wikia.nocookie.net/horadeaventura/images/c/c2/CaracolRJS.png/revision/latest?cb=20140518032802&path-prefix=es" alt="drawing" style="width:100px;"/>**_bye bye_**