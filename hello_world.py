import datetime

def print_menu():
    '''A function for printing the menu'''
    print ('''1. add
2. delete
3. print
4. quit''')

def fancy_print_menu(items):
    '''A fancier function for printing menus'''
    for i,s in enumerate(items):
        print (f"{i+1}. {s}")

# Array for menu items
items = ["add", "delete", "print", "quit"]

# Used for mapping weekdays to strings
weekdays = {
    1:"Monday", 
    2:"Tuesday", 
    3:"Wednesday",
    4:"Thursday",
    5:"Friday",
    6:"Saturday",
    7:"Sunday"}

# Main starts here
fancy_print_menu(["add", "delete", "print", "quit"])
x = input("Choose:")

print ("I don't want to " + items[int(x)-1])

datestr = input("Give me a date: ")

numbers = datestr.split(".")

if len(numbers) != 3:
    print ("ERROR")
else:
    day = int(numbers[0])
    month = int(numbers[1])
    year = int(numbers[2])
    indate = datetime.date(year, month, day)
    print ("Your date was a " + weekdays[indate.isoweekday()])

# Ett mer magiskt exempel
day, month, year = [int(p) for p in datestr.split(".")]