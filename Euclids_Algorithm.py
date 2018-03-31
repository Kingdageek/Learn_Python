#Euclids_Algorithm.py
# Program to implement the Euclid's algorithm and obtain GCD


def euclids_algo(x,y):
    if y == 0:  # if the remainder ever becomes 0, return the number
        return x
    else:
        r = x % y
        return euclids_algo(y,r)


def getinput():
    user_in1 = int(input("Enter the first number: "))
    user_in2 = int(input("Enter the second number: "))
    return user_in1, user_in2


def main():
    while True:
        try:
            num1, num2 = getinput()

            max_num, min_num = max(num1, num2), min(num1, num2)
                
            print("The gcd of %4d and %4d is %4d" % (num1, num2, euclids_algo(max_num, min_num)))
            break
        except ValueError as err:
            print(err)
            print("Please enter valid integers!!!!!\n")

if __name__ == "__main__": main()
