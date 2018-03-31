from pprint import pprint
from random import shuffle
li = ["c","a","t","d","o","g"]
result = []

def catdog_gen():
    count = 0
    for i in range(len(li)):
        for i in range(len(li)):
            for i in range(len(li)):
                for i in range(len(li)):
                    for i in range(len(li)):
                        for i in range(len(li)):
                            shuffle(li)
                            st = "".join(li)
                            if st not in result:
                                result.append(st)
                                count+=1
    pprint(result)
    print(count)
"""def catdog_gen(n):
    if len(result) <= n:
        shuffle(li)
        st = "".join(li)
        if st not in result:
            result.append(st)
        catdog_gen(n-1)
    pprint(result)"""
        

catdog_gen()
