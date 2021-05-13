#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 13 13:29:35 2021

@author: michi
"""

import requests
import time


translations = {
    "A": "Alpha",
    "B": "Bravo",
    "C": "Charlie",
    "D": "Delta",
    "E": "Echo",
    "F": "Foxtrott",
    "G": "Golf",
    "H": "Hotel",
    "I": "India",
    "J": "Juliett",
    "K": "Kilo",
    "L": "Lima",
    "M": "Mike",
    "N": "November",
    "O": "Oscar",
    "P": "Papa",
    "Q": "Quebec",
    "R": "Romeo",
    "S": "Sierra",
    "T": "Tango",
    "U": "Uniform",
    "V": "Victor",
    "W": "Whiskey",
    "X": "XRay",
    "Y": "Yankee",
    "Z": "Zulu",
}


def prepare_word(word):
    word = word.lower().strip()
    word = word.replace("ä", "ae")
    word = word.replace("ö", "oe")
    word = word.replace("ü", "ue")
    word = word.replace("ß", "ss")
    return word


def is_valid_word(word):
    if word == None or word == "":
        return False
    for char in prepare_word(word):
        if not char.upper() in translations.keys():
            print("Invalid word: \"{}\"".format(word))
            return False
    return True
        

def get_word():
    word = None
    while not is_valid_word(word):
        api_url = "http://api.corpora.uni-leipzig.de/ws/words/deu_news_2012_1M/randomword/?limit=1"
        response = requests.get(api_url)
        word = response.json()[0]["word"]
    return word
    
    
def print_word(word):
    timeout = 5
    while timeout > 0:
        print("\r{} ({})".format(word, timeout), end = "")    
        timeout -= 1
        time.sleep(1)
    print("\r{}{}".format("#" * len(word), " " * 4))


if __name__ == "__main__":   
    print("Drücke \"Enter\" zum Beginnen.")
    print("Drücke \"Strg + C\" zum Beenden.")
    print("Das Wort wird für jeweils 5 Sekunden angezeigt und verschwindet dann.")
    input()
    
    while True:
        try:
            word = get_word()
            print_word(word)
            for char in prepare_word(word):
                answer = input("> ").strip().lower()
                expected = translations[char.upper()].strip().lower()
                if not answer == expected:
                    print("Falsch! Richtige Antwort: \"{}\", deine Antwort: \"{}\", Wort: \"{}\"".format(expected, answer, word))
            input("Fertig! Drücke \"Enter\" für ein neues Wort, drücke \"Strg + C\" zum Beenden. ")
            print("#" * 80)
            print()
        except KeyboardInterrupt:
            print("Ende")
            break
