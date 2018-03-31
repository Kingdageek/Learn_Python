

low_limit = input("Enter lower limit number:")
upp_limit = input("Enter upper limit number:")
x = int(low_limit)
y = int(upp_limit)
total = 0

for i in range(x, y+1):
    total +=i

print("the sum is: " + str(total))
