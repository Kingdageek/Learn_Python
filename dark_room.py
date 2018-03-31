#dark_room.py
from Guess_game import enter_cmd
def help():
    print("There are 4 rooms, Just flow with the game")
    print("type 'play' to play 'a dark room'")
    print("type 'quit' to quit playing")
    print("type 'help' to see this message again")

def play():
    while True:
        print("You enter a dark room with four doors. Do you go through door #1, door #2, door #3 or door #4")
        door = input("> ")
        if door == "quit":
            return
        elif door == "help":
            help()
            return
        elif door == "1":
            print("You see a giant Python curling itself around a man. What do you do?")
            print("1. Run out\n2. Try to save the man")
            python = input("> ")
            if python == "1":
                print("You're a bloody coward!!!. We'll see how you fare soon.")
                continue
            elif python == "2":
                print("The Python gets angry and squeezes life out of you... Good Job!")
                return
            else:
                print("doing %s is probably better" % python)
                return
        elif door == "2":
            print("You see people partying and drinking booze. What do you do?")
            print("1. join them to party\n2. Try another room")
            party = input("> ")
            if party == "1":
                print("As soon as you enter, you discover they're vampires and they suck all of your blood. Good job!")
                return
            elif party == "2":
            	print("You HOPPER!!!! we'll soon see how you fare SUCKER!!!")
            	continue
            else:
                print("doing %s is probably better" % party)
                return
        elif door == "3":
            print("You see a bear eating cake. What do you do?")
            print("1. take the cake from the bear\n2. Scream at the bear")
            bear = input("> ")
            if bear == "1":
                print("The bear eats your face. Good Job!")
                return
            elif bear == "2":
                print("The bear eats your balls if you're a guy or your boobs for the other gender. Good job!")
                return
            else:
                print("Doing %s is probably better." % bear)
        elif door == "4":
            print("You stare into an abyss of lost souls. What do you do?")
            print("1. piss into the abyss\n2.run out in fear")
            abyss = input("> ")
            if abyss == "1":
                print("While pissing, you slip and fall into the abyss. Good Job!")
                return
            elif abyss == "2":
                print("Scaredy Cat!!! You fall on a knife and die!")
                return
            else:
                print("I guess doing %s is probably better" % abyss)
                return
        else:
            print("You fall on a knife and DIE!!!!!")
            return

def main():
    print("WELCOME TO A DARK ROOM. DARK THE KEYWORDD\n")
    while True:
        print("THIS IS A DARK ROOM OPTIONS MENU...\n")
        cmd = enter_cmd()
        if cmd == "play":
            play()
        elif cmd == "help":
            help()
        elif cmd == "quit":
            return
        else:
            print("INVALID COMMAND | ENTER 'help' for help")

if __name__ == "__main__": main()
