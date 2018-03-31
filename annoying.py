import random
from copy import deepcopy


def rand():
    li = ["D", "P", 'P', 'I', 'I', 'E', '0', 'N', 'S', 'A', 'T', 'D']
    random.shuffle(li)
    """lst = deepcopy(li)
    if (lst[0] == li[0] or lst[1] == li[1]or lst[2] == li[2] or lst[3] == li[3] or
        lst[4] == li[4] or lst[5] == li[5] or lst[6] == li[6] or lst[7] == li[7] or lst[8] == li[8] or lst[9] == li[9] or
        lst[10] == li[10] or lst[11] == li[11] ):
        continue"""
        
    return "".join(li)

for i in range(0,5760):
    print(rand())
    if rand() == "DISAPPOINTED":
        break
    
