from datetime import datetime as dt

def get_bd():
    bd = input("Enter birthday in the format <YY-MM-DD>: ")
    return bd

def delta_bd(birthday, now):
    delta = birthday - now
    seconds = delta.total_seconds()
    minutes = seconds / 60
    hours = minutes / 60
    days = hours / 24
    return days, hours, minutes, seconds

def process_bd(bd):
    li = [int(i) for i in bd.split("-")]
    year, month, day = li
    birthday = dt(year, month, day)
    now = dt.now()
    assert now > birthday
    age = (now - birthday).days//365
    birthday = birthday.replace(year= now.year)
    if now < birthday: return delta_bd(birthday, now)
    elif now == birthday: print("happy birthday!!")
    else:
        birthday = birthday.replace(year= now.year + 1)
        return (age,) + delta_bd(birthday, now) 

def main():
    while True:
        try:
            age, days, hours, minutes, seconds = process_bd(get_bd())
            print("You are %2d years old!" % age)
            print("Your next birthday is in: ")
            print("%.4f days, %.4f hours,\
%.4f minutes, %.4f seconds" % (days, hours, minutes, seconds))
            break
        except (ValueError, AssertionError):
            print("INVALID INPUT | YOU BIRTHDAY MIGHT BE IN THE FUTURE | FOLLOW\
 OUR FORMAT")

if __name__ == "__main__": main()
