#zipf_data.py

"""zipf law shows a relationship between the rank(1 for most common word)
of a word in a language and it's frequency.
f = c*r**-s. logf = logc - s*logr (y = mx+c). This program outputs data for
logf and logr (rank). s and c are params dependent on the language and text"""

import math
from file_barchart import get_input
from markov_analysis import process_file

def get_frequency(li):
    h = dict()
    for i in li:
        h[i] = h.get(i,0) + 1
    li = list(zip(h.values(), h.keys()))
    li.sort(reverse=True)
    return li

def get_rank(li):
    """if previous word and current word have the same frequency, their rank
    should be the same. li is a sorted list of tuples."""
    rank = [1]
    for i in range(1, len(li)):
        if li[i-1][0] == li[i][0]:
            rank.append(rank[-1])
        else: rank.append(rank[-1] + 1)
    return rank

def output_data(li,ra):
    print("     %10s %s %s  %s   %s" %( "WORD", "FREQUENCY", "RANK",
                                    "LOG(F)", "LOG(R)"))
    print("-----------------------------------------------------------------")
    print()
    for i in range(len(li)):
        word = li[i][1]
        freq = li[i][0]
        rank = ra[i]
        logf = math.log(freq)
        logr = math.log(rank)
        print("%3d. %10s  %7d  %4d  %.5f  %.5f" % (i+1, word, freq, rank, logf, logr))

def main():
    while True:
        try:
            li = process_file(get_input())
            freq_li = get_frequency(li)
            rank_li = get_rank(freq_li)
            output_data(freq_li, rank_li)
            break
        except IOError as err:
            print(err)

if __name__ == "__main__": main()
