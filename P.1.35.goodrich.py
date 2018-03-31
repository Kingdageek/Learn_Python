"""IF THERE ARE MORE THAN 23 PEOPLE IN A ROOM, IT'S A MORE THAN 50% PROBABILITY THAT TWO(2) OF THEM HAVE THE SAME BIRTHDAYS - THE BIRTHDAY PARADOX.
THIS PROGRAM TRIES TO TEST THAT PARADOX FOR 20 SAMPLES (FOR 5 PEOPLE TO 100 PEOPLE WITH INCREMENTS OF THE ORDER OF 5)"""
from random import randint
people = [i for i in range(5,101,5)]

def birthday_gen(n):
    """THIS TAKES A NUMBER(n) AND RETURNS A LIST OF BIRTHDAYS OF LENGTH 'n'"""
    months = ["January","February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"]
    day_endings = ["st","nd",'rd']+['th']*17 + ['st','nd', 'rd'] + ['th']*7 + ['st']
    birthdays = []
    
    for i in range(n):
        month = randint(1,12)
        year = randint(1975,2014)

        #To generate for "day"
        day_up_lim = 0
        day_down_lim = 1
        #Leap year test to know how many feb days
        year_condition = ((year % 4== 0 and year % 100 != 0) or ((year % 4 == 0 and
                                                                 year % 100 == 0) and
                                                                year % 400 == 0))
        #The February special
        if month == 2 and year_condition:
            day_up_lim = 29
        elif month == 2:
            day_up_lim = 28
        elif month == 4 or month == 6 or month == 9 or month == 11:
            day_up_lim = 30
        else:
            day_up_lim = 31

        day = randint(day_down_lim,day_up_lim)
        birthday = months[month - 1] + " " + str(day) + day_endings[day-1]
        birthdays.append(birthday)

    return birthdays

def birthday_stack():
    """RETURNS A TWO DIMENSIONAL LIST OF GENERATED BIRTHDAYS FOR OUR SAMPLES"""
    birthday_results = []
    for i in people:
        birthday_results.append(birthday_gen(i))
    return birthday_results

def count(some_list):
    """TAKES A 2D LIST AND RETURNS A TUPLE OF TWO 2D LISTS (THE 2D LIST OF COUNTS OF SAMPLES
    AND THE 2D LIST OF ANALYSIS OF THOSE COUNTS) . IT COUNTS THE NUMBER OF TIMES A BIRTHDAY OCCURS
    IN THE RESULT OF ONE SAMPLE"""
    count_same_birthday = []
    count_birthday_analysis = []
    for element in some_list:
        li = []
        count_val = []
        count_analysis = []
        for value in element:
            count = 0
            for i in range(len(element)):
                if value == element[i]:
                    count+=1
            if value not in li:
                count_val.append(count)
                if count == 1:
                    count_analysis.append(value + " appears once.")
                else:
                    count_analysis.append(value + " appears " + str(count) + " times.")
                li.append(value)
        count_same_birthday.append(count_val)
        count_birthday_analysis.append(count_analysis)
    return count_same_birthday, count_birthday_analysis

def test():
    count_same_bd, count_bd = count(birthday_stack())
    test = [None] * len(people)

    for i in range(len(people)):
        for k in range(len(count_same_bd[i])):
            if people[i] < 23 and count_same_bd[i][k] == 1:
                test[i] = "MUCH EXPECTED: still follows the paradox" 
            elif people[i] > 23 and count_same_bd[i][k] == 1:
                test[i] = "PROBABLE, still follows the paradox"
            elif people[i] < 23 and count_same_bd[i][k] > 1:
                test[i] = "RARE. Had a probability of occurring below half."
                break
            elif people[i] > 23 and count_same_bd[i][k] > 1:
                test[i] = "EXPECTED: This had an above 50% chance of occurring, it follows the paradox"
                break
    return test

def output_findings():
    birthday_results = birthday_stack()
    count_same_birthday, count_birthday_analysis = count(birthday_results)
    test_list = test()
    people_string = [str(i) for i in people]

    for i in range(len(people)):
        print("The results for " + str(people[i]) + " people are: ")
        for j in range(people[i]):
            print(birthday_results[i][j])
        print()
        for k in range(len(count_birthday_analysis[i])):
            print(count_birthday_analysis[i][k])
        print()
        print("The CONCLUSION for this particular random birthday generation for " + people_string[i] + " people is: ")
        print(test_list[i])
        print()

output_findings()
    
        
        
