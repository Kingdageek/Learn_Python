#markov_analysis.py

import string
from random import choice

def process_file(filename):
    """Returns a list of every word in the file"""
    new_li = []
    with open(filename) as f:
        for line in f:
            process_line(line, new_li)
    return new_li

def process_line(line, new_li):
    """modify 'new_li' until it contains all the words in file"""
    line = line.replace("-", " ")
    li = line.split()
    for word in li:
        word = word.strip(string.punctuation +
                          string.whitespace).lower()
    new_li.extend(li)

def do_markov(new_li):
    """Returns a dictionary with keys as tuples (prefixes) and
    values as a list of (suffixes)"""
    h = dict()
    for i in range(len(new_li) - 3):
        prefix = new_li[i], new_li[i+1], new_li[i+2]   # prefix of order 2.
        # increasing the order of the prefix increases the correctness of the
        #output. order 3 now
        h.setdefault(prefix, []).append(new_li[i+3])
        #h[prefix] = h.get(prefix,[]).append(new_li[i+2])
    return h

def output_markov(h, word_count):
    prefix = choice(list(h.keys())) #h.keys() doesn't support indexing
    markov_str = prefix[0] + " " + prefix[1]
    for j in range(word_count-2):
        word = choice(h[prefix])
        markov_str = markov_str + " " + word
        prefix = shift(prefix,word)
    return markov_str

def shift(prefix, word):
    return prefix[1:] + (word,)

def get_input():
    file = input("Enter file path: ")
    count = int(input("Enter no. of words for output: "))
    return file,count

def main():
    while True:
        try:
            file, word_count = get_input()
            h = do_markov(process_file(file))
            print(output_markov(h, word_count))
            break
        except (KeyError, ValueError):
            print("Invalid Input!! or your file is smaller!!!")

if __name__ == "__main__": main()
    #k=do_markov(['us', 'want', 'job', 'grace'])
    #print(k)
    
