#Dictionary to hold the contents of addressbook
contacts = {
    "Alice": {
        "phone": 98434,
        "addr": "26 Afolabi Obe"
        },
    "Nonso": {
        "phone": 894434,
        "addr": "26 Alago str"
        },
    "Emeka": {
        "phone": 892334,
        "addr": "26 Africa str"
        }
    }
#labels to be used for printing in full
labels = {
    "phone": "phone-number",
    "addr": "address"
    }
name = input("Enter Name: ")

while True:
    request = input("Enter (p) for phone-number or (a) for address: ")

    if request == "p": key = "phone"
    elif request == "a": key = "addr"
    else: print("You entered wrongly, sorry no defensive programming today, Bye-Bye. \nJoke! ENTER CORRECTLY! "); continue
        
    if name in contacts:
        print("{}'s {} is {}".format(name, labels[key], contacts[name][key]))
        break
    else:
        print("'{}' not in this address book".format(name))
        break
