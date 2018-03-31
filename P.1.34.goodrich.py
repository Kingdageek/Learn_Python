import random
li = ["I will never spam my friends again"] * 100
a,b = -len(li),-1               #2 ints to choose a random element from in li
c,d = 0,len(li[0])-1            #2 ints to choose a random letter from in one li element
check = []
for i in range(8):
    index = random.randint(a,b)
    index2 = random.randint(c,d)
    while index in check:
        index = random.randint(a,b)
    while index2 in check:
        index2 = random.randint(c,d)
    check.append(index)
    check.append(index2)
    li[index] = li[index][:index2] + li[index][index2+1:]
for i in range(1,101):
    print(str(i)+". "+ li[i-1])
