#rockpaperscissors.py
from random import choice
from Guess_game import enter_cmd

def help():
    print("------------------------------------------------------------------")
    print("ENTER <PLAY> TO PLAY ROCKPAPERSCISSORS...")
    print("ENTER <QUIT> TO STOP PLAYING.......")
    print("ENTER <HELP> TO SEE THIS MESSAGE AGAIN!")

def check(com, user):
    """Logic of the entire game.

    returns 2 for a DRAW, 1 if USER WINS, 0 IF COM WINS
    """
    if com == user:
        print("I chose same :", com)
        print("A DRAW. AGAIN...")
        return 2
    elif com == "rock" and user == "paper":
        print("YOU WIN!! I chose", com)
        return 1
    elif com == "rock" and user == "scissors":
        print("YOU LOSE!! I chose", com)
        return 0
    elif com == "paper" and user == "rock":
        print("YOU LOSE!! I chose", com)
        return 0
    elif com == "paper" and user == "scissors":
        print("YOU WIN!! I chose", com)
        return 1
    elif com == "scissors" and user == "rock":
        print("YOU WIN!! I chose", com)
        return 1
    elif com == "scissors" and user == "paper":
        print("YOU LOSE!! I chose", com)
        return 0

def round_results():
    while True:
        try:
            rounds = input("Enter the number of rounds you'd like to\
 play for: ").strip().lower()
            if rounds == "quit": return
            elif rounds == "help":
                help()
                return
            else: rounds = int(rounds)
            com, user, draw =0, 0,0
            for i in range(rounds):
                print("\nROUND %d\n" % (i+1))
                k = play() # returns check() or None
                if k == 1:
                    user +=1
                elif k == 0:
                    com +=1
                elif k == 2:
                    draw += 1
                else: return
            print("IN %2d GAMES, WE DREW %2d TIME(S)..." % (rounds, draw))
            print("THE EVENTUAL SCORE IS: COM: %2d | USER: %2d" %(com, user))
            if com > user:
                print("YOU LOSE OVERALL!!!")
            elif com == user:
                print("IT'S A DRAW!!! | NO WINNER")
            else:
                print("YOU WIN OVERALL!!!")
            break
        except ValueError as err:
            print(err)
            print("INVALID INPUT!!!")

def play():                                                                                                                                                                                 
    print("<ROCK> <PAPER> OR <SCISSORS>...")
    mapp = ["rock", "paper", "scissors"]
    com_choice = choice(mapp) # I felt choice would be faster than randint
    
    while True:         
            user_guess = input("Enter your guess: ").strip().lower()
            if user_guess == 'quit':
                return
            elif user_guess == 'help':
                help()
                return
            if user_guess not in mapp:
                print("INVALID INPUT!!! ENTER <HELP> FOR HELP")
            else:
                return check(com_choice, user_guess)
                
def main():
    print("WELCOME TO ROCKPAPERSCISSORS.PY!"); 
    while True:
        print("\nTHIS IS THE OPTIONS MENU...\n")
        cmd = enter_cmd()
        if cmd == "play":
            round_results()
        elif cmd == "help":
            help()
        elif cmd == "quit":
            return
        else:
            print("INVALID INPUT... ENTER 'help' for help")

if __name__ == "__main__": main()

    
            
