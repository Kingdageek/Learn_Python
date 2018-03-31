user_in = input("Enter a string: ")

def count_string(s):
    lis = s.split()
    li = [i.lower() for i in lis]
    non_rep = []
    for i in li:
        count = 0
        for j in range(len(li)):
            if i == li[j]:
                count += 1
        if i not in non_rep:
            print("'"+ i + "'" + " appears " + str(count) + " time(s)")
            non_rep.append(i)

count_string(user_in)
