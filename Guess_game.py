#Guess_game.py
import random

def help():
    print("I'll think of a number btw 0 and 51 and you'll have to guess it")
    print("if your guess is lower or higher than the number, I'll tell you so you'll try to guess appropriately")
    print("enter 'play' to play")
    print("enter 'quit' to quit")
    print("type 'help' to see this message again")

def play():
    print("I have a number in mind, try to guess it...")
    com_number = random.randint(1,50)
    
    while True:
        try:
            user_guess = input("Enter your guess: ").strip().lower()
            if user_guess == 'quit':
                return
            elif user_guess == 'help':
                help()
                return
            else:
                user_guess = int(user_guess)
                assert 0 < user_guess < 51
                if user_guess == com_number:
                    print("You've guessed right!!")
                    break
                elif user_guess < com_number:
                    print("Your guess is less than the number, keep guessing.")
                elif user_guess > com_number:
                    print("Your guess is greater than the number, keep guessing.")
            
        except (TypeError, ValueError, AssertionError):
            print("INVALID INPUT | TYPE 'help' for help")

def enter_cmd():
    cmd = input("Enter command (type 'help' for help): ").strip().lower()
    return cmd
    

def main():
    print("WELCOME TO GUESS_GAME.PY!\n"); 
    while True:
        print("THIS IS THE GUESS_GAME OPTIONS MENU...\n")
        cmd = enter_cmd()
        if cmd == "play":
            play()
        elif cmd == "help":
            help()
        elif cmd == "quit":
            return
        else:
            print("INVALID INPUT... ENTER 'help' for help")

if __name__ == "__main__": main()
