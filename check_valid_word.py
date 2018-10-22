import json
from itertools import permutations


def create_words_from_characters(char_list, word_lengths):
    for length in word_lengths:
        word = "".join(char_list)
        yield ",".join(set(["".join(p) for p in permutations(word, int(length))]))


def check_valid_word(word):
    with open('english-words/words_dictionary.json') as f:
        data = json.load(f).keys()
        if word in data:
            return word


chars = input("enter the characters with spaces: ").split()
word_lengths = input("enter the length of words you need: ").split()

for word in create_words_from_characters(chars, word_lengths):
    words = word.split(",")
    for w in words:
        if check_valid_word(w):
            print(w)
