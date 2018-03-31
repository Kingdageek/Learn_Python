# num_palindromes.py
"""Some number palindrome pairs have their square roots mirroring each other e.g. 144 = 12 and 441 = 21. This program tries to return those pairs within a given range.
The program is not exactly performance-based (it took about 97 seconds for it to print pairs btw 112 and 100000), I just wanted a working program and the prog. standard
is crappy (I'm still a newbie though). The is_perfect_square() fn is cruft. Oh, I'm not going to do anything about this program. I'm just glad it worked."""
from pprint import pprint
from math import sqrt

"""def is_perfect_square(x):
    if x % sqrt(x) == 0:
        return True
    else:
        return False"""
user_input = int(input("Enter a number (upper limit) to check for palindromes btw 112 and that number: ")) # Require an upper limit from user

palin_set = set()   # a set to store the pairs | a list will be okay too, but I just started experimenting with sets
rep_li = []         # list to ensure no two pairs are similar

for i in range(112, user_input + 1):
    if i in rep_li: continue        # if the current iterating number is in rep_li, don't bother| Continue Iterating
    square_rt = sqrt(i)             # square root of current iterating number
    temp_li = list(str(i))          # some "temporary" list to enable us reverse the current iterating number
    temp_li.reverse()
    rev_num = int("".join(temp_li)) # a data type op
    rep_li.append(rev_num)          # add the reversed number to the list so if it reaches its turn, it knows it's already done

    if i == rev_num: continue       # WE DON'T WANT EXACT PALINDROMES LIKE 121 MIRRORING ITSELF
    

    #if is_perfect_square(rev_num):
    square_rt_rev = sqrt(rev_num)   
    sqr_inted_float = int(float(str(square_rt_rev))) #TO ENSURE THE SQUARE ROOT OF THE REVERSED NUMBER IS AN INTEGER
    sqr_li = list(str(sqr_inted_float)) # ANOTHER LIST TO ENABLE US REVERSE THAT SQUARE ROOT
    sqr_li.reverse()
    rev_sqrt = int("".join(sqr_li))     # THE RESULT OF REVERSING THE SQUARE ROOT OF THE REVERSED NUMBER
    
    if square_rt == rev_sqrt:           # IF THE SQUARE ROOT OF THE CURRENT I.N. IS EQUAL TO THE REVERSE OF THE SQUARE ROOT...
                                        # OF THE REVERSED NUMBER THEN, IT FITS THE DESCRIPTION OF WHAT WE'RE LOOKING FOR
        palin_set.add((i,rev_num))      # ADD THE PAIR TO OUR SET
pprint(palin_set)                       # INTELLIGENTLY PRINT OUR SET
    
