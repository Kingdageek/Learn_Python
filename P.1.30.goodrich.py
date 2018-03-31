
def times(num):
    """ times computes the number of times one must
repeatedly divide "num" by 2 before getting a value less than 2"""
    count= 0
    while True:
        num = num/2
        count += 1
        if num < 2:
            return count
            

while True:
    user_in = input("Enter a postive integer greater than 2: ")
    try:
        user_int = int(user_in)
        assert user_int > 2
        print("The number of times", str(user_int), "can be repeatedly divided by",
              "2 before getting a value < 2 is", str(times(user_int)))
        break
    except (ValueError, AssertionError):
        print("Invalid input, Enter correctly")
        


        
            
