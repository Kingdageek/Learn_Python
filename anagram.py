#anagram.py
import string
from pprint import pprint
from markov_analysis import process_file
from file_barchart import get_input

def convert(word):
    k = string.punctuation+string.whitespace
    for i in k:
        word = word.replace(i, "").lower()
    word_list = sorted(word)
    return tuple(word_list)

def find_anagram(li):
    hist = dict()
    for word in li:
        if len(word) > 1: # It shouldn't convert characters
            key = convert(word)
        #if word not in hist.get(key, []):
            #hist.setdefault(key, []).append(word)
        #hist[key] = hist.get(key, set()).add(word)
            hist.setdefault(key, set()).add(word) # no word should appear twice
    return hist

def print_results(h):
    for i in h.values():
        if len(i) > 1:
            pprint(i)

def main():
    while True:
        try:
            file = get_input()
            h = find_anagram(process_file(file))
            print_results(h)
            break
        except (ValueError, IOError):
            print("Invalid Input! if you entered a file",
                  "check if it's in the current directory!")

if __name__ == "__main__": main()
