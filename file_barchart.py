#file_barchart.py
from markov_analysis import process_file

def get_input():
    return input("Enter a file path: ")

def print_barchart(d):
    dlist = list(zip(d.values(), d.keys()))
    dlist.sort(reverse=True)
    for value, key in dlist:
        print("\n" + key + ": ", end = "")
        for i in range(value):
            print("X", end ="")
        print(" | (%.2d)" % value, end = "")

def count_letter():
    file_list = process_file(get_input())
    long_string = "".join(file_list).lower()
    hist = {}
    for i in long_string:
        #hist.setdefault(i, 0) + 1    #if i not in dict, set i to count 1
        hist[i] = hist.get(i, 0) + 1  #if i is encountered again increment it's count
    return hist

def main():
    import string
    #letters = string.ascii_lowercase
    print_barchart(count_letter())

if __name__ == "__main__": main()
