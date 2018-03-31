# breakfile.py
import string

f = input("Enter file path: ")
li = []
with open(f) as file:
    while True:
        line = file.readline()
        if not line: break
        li.extend(line.split(" "))

distinct = set()
for l in li:
    if l in string.punctuation+string.whitespace:
        li.remove(l)
    else:
        for s in string.punctuation+ string.whitespace:
            l = l.replace(s, "")
        l = l.lower()
        distinct.add(l)
        
        
print("There are %d words in the file: " % len(li))
print("There are %d distinct words in the file: " % len(distinct))
print("They are:")
for i in distinct: print(i)
    
