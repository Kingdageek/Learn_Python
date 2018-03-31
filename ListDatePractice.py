# List to hold the months of the year
months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']

# List to hold the appropriate day suffix
days_endings = ['st', 'nd', 'rd'] + 17 * ['th'] + \
               ['st', 'nd', 'rd'] + 7 * ['th']  + \
               ['st']

#To collect the values from the user
month = input("Enter Month (0-12): ")
year = input("Enter Year: ")
day = input("Enter Day (0-31): ")

month_num = int(month)
day_num = int(day)

month = months[month_num - 1]
day = str(day_num) + days_endings[day_num - 1]

print("The date you gave is: " + month + ', ' + day + " " + year)
