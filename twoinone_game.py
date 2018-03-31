#twoinone_game.py
import dark_room
import Guess_game

def help():
    print("This is a two in one game!!\nThe adventure 'DARK ROOM' and the logical 'GUESS GAME'")
    print("Enter <D> to play 'DARK ROOM' | <G> for 'GUESS GAME'")
    print("As usual, Enter <quit> to quit and <help> to see this message again")

def main():    
    while True:
        print("WELCOME TO THE 2 IN 1 ABSOLUTE TEXT-BASED GAME\n")
        cmd = Guess_game.enter_cmd()
        if cmd == "d":
            dark_room.main()
        elif cmd == "g":
            Guess_game.main()
        elif cmd == "help":
            help()
        elif cmd == "quit":
            return
        else:
            print("INVALID COMMAND | ENTER <help> FOR HELP...")

if __name__ == "__main__": main()
