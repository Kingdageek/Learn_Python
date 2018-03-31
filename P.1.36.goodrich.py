user_in = input("Enter a string: ")

def count_string(s):
    """count_string takes in a string argument, a sentence
    separated by whitespace and returns the number of times
    a word appeared in the sentence"""
    lis = s.split()
    li = [i.lower() for i in lis]
    non_rep = []
    for i in li:
        count = 0
        for j in range(len(li)):
            if i == li[j]:
                count += 1
        if i not in non_rep:
            if count == 1:
                print("'{value}' appears {count: 2d} time".format(count= count, value= i))
            else:
                print("'{value}' appears {count: 2d} times".format(count= count, value= i))
            non_rep.append(i)
         

count_string(user_in)
