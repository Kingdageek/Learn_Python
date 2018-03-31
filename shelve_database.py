import shelve
def store_person(db):
    """Query user for details to store in database"""
    pid = input("Enter your unique ID: ")
    person = {}
    person["name"] = input("Enter your name: ")
    person["age"] = input("Enter your age: ")
    person["phone"] = input("Enter your phone: ")
    db[pid] = person

def lookup_person(db):
    """Query user for the ID and desired field and returns
    the value appropriate to field"""
    pid = input("Enter your ID: ")
    field = input("Enter the info you'd like to know? (name, age, phone): ").strip().lower()

    print(field.capitalize()+ ": " + db[pid][field])  #field with first letter capitalized

def print_help():
    print("The commands are: ")
    print("Enter 'store' to store details in database")
    print("Enter 'look' to lookup details already in database")
    print("Enter 'quit' to close and exit")
    print("Enter '?' for help; essentially reprinting this message")

def enter_command():
    cmd = input("Enter command (press '?' for help): ").strip().lower()
    return cmd
    
def main():
    database = shelve.open("example.dat")  # shelve database object... extension '.dat'
    try:
        while True:
            cmd = enter_command()
            if cmd == "store":
                store_person(database)
                print("Congratulations! Person now stored in database")
            elif cmd == "look":
                lookup_person(database)
            elif cmd == "?":
                print_help()
            elif cmd == "quit":
                return
            else:
                print("This command is not available, Enter '?' for help")
    finally:
        database.close()    # Close shelve object

if __name__ == "__main__": main() #if it's run as a script on its own. It can also be im
                                        # ported as a module
            
    
    
