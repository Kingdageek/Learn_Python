import random, string
letters = string.ascii_lowercase
vowels = "aeiou"
def create_words():
    letter1 = random.choice(letters)
    letter2 = random.choice(vowels)
    letter3 = random.choice(letters)
    letter4 = random.choice(letters)

    word = letter1+letter2+letter3+letter4+ " "
    return word

with open("Create_File.txt", "w+") as file:
    for i in range(100):
        content = file.write(create_words())
