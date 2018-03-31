#Program to obtain Kaprekar's constant 6174 from a 4 digit number
KAPREKAR_CONST = 6174
user_in = ""
while True:
    user_in = input("Enter a 4 digit number: ")

#To confirm that the user entered a valid number, a little defensive programming
    
    try:
        number = int(user_in)

        assert number > 0, "The number must be positive"

        #Remove any preceding zero from the user's input. As we know, 00009
        #has 5 digit spaces but it is the same as the number 9.
        
        if user_in[0] == "0":
            user_in = user_in.lstrip("0")

        # Conditional to ensure that the user's input is not > 4, does not evaluate to zero
        # and if it's 4, it isn't a rep-digit
            
        if len(user_in) > 4 or number == 0 or (len(user_in) == 4 and user_in[0] == user_in[1] == user_in[2] == user_in[3]):
            print("Do you really want Kaprekar to work or not?\n Please Enter a 4, 3, 2 or 1 non-zero, non-repeating-digit number!")
            continue
        
        break
    
    except ValueError as err:
        print(err)

        print(user_in, "is not a valid number\nEnter a valid number!!")
    except AssertionError as err1:
        print(err1)
        print("Please enter correctly...")


count = 1
while True:
    #Block to pad user input with preceding zeroes if it's not a 4 digit number
    while len(user_in) != 4:
        user_in = '0' + user_in
    
    sort_user_in = "".join(sorted(user_in))
    rev_user_in = "".join(reversed(sort_user_in))
    sort_user_int= int(sort_user_in)
    rev_user_int= int(rev_user_in)

    boolsit = rev_user_int - sort_user_int

    print("IN ASCENDING ORDER,", user_in, "is", sort_user_in)
    print("IN DESCENDING ORDER,", user_in, "is", rev_user_in)
    print(rev_user_in + " - " + sort_user_in + " = " + str(boolsit) + "\n\n")
    
    if boolsit == KAPREKAR_CONST:
        print("Kaprekar's Constant 6174 reached after", count, "iterations", sep = "_")
        break
    else:
        user_in = str(boolsit)
        count+=1
        

    
    

