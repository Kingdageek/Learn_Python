# intellect_googol.py
import numpy as np
import matplotlib.pyplot as plt

# to load the data

num_chats = []
members = []

with open("../intellect_googol.csv", "r") as file:
	for line in file:
		x,y = line.split(",")
		members.append(x)
		num_chats.append(int(y))
		
# convert to a numpy array
num_chats = np.array(num_chats)
members = np.array(members)

avg = num_chats.mean()
total = num_chats.sum()

member_percent = []
for k in num_chats:
	f = k / total * 100
	member_percent.append(f)
	
print("OUR DATA IN 2 MONTHS")
for i in range(len(num_chats)):
	print("%20s: %4d" %(members[i], num_chats[i]))

print("\nRATIO IN PERCENT OF INDIVIDUAL MEMBER SENT MESSAGES TO TOTAL SENT IN 2 MONTHS")

for i in range(len(num_chats)):
	print("%20s: %.2f" %(members[i], member_percent[i]))
print("\nAVERAGE IS: %.2f \nTOTAL CHATS: %5d"% (avg, total))
# plot the first version

plt.pie(num_chats)
plt.show()




		 