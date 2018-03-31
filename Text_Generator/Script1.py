import random, string

vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"
letters = string.ascii_lowercase

while True:
    userChoice_1 = input("What letter do you want to occupy the first position? Enter 'v' for vowels, 'c' for consonants, \
    'l' for any letter or you could just type the letter you want...")
    userChoice_2 = input("What letter do you want to occupy the second position? Enter 'v' for vowels, 'c' for consonants, \
    'l' for any letter or you could just type the letter you want...")
    userChoice_3 = input("What letter do you want to occupy the third position? Enter 'v' for vowels, 'c' for consonants, \
    'l' for any letter or you could just type the letter you want...")

    concat = userChoice_1+userChoice_2+userChoice_3
    # To print the user's choices
    print("You entered: "+concat)

    # To validate the user's Inputs
    if userChoice_1 in letters and userChoice_2 in letters and userChoice_3 in letters :

        def generator():

        # To test if the user Inputs a vowel, consonant or letter option and take action accordingly

            if userChoice_1=="v":
                letter1 = random.choice(vowels)
            elif userChoice_1=="c":
                letter1 = random.choice(consonants)
            elif userChoice_1=="l":
                letter1= random.choice(letters)
            else:
                letter1 = userChoice_1

            if userChoice_2=="v":
                letter2 = random.choice(vowels)
            elif userChoice_2=="c":
                letter2= random.choice(consonants)
            elif userChoice_2=="l":
                letter2 = random.choice(letters)
            else:
                letter2 = userChoice_2

            if userChoice_3=="v":
                letter3 = random.choice(vowels)
            elif userChoice_3=="c":
                letter3= random.choice(consonants)
            elif userChoice_3=="l":
                letter3 = random.choice(letters)
            else:
                letter3 = userChoice_3

            name= letter1+letter2+letter3
            return name


        # Loop to execute function ten times i.e. print 10 words
        for i in range(10):
            print(generator())
        break
    else:
        print("Some/all of your inputs are not entered\a correctly ...\n\nPlease enter correctly...\n")
        continue
