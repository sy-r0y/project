# Operation Precedence
# BODMAS
'''
    Exponentiation
    Multiplication/Division
    Addition/Substraction
'''
# value = 10 + 2 * 3
# value = 10 + 2 - 3
# value= 10 ** 2 - 3 * 5
# print(value)
###########################################################
# x= 2.51
# print(round(x))
# print(abs(-6))
#######-------*******##########################
'''
import math

print(math.ceil(4.1))

print(math.floor(4.1))

print(math.comb(5 , 10))'''
# ********************************************************

# STATEMENTS
# if if else

# is_hot=False
# is_cold=True
# a=5
# b=6

# if is_hot:
#   print("It's a Hot day")
# elif is_cold:
#   print("Not a hot day")
# else:
#   print("Lovely Day Boy")
# print("Enjoy your Day")
''' temp=input("Enter Temperature in Celsius- ")
temp=int(temp)
if temp>20:
    print("It's a Warm Day")
elif temp>30:
    print("It's a Hot Day")
else:
    print("It's a Cold Day")'''

# ******************************************************#


''' print("Price of House is $1000000")

buyer_credit_good = input('Credit Score: ')

buyer_credit_good = int(buyer_credit_good)

if buyer_credit_good >= 500:
    print("Credit is Good")
    print("Deposit 10% of Money")
    down_payment = 0.1 * 1000000
    # print(f"Deposit {down_payment} amount")
else:
    print("Credit is not Good")
    print("Deposit 20% of Money")
    down_payment = 0.2 * 1000000
    # print(f"Deposit {down_payment} amount")

print(f'Down Payment is {down_payment} Dollars')

print("Happy Hunting Sebastian")
'''

# ****************************************** #

''' income=input("Enter Annual Salary - ")
income=int(income)

criminal_record=False

if not criminal_record and income<=10000:
    print("Not Eligible For Loan cuz you broke")
elif not criminal_record and income>10000 and income<=100000:
    print("Eligible for loan @ 10%")
elif not criminal_record and income>100000:
    print("Eligible for loan @ 5%")
else:
    print("Stay away criminal")
'''

# ----------------------------------------------------------------#

''' name=input("Enter Name : ")

name_length= len(name)

#print(name_length)

if name_length < 3:
    print("Name Too Short")
elif name_length>50:
    print("Name Too Long")
else:
    print("Name Accepted!")
    print(f"Hi {name}")
'''
# -------------------------------------------------------------
''' weight=input("Enter Weight - ")
weight=int(weight)

format=input("Pounds(P) or Kilos(K)? ") 

''' ''' if format=='p' or format=='P':
    weight=weight/2.205
    print(f"Weight in Kilo is {weight}")
elif format=='K' or format=="k":
    weight=weight*2.205
    print(f"Weight in Pound is {weight}")
else:
    print("Invalid Format. Pres K/k or P/p only")
''' '''
if format.upper() == "P":
    weight=weight/2.205
    print(f"Weight in Kilo is {weight}")
elif format.upper()=="K":
    weight=weight*2.205
    print(f"Weight in Pound is {weight}")
else:
    print("Invalid Format. Press K/k or P/p")

'''

# --------------------------------------------------------------------

# While Loops


# i = 1
# while i<=5:
#    print("*" * i)
#    i+=1
# print(f"Value of i: {i}")

'''
secret_number = 9
guess_count = 1
guess_limit = 3
#remaining_tries = guess_limit

while guess_count <= guess_limit:
    guess = int(input("Guess The Number: "))
    if guess == secret_number:
        print("Correctly Guessed!!!")
        #exit()
        break
    else:
        #remaining_tries -= 1
        guess_limit -= 1
        print(f"{guess_limit} more chance remaining")

else:
    print("You Failed Loser :D ")
'''
# CAR GAME

'''
command = input("Enter Command - ")
command = command.lower()

if command == "quit":
    #breakpoint()
    exit()
elif command == "start":
    print("Car Started .. Ready To Rumble!!")
elif command == "stop":
    print("Car Stopped!")

'''
'''
i = 1

while i<6:
    print('*' * i)
    i+=1

print("Done") '''
'''
secret_number=9
tries=1
max_tries=3

while tries <= max_tries:
    guess=int(input("Guess Secret Number: "))
    #guess=int(guess)

    if guess == secret_number:
        print("Successful Guess!")
        break
    else:
        print("Wrong Guess! Try Again")
        tries+=1
    #tries+=1
if tries==4:
    print("You have exhausted your options!")
'''
'''
while(1==1):
    command=input(" >  ").lower()
    start_count = 0
    stop_count = 0
#    command=command.lower()
    if command == "start":
        if start_count > 0:
            print(' >  Car Already Running')
        else:
            print(" >  Car Started... Ready To Roll")
            start_count += 1
    elif command == "stop":
        if stop_count > 0:
            print(" >  Car Already Stopped!!")
        else:
            print(" >  Car Stopped!!")
            stop_count += 1
    elif command == "help":
        print(" >  Commands are Start, Stop, Quit, Help")
    elif command=="quit":
        exit()
    else:
        print(" >  Command Not Recognized")
'''

# For Loop (https://youtu.be/_uQrJ0TkZlc?t=6100)
# content='python'
'''
list = ['first', 'second', 'third', 'fourth']
#inner_list = [1,2,3,4,5]

for item in list:
    for inner in range(5, 100, 20):
        print(inner)
    print(item)
'''
'''
cart=[20, 30, 40, 50] # LIST
#cart.append(100)
total_price=0
for price in cart:
    total_price += price
    #print("Price:- " + price.__str__())
    print(f"Price:- {price}")
#print("Total Price:- " + total_price.__str__())
print(f'Total Price:- {total_price}')
'''
'''
xxxxx
xx
xxxxx
xx
xx
xx

xx
xx
xx
xx
xx
xxxxxxxxxx

'''
'''
string_count=[2, 2, 2, 2, 2, 10]

for count in string_count:
    output=''
    for x_count in range(count):
        output += 'X'
    print(output)
'''

# LISTS

'''names = ['Soumyajit', 'Haneen', 'Sofia', 'Ananya', 'Akansha', 'Palwasha', 'Kalyani']

#add = ''
#add = input("Enter Name: ")
#names.append(add)

print(names[2:])

names[3]='XYZ'

print(names[:])
#print(names[1])
'''
'''
#FIND LARGEST NUMBER IN LIST

list= [3, 5, 999, 77, 1001, 2, 100]

print(list)
#largest=0

largest= list[0]
for item in list:
    print(item)
    if largest < item:
        largest = item
print(f'Largest Item is {largest}')

'''

# 2 DIMENSIONAL LIST .. MATRIX
'''
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix)

#print(matrix[1][1])

#matrix[1][1]= 20

print(" ")

for row in matrix:
    print(row)
    for item in row:
        print(f' Matrix Item in {item}')
'''

# LIST METHODS

# list = [9,2,3,4,4,4,5,6,7,8,9, 1]
# print(f'List 1 is - {list}')

# print(list.index(7))
# list.append(75)
# list.insert(5, 99)
# print(list.count(8))
# list.remove(2)
# print(list)
# list.clear()
# list.pop()
# list.pop()
# list.pop()

# print(list.index(6))

# if 7 in list:
#    print("Exists")
# else:
#    print("Does not exist")

# char= 'Hello'
# print("z" in char)

# print(list.count(4))

# print(list.sort())

# list.sort()
# print(list)
# list.reverse()

# print(list)

# print(list)

# list2= list.copy()
# print(f'List 2 is-- {list2}')


# REMOVE DUPLICATES IN A LIST


# list = [2,2,4,6,3,4,6,1,1,1,1,1,1,1,1,1,1,9,8]

# print(list)

# for item in list:
#    while list.count(item)>1:
#        list.remove(item)

# unique = []
# for item in list:
#    if item not in unique:
#        unique.append(item)

# print(unique)


# --------------------------------------------------------------


# TUPLES
# TUPLES are similar to list .. but TUPLES are immutable i.e unchangeable
'''
list = (1,2,3,4,5,6)
print(list)
print(list.count(3))
print(list.index(5))
print(list[5])
print(list)
'''

# ------------------------------------------------

# UNPACKING

'''
list = (1,2,3)

print(list)

x = list[0]
y = list[1]
z = list[2]

print(x*y*z)


#unpacking

p, q, r = list

print(p,q,r)
'''
'''
# ---------------------------------------------

# DICTIONARIES --- to store Key-Value pairs

dictionary = { "name": "XYZ", "age":21, "mail":"xyz@gmail.com", "virgin": False}


print(dictionary)
print(dictionary.values())
print(dictionary.keys())
print(dictionary.items())


print("")
print("")

print(dictionary["virgin"])
print(dictionary["age"])
print(dictionary["name"])


print("")
print("")

print(dictionary.get("name"))
print(dictionary.get("age"))
print(dictionary.get("mail"))


print(" ") #Line Break
print(dictionary.get("birthdate", "January 1st 1918"))
print("")

print(dictionary)
print("")
dictionary["birthdate"] = "May 8 1990" # Add New Key-Value
print(dictionary)

'''

# Enter Phone Number ... Translate To Individual Number Words
'''
numbers = input("Phone No.- ")  # input() returns a string .. so the entered "number" is technically a string

word_number_mapping = {"1": "one", "2": "two", "3": "three", "4": "four",
                       "5":"five", "6": "six", "7": "seven",
                       "8": "eights", "9": "nine", "0": "zero"
                       }

for digit in numbers:
   print(" ")
   print(" " + word_number_mapping.get(digit, "X"))
'''
'''
#  EMOJI CONVERTER

# Map character based emojis .. into proper smiley-face emojis

message= input(" >  ")
#print(message.split(' '))

split_message = message.split(" ")

#print(split_message)
print("")

emoji_map = {
    ":)": "smiley_face",
    ":(": "saddy_face"
}

output = ''

for ch in split_message:
    output += emoji_map.get(ch, ch) + " "

print(output)

'''


# FUNCTIONS IN PYTHON

# FUNCTIONS are like container with a few lines of code, which perform a certain task/purpose
'''
# Define the function--
# define the parameters of this function to be supplied by arguments when user calls the function
def function_name(first_name, second_name, num):
    # here name, num are the parameters .. user would need to pass arguments for these parameters
    num += 5
    print(f"Hello there {first_name}{second_name} {num}")
    print("Function in python")
    print("Good Experience")


print("Fire up the function- ")
function_name("Soumyajit", "Roy", 10)  # Call the function & pass the positional arguments
print("End function")

print("Again....")

function_name("Sahana", "Bhatt", 20)  # call the function again & pass the positional arguments

# KeyWord Argument

print(" KeyWord Argument:-  ")

# function_name(first_name="Sofia ", second_name="Khan ", num=30)

function_name(num=30, second_name="Khan ", first_name="Sofia ")

# always prefer positional arguments... but if necessary supply keyword arguments for better readability
# always pass positional arguments first.. and then the keyword argument
# so better never to mix-match positional & keyword argument

'''

'''
# Return a value from a function

def square_number(number):

    # By default .. all funcions in Python return ** None **

    return number * number


print(" Call the function, pass the argument(number value):- ")

num = input("Enter Number to be squared:- ")
num = int(num)

print(f" Square of {num} is:- {square_number(num)}")

'''



# AS A GENERAL RULE OF THUMB .. the *Function* should not worry about receiving input or printing output
# That is left upto the users .. *Function* should only contain the logic/business-logic

# One **Function** should only perform 1 task

'''
def emoji_converter(message):


    emoji_map = { ":)": "smiley_face", ":(": "saddy_face"}
    split_message= message.split(" ")
    output = " "
    for ch in split_message:
        output += emoji_map.get(ch, ch) + " "

    return output


argument = input("Enter message to Emoji Converter :- ")

print(emoji_converter(argument))  # call function, pass the argument, print the return value

'''
'''

# EXCEPTIONS -- to anticipate certain situations were the program crashes & does not exits properly
# Exit Code 0 --- successful exit ... anything but exit code 0 -- unsuccessful exit

# anticipate the various types of errors which can be encountered & handle exceptions & exit gracefully

# try-except

try:
    salary = int(input("Enter Salary:- "))
    #print(salary + 10)
    age = int(input("Enter Age:- "))

    risk = salary/age
    print(risk)

except TypeError:
    print("Enter String Value")

except ValueError:
    print("Enter Whole Number")

except ZeroDivisionError:
    print("Age can not be Zero")

'''

'''
# CLASSES -- we use classes to define NEW TYPES
# Numbers, Strings, Booleans.... these are simple types of classes
# Lists, Dictionaries ... also classes

# Classes are used to define a new type .. to model some real concept
# Classes can have METHODS .. these are operations which we can perform

# Pascal Naming Convention .. Capitalize first letter of word of the class


class Point:

    # Define the various methods/functions of the class
    def draw(self):
        print(" Draw ")

    def distance(self):
        print(" Distance ")


# Now that the CLASS has been defined... we can create OBJECTS ...  i.e Instances of the Class
# CLASS simply defines the blueprint/template for creating OBJECTS
# OBJECTS are the actual instances based on that blueprint/template ..  so can have 100s of instances

# Define a new object of that class  ... objects are the actual instances based on that blueprint/template defined in the class

obj1 = Point()  # creates a new object & then returns it to be stored in the variable

obj1.draw()
obj1.distance()

#  MAGIC METHODS are with double underscores

obj1.x = 10  # set attributes of the object
obj1.y = 20
obj1.z = "ATTRIBUTES OF THE 1st OBJECT"

print(obj1.x)
print(obj1.y)
print(obj1.z)

obj2 = Point()  # create a 2nd object/instance of the Point class

obj2.draw()
obj2.distance()

obj2.a = 50
obj2.b = 60
obj2.c = "ATTRIBUTES OF THE 2nd OBJECT"

try:

    print(obj2.a)
    print(obj2.b)
    print(obj2.c)

except AttributeError:
    print("Object Attribute Not Constructed")

'''

'''
# CONSTRUCTORS -- DESTRUCTORS
# A CONSTRUCTOR .. is a function that gets called.. at the time of creation of an object
# A CONSTRUCTOR .. allows us to initialize the attributes of an object(we can alter them later on)

class Point:
    # __init__ is a CONSTRUCTOR .. which is a method/function that gets called whenever we create a new object
    def __init__(self, x, y):
        self.x = x  # initialize the object attribute x with the value passed
        self.y = y  # initialize the object attribute y with the value passed

    def draw(self, p):
        print("Draw Method")
        print(p)

    def distance(self, q):
        print("Distance Method")
        print(q)


point1 = Point(10, 20)

print(point1.x)
print(point1.y)

point1.draw(30)
point1.distance(40)


point1.x = 11  # Can Change the object attribute which was earlier intialized
point1.y = 12
print(point1.x)
print(point1.y)

'''
'''
class Person:

    def __init__(self, name):  # CONSTRUCTOR METHOD
        self.name = name   # INITIALIZE THE ATTRIBUTE 'name'

    def talk(self):
        print(f" {self.name} Is Talking!")


entered_name = input(" Enter Your Name :- ")

person1 = Person(entered_name)

print(f" Hello {person1.name}! ")

person1.talk()


person2 = Person("Bob")  # CREATE a New OBJECT i.e INSTANCE of the class

print(f' Hello {person2.name}!')
person2.talk()

'''
'''

#  INHERITANCE
#  DRY --- DON'T REPEAT YOURSELF
#  REUSE CODE as much as possible
# Don't define something twice

class Mammal:
    def walk(self):
        print("Walking!")


class Dog(Mammal):
    pass  # to pass this line .. just added something to not let Dog class remain empty
    def bark(self):
        print("Dog Barks!")

class Cat(Mammal):
    def purr(self):
        print("Cat Purrs!")

dog1 = Dog()
cat1 = Cat()

dog1.walk()
cat1.walk()

dog1.bark()
cat1.purr()

'''

'''
#  MODULES

import module1   #  IMPORT THE MODULE HERE .. ideall should be at the top of the file

from module1 import pound_to_kg

from module1 import kg_to_pound

#print(f" Weight in Pound is- {module1.kg_to_pound(75)}")

#print(f" Weight in KG is- {module1.pound_to_kg(180)}")

print(pound_to_kg(150))
print(kg_to_pound(93))

'''
'''

#  MODULES helps us organize our project & arrange our code


import utility
import module1

file_list = [10, 5, 9, 21, 59, 104]

print(utility.find_max(file_list))  # use module **utility**

print(module1.kg_to_pound(70))  # use module **module1**
'''


#   PACKAGES -- another way to ORGANIZE the code/project
#   PACKAGES used to organize all the files/modules
#   PACKAGES are like a *directory/folder*
#   PACKAGE contains a particular type of module/s

import shipping.costing

import transporting.transportaion_cost







































