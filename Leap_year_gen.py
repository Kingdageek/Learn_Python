def leap_year_gen(start,stop):
    step = -1 if start > stop else 1

    print("The Leap year(s) are: \n")
    count = 0
    for year in range(start,stop,step):
        
        if ((year % 4 == 0 and year % 100 != 0) or
            ((year % 4 == 0 and year % 100 == 0) and year % 400 == 0)):
            
            print(f"{year}\n")
            count+=1

    format = "There are %2d leap years between %5d and %5d"
    values = (count,start,stop)
    print(format%values)

print("If you want B.C.E years, precede it with a minus...\n")
while True:
    
    user_in = input("Enter the first year: ")
    user_in1 = input("Enter the second year: ")

    try:
        user_val = int(user_in)
        user_val1 = int(user_in1)
        assert (-500 <= user_val <= 3000) and (-500 <= user_val1<= 3000), "Year\
 shouldn't be less than -500 or greater than 3000"

        leap_year_gen(user_val, user_val1)
        break
    except ValueError as err:
        print(err)
        print("Enter Correctly!!")
    except AssertionError as err1:
        print(err1)
        
    

