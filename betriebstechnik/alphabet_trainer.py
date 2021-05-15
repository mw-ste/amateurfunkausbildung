#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 13 13:29:35 2021

@author: michi
"""

import time
import requests
from difflib import SequenceMatcher

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
    valid = [char.upper() in translations.keys()
             for char in prepare_word(word)]
    if not all(valid):
        print("Ungültiges Wort: \"{}\"".format(word))
        return False
    return True


def get_word_from_api():
    word = None
    while not is_valid_word(word):
        print("Hole neues Wort vom Server...")
        api_url = "http://api.corpora.uni-leipzig.de/ws/words/deu_news_2012_1M/randomword/?limit=1"
        response = requests.get(api_url)
        word = response.json()[0]["word"]
    return word


def print_with_timeout(text, timeout=5, overwrite="#"):
    while timeout > 0:
        text_with_timeout = "\r{} ({})".format(text, timeout)
        print(text_with_timeout, end="")
        timeout -= 1
        time.sleep(1)
        print("\r{}".format(" " * len(text_with_timeout)), end="")
    print("\r{}".format(overwrite * len(text)))


def prompt():
    return input("> ").strip().lower()


def show_progress(word, index):
    progress = word[:index] + "_" + word[index] + "_" + word[index + 1:]
    print_with_timeout(progress, overwrite=" ")


def startup():
    print("Drücke \"Enter\" zum Beginnen.")
    print("Drücke \"Strg + C\" zum Beenden.")
    print("Gibt \"?\" ein, um das Wort und den aktuellen Buchstaben zu sehen zu sehen.")
    print("Das Wort wird für jeweils 5 Sekunden angezeigt und verschwindet dann.")
    input()


def main():
    word = get_word_from_api()
    prepared_word = prepare_word(word)
    print_with_timeout(word)

    for index, char in enumerate(prepared_word):
        answer = prompt()

        while answer == "?":
            show_progress(prepared_word, index)
            answer = prompt()

        expected = translations[char.upper()].strip().lower()
        if SequenceMatcher(None, answer, expected).ratio() < 0.5:
            print("Falsch! Richtige Antwort: \"{}\", deine Antwort: \"{}\"".format(
                expected, answer))

    print()
    input("Fertig! Drücke \"Enter\" für ein neues Wort, drücke \"Strg + C\" zum Beenden. ")
    print()
    print("#" * 80)
    print()


if __name__ == "__main__":
    try:
        startup()

        while True:
            main()

    except KeyboardInterrupt:
        print("\nEnde")
