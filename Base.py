#1 Lesson Data types
#class str#class str#class str#class str#class str
name1 = "Arby" #Variable
name2 = "Adam"  #Variable
name3 = 'Said'  #Variable
print(type(name1)) #class str
print("How r u " +name1+ " and " +name2 +"?")

#<class 'int'>#<class 'int'>#<class 'int'>
my_age = 28
my_age += 1
my_age -=4
print(my_age) #<class 'int'>
print(type(my_age))
#print("Your age is "+my_age) #wrong
print("Your age is probably "+ str(my_age))

#<class 'float'>#<class 'float'>#<class 'float'>
my_height = 188.5
print(my_height)
print(type(my_height)) #<class 'float'>
#print("MY Height is how many cm do u know? "+my_height) #wrong
print("MY Height is how many cm do u know? "+str(my_height)+ " cm") #wrong

#<class 'bool'>#<class 'bool'>#<class 'bool'>#<class 'bool'>#<class 'bool'>
human=True
print(human)
print(type(human)) #<class 'bool'>
#print(" Are you human? Yes I am "+human) wrong
print(" Are you human? Yes it is "+str(human))

#Lesson2 Multiple assignment

name = "Arby"
age = 28
attractive = True
print(name)
print(age)
print(attractive)

name, age, handsome = "Arby", 28, True
print(name)
print(age)
print(handsome)

spongebob = patrick = sandy = squidward = 30
print(spongebob,patrick)
print(sandy, squidward)

#Lesson 3 STRING METhods
name = "Arby"
print(len(name)) #Show quantity of SYMBOLS
name = "arby"
#print(name.find("y"))

name = "Arby said"
#print(name.capitalize()) # First letter is Capitilised
#print(name.upper()) # LETTERS is UPPER
#print(name.lower()) letters are low
#print(name.isdigit()) Checking boolean if are any symbols instead of numbers, if number True if not False
#print(name.isalpha()) Boolean , are all alphabetical letters
#print(name.count("a")) #check how many letters
#print(name.replace("A", "a")) #REplace letter
#print(name*2) Multiple


#Lesson4 type casting
#type casting = convert the data type of a value to another data type.
x = 5
y = 2.0
z = "3"

x = str(x)
z = float(z)
y = int(y)

print("IT IS "+x)
print(x)
print(z)
print(y)

# Lesson 5 User input
name = input("What is your name?: ")
#name2 = input("Who are u?: ")
#print("I am "+name2)

old = int(input("How old are u?: "))
old += 2
height = float(input("What is your height?: "))
print("Hi "+name) # in name will be only what he inputs
print("No your age is: "+str(old))
print("You are "+str(height)+" cm tall")


# Lesson 6 math functions

import math  #for import of module

pi = 3.14
x = 1
y = 2
z = 3

#print(round(pi)) #making round to nearest integer
#print(math.ceil(pi)) #up round
#print(math.floor(pi)) #down round
#print(abs(pi)) # absolute value of number of closest to zero
#print(pow(pi,2)) #power (stepen)
#print(math.sqrt(pi)) #sq square root квадратный корень
#print(max(x,y,z)) # find maximum
#print(min(x,y,z)) # or minimum

# Lesson 7 string slicing =create a substring by EXTRACTING elements from another string
#             indexing[]   or slice()
#              [start:stop:step]

name = "Said Arby Ibrakhimi"
#first_name = name[0]
#print(first_name) # Such case will print only first letter "S"
#first_name = name[0:3] #First letter inclusive but last letter exclusive = "Sai" result
#first_name = name[0:4] or [:4] # right
first_name = name[:4]
last_name = name[5:9] # also [5:] slice until the end
latest_name = name[::3] #3 step 333
reversed_name = name[::-1] #reversing
#print(len(name))
print(reversed_name)

#website1 = "http://yandex.ru"
website = "http://youtube.com"
slice_youtube = slice(7,-4) #SLICE function

#slice_ya1 = slice(7,-3)
#print(website[slice_ya])
print(website[slice_youtube])

#Lesson 8 # if statement
#                       = a block of code that will execute if it's condition is true

my_age = int(input("How old r u?: "))
if my_age == 99:
    print("It soon will be century")
elif my_age >=18:
    print("You are an adult")
elif my_age<0:
    print("U have not born yet")
else:
    print("You are a child")
number = int(input("Choose number (1,2,3): "))
if number == 1:
    print("yo have chosen 1")
elif number == 2:
    print("YOu have chosen 2")
else:
    quit()

#Lesson 9
# logical operators (and,or,not) = used to check if two or more conditional statements is true

temp = int(input("What is temp outside?:"))

#if temp >= 0 and temp <= 30: #both must be true!!!
if not(temp >= 0 and temp <= 30):  # both must be true!!!
    print("Its better to stay at home")
elif not(temp <0 or temp >30):
    print("The temp is good today")
temp = int(input("What is the temperature outside?: "))

if temp >= 0 and temp <= 30:
    print("the temperature is good today!")
    print("go outside!")
elif temp < 0 or temp > 30:
    print("the temperature is bad today!")
    print("stay inside!")
string_1 = ''
if not string_1:
    print('String is empty.')
else:
    print(string_1)

a = tuple()
if not a:
    print('Tuple is empty.')
else:
    print(a)

#Lesson 10 # while loop =  a statement that will execute it's block of code,
#                        as long as it's condition remains true

#while not 1==1:
#    print("Help ME")

#name = ""
#while len(name) == 0:
#    name = input("write your name: ")
#print("Hi "+name)

name = None
while not name:
    name = input("write your name: ")
print("Hi "+name)

name = ""
while not len(name) > 0:
    name = input("write your name: ")
print("Hi "+name)

#Minutomer
import time

min = 0
while True:
    print(min)
    time.sleep(60)
    min += 1
#Secundomer
import time
sec = 0
while True:
    print(sec)
    time.sleep(1)
    sec += 1


#Lesson 11 # for loop =    a statement that will execute it's block of code
#                      a limited amount of times
#
#                     while loop = unlimited
#                     for loop = limited

#for i in range(10):   #i = index
#    print(i+1)

#for i in range(50,101):
#    print(i)

#for i in range(3,34,3):   #STEP 3rd
 #   print(i)

import time #time module

for secs in range(10,0,-1):
    print(secs)
    time.sleep(1)  #seconds
print("HAPPY NEW YAER")

for i in "ARBI SAID":
    print(i)

#Lesson 12
#python #nested #loops

# nested loops =    The "inner loop" will finish all of it's iterations before
#                   finishing one iteration of the "outer loop"

rows = int(input("How many rows?: "))
columns = int(input(("How many columns:? ")))
symbol = input("Enter your symbol: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end=" ")
    print()


#Lesson 13
# Loop Control Statements = change a loops execution from its normal sequence

# break =       used to terminate the loop entirely
# continue =    skips to the next iteration of the loop.
# pass =        does nothing, acts as a placeholder

#while True:
#    name = input("Enter your name: ")
#    if name == "":
#        break

#phone_number = "123-456-789"

#for i in phone_number:
#    if i == "-":
#        continue
#    print(i, end="")

sum = 15

for i in range(sum):
    if i == 13:
        pass
    else:
        print(i)

for i in range(5,25,5):
    if i == 15:
        pass
    print(i, end=",")

#Lesson 14 # list = used to store multiple items in a single variable

food = ["pizza", "kotam", "moskal"]
#food[2] = "shaurma"
#print(food)
#food.append("ice cream") Add 1 more in the END
#food.remove(food[1]) Delete item in list or
#food.remove("kotam")  Delete item in list or
#food.pop() #Delete last item in list or
#food.insert(0, "borghal")
#food.insert(2, "dulh")
#food.sort() alphabetical sort
#food.clear
for i in food:
    print(i)

#Lesson 15 # Python 2D lists two dimensional list

# 2D lists = a list of lists
drinks = ["chai", "hiy", "coffee"]
dinner = ["kotam", "moskal", "ustagh"]
dessert = ["pirojnoe", "tort"]

food = [drinks, dinner, dessert]
#print(food[0][1])
print(food)
n = [1,2,3,4]
n[0] = 15
print(n)


#Lesson 16 ## tuple =   collection which is ordered and unchangeable
#                used to group together related data

student = ("Arbi", 21,"male")
#print(student.count("Arbi"))
#print(student.index("male"))

#for i in student:
#    print(i, end=" ")

if "males" in student:
    print("HE HEY")
elif "arbi" in student:
    print("NOT he is not")
else:
    print("come on")



#Lesson 17 # set = collection which is unordered, unindexed. No duplicate values

utensils = {"fork", "spoon","knife"}   # Set is faster
dishes = {"bowl","plate","cup","knife"}
#Methods
#utensils.add("napkin")
#utensils.remove("fork")
#utensils.clear
#utensils.update(dishes)
#dinner_table = utensils.union(dishes)
#sss = dishes.difference(utensils)
#print(utensils.difference(dishes))
sss = utensils.intersection(dishes)
print(sss)

#for x in dinner_table:
#    print(x, end=" ")


#Lesson 18 # dictionary =  A changeable, unordered collection of unique key:value pairs
#                        Fast because they use hashing, allow us to access a value quickly

stolicyi = {'USA':'Washinghton',
            'India':'New Delhi',
            'China':'Beijing',
            'Russia':'Moscow'}
stolicyi.update({'Germany':'Berlin'})
stolicyi.pop('China') #delete
#stolicyi.clear()
#print(stolicyi['Russia'])
#print(stolicyi.get('Germany')) # GET to check is there is key SAFER WITHOUT ERROR
#print(stolicyi.keys())
#print(stolicyi.values())
#stolicyi.update({'USA':'LAS VEGAS'})
#print(stolicyi.items())
print(stolicyi)

#for key,value in stolicyi.items():
 #   print(key,value)


#Lesson 19 # index operator [] = gives access to a sequence’s element (str,list,tuples)

name = "arbi Said"
#if(name[0].islower()):
#    name = name.capitalize()

first_name = name[:5].upper()
last_name = name[5:].upper()
last_character = name[-1]

#print(first_name, last_name)
print(last_character)

#Lesson 20 # function = a block of code which is executed only when it is called.


def hello(name,second_name,age):
    print("Hello Arbi ",name,second_name,age)
    print("you are",age,"old")
    print("Have a nice day")

#hello("Bro")
#hello("DUde")
#name = "BRO"
#m_name = "BRO"
hello("said", "Ibrakhimi", 28)


#Lesson 21 # return statement = Functions send Python values/objects back to the caller.
#                    These values/objects are known as the function’s return value

def multiply(number1,number2):
    return number1 * number2

x = (multiply(6,8))
#print(multiply(6,8))
print(x)

#Lesson 22 # keyword arguments =   arguments preceded by an identifier when we pass them to a function
#                       The order of the arguments doesn't matter, unlike positional arguments
#                       Python knows the names of the arguments that a function receives

def hello(f_name,s_name,l_name):
    print("Hello",f_name,s_name,l_name)
hello(l_name="Ibra",f_name="Said",s_name="Arbi")

#Lesson 23 # nested functions calls =  function calls inside other function calls
#                           innermost function calls are resolved first
#                           returned value is used as argument for the next outer function

#num = input("Enter a whole positive number: ")
#num = float(num)
#num = abs(num)
#num = round(num)
#print(num)

print(round(abs(float(input("Enter positive number: ")))))

#Lesson 24 # scope = The region that a variable is recognized
#         A variable is only available from inside the region it is created.
#         A global and locally scoped version of a variable can be created
name = "arbi"  #global scope
def display_name():
    name = "Said" # local scope (available only inside this function)
    print(name)
display_name()
print(name)


#Lesson 25 # *args =   parameter that will pack all arguments into a tuple
#                useful so that a function can accept a varying amount of arguments


"""def add (sum1, sum2):
    res = sum1 + sum2
    return res
print(add(2,2))"""

def add (*args):
    res = 0
    for i in args:
        res += i
    return res
print(add(3,2))


def multipl(*chisla):
    sum = 2
    for i in chisla:
        sum *= i
    return sum
print(multipl(3,5,2,))


#Lesson 26 # **kwargs =   parameter that will pack all arguments into a dictionary
#                       useful so that a function can accept a varying amount of keyword arguments

#def hell(fst,last):
#    print("hello ",fst,last)
#hell(fst="said",middle="ibrakhimi" last="arbi")

def hello(**kwargs):
    #print("hello ",kwargs["fst"],kwargs['last'])
    print("Hello", end=" ")
    for key,value in kwargs.items():
        print(value, end=" ")
hello(fst="said",middle="ibrakhimi",last="arbi")

##Lesson 27 Python string format method tutorial explained
# str.format() =    optional method that gives users
#                   more control when displaying output

animal = "cow"
item = "moon"
#print("the animal "+animal+" jumped over the "+item)
#print("the {} jumped over the {}".format("cow","moon"))
#print("the {} jumped over the {}".format(animal,item))
#print("the {0} jumped over the {1}".format(animal,item)) #positinal argum
#print(("the {animal} jumped over the {item}".format(animal="cow",item="moon"))) #keyword arguments

text = "The {0} jumpedover the {0}"
print(text.format(animal,item))

name = "Arbi"
print("hello my name is {}".format(name))
print("hello my name is {:10}. nice".format(name))
print("hello my name is {:<10}. nice".format(name))
print("hello my name is {:>10}. nice".format(name))
print("hello my name is {:^10}. nice".format(name))

#number = 3.14159
#print("the number pi is {:.2f}".format(number))

number = 1000
print("the number is {:,}".format(number))
print("the number is {:b}".format(number))
print("the number is {:o}".format(number))
print("the number is {:X}".format(number))
print("the number is {:E}".format(number))


##Lesson 28 Python random numbers module tutorial explained
import random #module random
x = random.randint(1,6) #integer
y = random.random() #from 0 to 1
myList = ['rock', 'paper','scissors']
z = random.choice(myList)

cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
random.shuffle(cards)
print(cards)

##Lesson 29 # exception =   events detected during execution that interrupt the flow of a program

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print("Dont diveide by zero")
except ValueError:
    print("onle number")
else:
    print(int(result))
finally:
    pass

##Lesson 30 Python file detection handling tutorial example explained

import os

path = "C:\\Users\\1\\Desktop\\test.txt.txt"

if os.path.exists(path):
    print("That location exists")
    if os.path.isfile(path):
        print("this is file")
    elif os.path.isdir(path):
        pass

else:
    print("that loc doesnt exists")

    ##Lesson 31 Python reading files tutorial example explained

    # with open('test.txt.txt') as file:
    #    print(file.read())
    try:
        with open('test.txt.tx') as file:  # if there is mistake
            print(file.read())
    except FileNotFoundError:
        print("that file was not found")

    # print(file.closed)

##Lesson 32 Python writing files tutorial example explained

text = 'Have\nThis is same\nCameon'

with open('test.txt.txt',"a") as file:
    file.write(text)

##Lesson 33 Python copy a file tutorial example explained
# copyfile() =  copies contents of a file
# copy() =      copyfile() + permission mode + destination can be a directory
# copy2() =     copy() + copies metadata (file’s creation and modification times)

import shutil
shutil.copyfile("test.txt.txt","copy.txt") #or C:\Users\1\Desktop\\copy.txt

##Lesson 34 Move replace file tutorial example explained

import os

source = "test.txt.txt"
destination = "C:\\Users\\1\\Desktop\\test.txt"

try:
    if os.path.exists(destination):
        print("there is")
    else:
        os.replace(source,destination)
        print(source+" was moved")
except FileNotFoundError:
    print("Was not found")


##Lesson 35 delete file tutorial example explained
import os
import shutil
path = "empty"
#os.remove(path)
#os.replace("copy.txt")
try:
    #os.remove(path)
    #os.rmdir(path)
    shutil.rmtree(path)
except FileNotFoundError:
    print("file was not found")
except PermissionError:
    print("u dont have permissin deletr")
except OSError:
    print("u cant delete")
else:
    print("was deleted")

##Lesson 36 Modules
#from messages import hello,bye
#hello()
#bye()
#import messages as  m
#m.hello()
#m.bye()

help("modules")

##Lesson 37 Rockk Paper
import random
player_score = 0
comp_score = 0

while True:


    choices = ['rock', 'paper', 'scissors']

    computer = random.choice(choices)

    player_choice = None
    while player_choice not in choices:
        player_choice = input("rock, paper or sciccors:? ").lower()
    if player_choice == computer:
        print("computer choice is "+computer)
        print("your choice is "+player_choice)
        print("Tie!")
    elif player_choice == "rock":
        if computer == "paper":
            print("computer choice is " + computer)
            print("your choice is " + player_choice)
            print("U lost!")
            comp_score += 1
        if computer == "scissors":
            print("computer choice is " + computer)
            print("your choice is " + player_choice)
            print("u win!")
            player_score += 1
    elif player_choice == "scissors":
        if computer == "paper":
            print("computer choice is " + computer)
            print("your choice is " + player_choice)
            print("U win!")
            player_score += 1
        if computer == "rock":
            print("computer choice is " + computer)
            print("your choice is " + player_choice)
            print("u lost!")
            comp_score += 1
    elif player_choice == "paper":
        if computer == "rock":
            print("computer choice is " + computer)
            print("your choice is " + player_choice)
            print("U win!")
            player_score += 1
        if computer == "scissors":
            print("computer choice is " + computer)
            print("your choice is " + player_choice)
            print("u lost!")
            comp_score += 1

    answer = input("play again?(yes,no): ").lower()
    if answer != "yes":
        break
print("Ur score: " + str(player_score))
print("comp score " + str(comp_score))
print("Good bye")

######################FRom Tim Tech
import random
user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]


while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue
    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("Computer picked", computer_pick)
    # rock: 0, paper:1, scissors:2
    if user_input == "rock" and computer_pick == "scissors":
        print("You win")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You win")
        user_wins += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("You win")
        user_wins += 1
    else:
        print("You lost")
        computer_wins += 1
print("You won", + user_wins, "times")
print("Comp wom", computer_wins, "times")
print("Goodbye")


######### Kylie Ying

import random
import math

def play():
    user = input("Choose: 'rock' for rock, 'p' for paper, 's' for scissors\n")
    user = user.lower()

    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return (0, user, computer)

    if is_win(user, computer):
        return (1, user, computer)

    return (-1, user, computer)

def is_win(user, computer):
    if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        return True
    return False
def play_best_of(n):
    player_wins = 0
    computer_wins = 0
    wins_necessary = math.ceil(n/2)
    while player_wins < wins_necessary and computer_wins < wins_necessary:
        result, user, computer = play()
        if result == 0:
           print("its tie You and computer have chosen {}. \n".format(user))
        elif result == 1:
            player_wins += 1
            print("You won. You chose {} and computer chose {}.\n".format(user, computer))
        else:
            computer_wins += 1
            print("you chose {} and comp chose {} and you lost.\n".format(user, computer))
        print("\n")
    if player_wins > computer_wins:
        print("You won the best {} games".format(n))
    else:
        print("Sorry computer won best of {} games".format(n))


if __name__ == '__main__':
    play_best_of(3)

#Lesson 38 Python quiz game
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1
    for key in questions:
        print("--------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C or D): ").upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1
    display_score(correct_guesses, guesses)

def check_answer(answer, guess):
    if answer == guess:
        print("Correct")
        return 1
    else:
        print("wrong")
        return 0

def display_score(correct_guesses, guesses):
    print("-----------------------------")
    print("Results")
    print("-----------------------------")
    print("Answers:", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses:", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)

    print("Your score is: "+str(score)+"%")
def play_again():
    response = input("Play again?")
    response = response.upper()
    if response == "YES":
        return True
    else:
        return False

questions = {
 "Who created Python?: ": "A",
 "What year was Python created?: ": "B",
 "Python is tributed to which comedy group?: ": "C",
 "Is the Earth round?: ": "A"
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
          ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
          ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
          ["A. True","B. False", "C. sometimes", "D. What's Earth?"]]

new_game()

while play_again():
    new_game()
print("Bye")


#lesson 39 python object oriented programming OOP tutorial example explained

from car import Car

car_1 = Car("chevy", "Corvet", 2021, "blue")
car_2 = Car("Ford", "Mustang", 2022, "red")
print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)

car_2.drive()
car_2.stop()

#lesson 40 Python class variables vs instance variables tutorial example explained

from car import Car

car_1 = Car("chevy", "Corvet", 2021, "blue")
car_2 = Car("Ford", "Mustang", 2022, "red")

Car.wheels = 2

#car_1.wheels = 2
print(car_1.wheels)
print(car_2.wheels)
#print(Car.wheels)

#lesson 41 Python inheritance tutorial example explained

class Animal:

    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")





class Rabbit(Animal):
    def run(self):
        print("this rabbit is swimming")

class Fish(Animal):
    def swim(self):
        print("This FiSH is swimming")

class Hawk(Animal):
    def fly(self):
        print("This hawk is flying")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

rabbit.run()
fish.swim()
hawk.fly()
#print(rabbit.alive)
#fish.eat()
#hawk.sleep()

#lesson 42 # multi-level inheritance = when a derived (child) class inherits another derived (child) class

class Organism:
    alive = True

class Animal(Organism):

    def eat(self):
        print("This animal is eating")
class Dog(Animal):

    def bark(self):
        print("This dog is barking")


dog = Dog()
print(dog.alive)
dog.eat()
dog.bark()

#lesson 43 # multiple inheritance = when a child class is derived from more than one parent class

class Prey:
    def flee(self):
        print("This animal flees")

class Predator:
    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish (Prey, Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()

#lesson 44 Method Overriding
class Animal:

    # overriden method
    def eat(self):
        print("This animal is eating")


class Rabbit(Animal):

    # overriding method
    def eat(self):
        print("This rabbit is eating a carrot")


rabbit = Rabbit()
rabbit.eat()

#Lesson 45 method chaining

# method chaining = calling multiple methods sequentially
#                   each call performs an action on the same object and returns self

class Car:
    def turn_on(self):
        print("U started engine")
        return self
    def drive(self):
        print("You drive the car")
        return self

    def brake(self):
        print("You step on the brakes")
        return self

    def turn_off(self):
        print("You turn off the engine")
        return self
car = Car()
#car.turn_on()
#car.drive()
#car.turn_on().drive()

car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()

#Lesson 46 # super() = Function used to give access to the methods of a parent class.
#                  Returns a temporary object of a parent class when used

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):

    def __init__(self, length, width):
        super().__init__(length, width)

    def area(self):
        return self.length*self.width

class Cube(Rectangle):

    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.length*self.width*self.height

square = Square(3,3)
cube = Cube(3,3,3)
print(square.area())
print(cube.volume())


#Lesson 47  Python abstract class example tutorial explained
# Prevents a user from creating an object of that class
# + compels a user to override abstract methods in a child class

# abstract class = a class which contains one or more abstract methods.
# abstract method = a method that has a declaration but does not have an implementation.
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def go(self):
        print("You drive the car")
    def stop(self):
        print("This car is stopped")

class Motorcycle(Vehicle):
    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("This motorcycle is stopped")

#vehicle = Vehicle()
car = Car()
motorcycle =Motorcycle()

#vehicle.go()
car.go()
motorcycle.go()
car.stop()
motorcycle.stop()

#Lesson 48 Python pass objects as arguments tutorial example explained

class Car:
    color = None
class Motorcycle:
    color = None
def change_color(vehicle, color):

    vehicle.color = color
car1 = Car()
car2 = Car()
car3 = Car()

bike1 = Motorcycle()
change_color(car1, "red")
change_color(car2, "white")
change_color(car3, "blue")
change_color(bike1, "green")

print(car1.color)
print(car2.color)
print(car3.color)
print(bike1.color)


#Lesson 49 # duck typing = concept where the class of an object is less important than the methods/attributes
#               class type is not checked if minimum methods/attributes are present
#               “If it walks like a duck, and it quacks like a duck, then it must be a duck.”

class Duck:

    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("This duck is qwuacking")

class Chicken:

    def walk(self):
        print("This chicken is walking")

    def talk(self):
        print("This chicken is clucking")
class Person:
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("U caught the critter!")
duck = Duck()
chicken = Chicken()
person = Person()

#person.catch(duck)
person.catch(chicken)

#Lesson 50 Python walrus operator assignment expression tutorial example explained
# walrus operator :=
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression

#happy = True
#print(happy)

#print(happy := True)

#foods = list()
#while True:
#    food = input("WHAT FOOD DO YOU LIKE?: ")
#    if food == "quit":
#        break
#    foods.append(food)

foods = list()
while food := input("WHAT FOOD DO YOU LIKE?:") != "quit":
    foods.append(food)

#Lesson 51 Python assign a function to a variable

def hello():
    print("Hello")

#print(hello)
hi = hello
hi()

say = print
say("I cant believe")

#Lesson 52 #  Higher Order Function =  a function that either:
#                           1. accepts a function as an argument
#                               or
#                           2. returns a function
#                           (In python, functions are also treated as objects)

def loud(text):
    return text.upper()
def quiet(text):
    return text.lower()
def hello(func):
    text = func("Hello")
    print(text)
hello(loud)
hello(quiet)

def divisor(x):
    def dividend(y):
        return y / x
    return dividend

divide = divisor(2)
print(divide(10))

#Lesson 54

# lambda function = function written in 1 line using lambda keyword
#                   accepts any number of arguments, but only has one expression.
#                   (think of it as a shortcut)
#                   (useful if needed for a short period of time, throw-away)
#
# lambda parameters:expression

def double(x):
    return x * 2

print(double(5))

tripple = lambda y:y * 2
print(tripple(7))

multuply = lambda z, r: z * r
print(multuply(3,2))

add = lambda t,u,i: t + u +i
print(add(1,2,3))


fullname = lambda first_name, lastname: first_name+" "+lastname
print(fullname("bro","arby"))

age = lambda age: True if age >= 18 else False
print(age(19))


#Lesson 54 # sort() method   = used with lists
# sort() function = used with iterables
students = [("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick","D", 36),
            ("Spongebob","B", 20),
            ("Mr.Krabs","C", 78)]
grade = lambda grades:grades[2]
students.sort(key=grade)
for i in students:
    print(i)

    students = (("Squidward", "F", 60),
                ("Sandy", "A", 33),
                ("Patrick", "D", 36),
                ("Spongebob", "B", 20),
                ("Mr.Krabs", "C", 78))
    grade = lambda grades: grades[2]
    sorted_students = sorted(students, key=grade)
    for i in sorted_students:
        print(i)

#students = ("Squi", "Sandy", "Patrick", "Sponge", "Mr. Krabs")
#students = ["Squi", "Sandy", "Patrick", "Sponge", "Mr. Krabs"]

#students.sort(reverse=True)
#sorted_students = sorted(students, reverse=True,)
#for i in sorted_students:
 #   print(i)

# Lesson 55 # map() =   applies a function to each item in an iterable (list, tuple, etc.)
#
# map(function,iterable)

store = [("shirt", 20.00),
         ("pants", 25.00),
         ("jacket", 50.00),
         ("socks", 10.00)]

# to_euro = lambda data: (data[0],data[1]*0.82)
to_dollars = lambda data: (data[0], round(data[1] / 0.82))
store_dollars = list(map(to_dollars, store))
# store_euros = map(to_euro, store)
# store_euros = list(map(to_euro, store))
# for i in store_euros:
#    print(i)
for i in store_dollars:
    print(i)


#Lesson 56 # filter() =    creates a collection of elements from an iterable,
#               for which a function returns true
#
#               filter(function, iterable)

friends = [("Rachel",19),
           ("Monica",18),
           ("Phoebe",17),
           ("Joey",16),
           ("Chandler",21),
           ("Ross",20)]
age = lambda data: data[1] >= 18
drinking_buddies = list(filter(age,friends))
for i in drinking_buddies:
    print(i)

#Lesson 57 # reduce() = apply a function to an iterable and reduce it to a single cumulative value.
#            performs function on first two elements and repeats process until 1 value remains
#
# reduce(function, iterable)

import functools
letters = ["H","E","L","L","O"]
word = functools.reduce(lambda x,y:x+y,letters)
print(word)

factorial = [5,4,3,2,1]
result = functools.reduce(lambda x,y:x*y,factorial)
print(result)

#Lesson 58  list comprehension =  a way to create a new list with less syntax
#                       can mimic certain lambda functions, easier to read
#                       list = [expression for item in iterable]
#                       list = [expression for item in iterable if conditional]
#                       list = [expression if/else for item in iterable]

squares = []                # create an empty list
for i in range(1,11):       # create a for loop
    squares.append(i * i)    # define what each loop iteration should do
print(squares)

squares = [i*i for i in range(1,11)]
print(squares)


students = [100,90,80,70,60,50,40,30,0]
#passed_students = list(filter(lambda x:x >= 60, students))
#passed_students = [i for i in students if i >= 60]
passed_students = [i if i >= 60 else "Failed" for i in students]
print(passed_students)

#Lesson 59 # dictionary comprehension = create dictionaries using an expression
#                            can replace for loops and certain lambda functions
#
# dictionary = {key: expression for (key,value) in iterable}
# dictionary = {key: expression for (key,value) in iterable if conditional}
# dictionary = {key: (if/else) for (key,value) in iterable}
# dictionary = {key: function(value) for (key,value) in iterable}

#cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
#cities_in_C = {key: round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}
#print(cities_in_C)

# dictionary = {key: expression for (key,value) in iterable if conditional}
#weather = {'New York': "snowing", 'Boston': "sunny", 'Los Angeles': "sunny", 'Chicago': "cloudy"}
#sunny_weather = {key: value for (key, value) in weather.items() if value == "sunny"}
#print(sunny_weather)

# dictionary = {key: (if/else) for (key,value) in iterable}

#cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
#desc_cities = {key: ("Warm" if value >=40 else "cold" ) for (key,value) in cities.items()}
#print(desc_cities)


# dictionary = {key: function(value) for (key,value) in iterable}
def check_temp(value):
    if value >= 70:
        return "Hot"
    elif 69 >= value >= 40:
        return "warm"
    else:
        return "cold"
cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
desc_cities = {key: check_temp(value) for (key, value) in cities.items()}
print(desc_cities)


#Lesson 60 # zip(*iterables) =  aggregate elements from two or more iterables (list, tuples, sets, etc.)
#                    creates a zip object with paired elements stored in tuples for each element
usernames = ["Dude", "Bro", "Mister"]
passwords = ("p@ssword", "abc123", "guest")
login_date = ["1/1/2021","1/2/2021""1/3/2021"]

users = zip(usernames,passwords,login_date)
for i in users:
    print(i)
#users = list(zip(usernames, passwords))
#users = dict(zip(usernames, passwords))
#for key,value in users.items():
#    print(key,value)

#Lesson 61 python if __name__ == '__main__' name == main tutorial example explained
# ***********************************
# if __name__ == '__main__'
# ***********************************

# y tho?
# 1. Module can be run as a standalone program
#    or
# 2. Module can be imported and used by other modules

#  Python interpreter sets "special variables", one of which is __name__
#  Python will assign the __name__ variable a value of '__main__' if it's
#  the initial module being run

def main():
    print("Hello!")


if __name__ == '__main__':
    main()

# ***********************************
#Lesson 62 import time
import time
# *************************************************************************
#print(time.ctime(0))    # convert a time expressed in seconds since epoch to a readable string
#                                        epoch = when your computer thinks time began (reference point)
#print(time.time())      # return current seconds since epoch
#print(time.ctime(time.time())) # will get current time
#print(time.ctime(time.time()))

#time_object = time.localtime()
#time_object2 = time.gmtime()
#print(time_object2)
#local_time = time.strftime("%B %d %Y %H:%B:%S", time_object)
#print(local_time)

#time_string = "20 April, 2020"
#time_object = time.strptime(time_string, "%d %B, %Y")
#print(time_object)
#time_tuple = (2020, 4, 20, 4 ,20, 0, 0, 0, 0)
#time_string = time.asctime(time_tuple)
#print(time_string)
time_tuple = (2020, 4, 20, 4 ,20, 0, 0, 0, 0)
time_string = time.mktime(time_tuple)
print(time_string)

#Lesson 63# Python threading tutorial
# ****************************************************
# thread =  a flow of execution. Like a separate order of instructions.
#                  However each thread takes a turn running to achieve concurrency
#                  GIL = (global interpreter lock),
#                  allows only one thread to hold the control of the Python interpreter at any one time

# cpu bound = program/task spends most of it's time waiting for internal events (CPU intensive)
#             use multiprocessing

# io bound = program/task spends most of it's time waiting for external events (user input, web scraping)
#            use multithreading

import threading
import time


def eat_breakfast():
    time.sleep(3)
    print("U eat breakfast")
def drink_coffee():
    time.sleep(4)
    print("U drink coffee")
def study():
    time.sleep(5)
    print("U studied")

x = threading.Thread(target=eat_breakfast, args=())
x.start()
y = threading.Thread(target=drink_coffee, args=())
y.start()
z = threading.Thread(target=study, args=())
z.start()

x.join()
y.join()
z.join()

#eat_breakfast()
#drink_coffee()
#study()
print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())





print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())

#Lesson 64  Python daemon threads
# **********************************************************

# daemon thread = a thread that runs in the background, not important for program to run
#                 your program will not wait for daemon threads to complete before exiting
#                 non-daemon threads cannot normally be killed, stay alive until task is complete
#
#                 ex. background tasks, garbage collection, waiting for input, long running processes
import time
import threading
def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for:", count, "seconds")


x = threading.Thread(target=timer, daemon=True)
x.start()
x.setDaemon(True)
answer = input("Do you wish to exit?")

#Lesson 65 Python multiprocessing
# *********************************
# multiprocessing = running tasks in parallel on different cpu cores, bypasses GIL used for threading
#                   multiprocessing = better for cpu bound tasks (heavy cpu usage)
#                   multithreading = better for io bound tasks (waiting around)

from multiprocessing import Process, cpu_count
import time


def counter(num):
    count = 0
    while count < num:
        count += 1


def main():

    print("cpu count:", cpu_count())

    a = Process(target=counter, args=(500000000,))
    b = Process(target=counter, args=(500000000,))

    a.start()
    b.start()

    print("processing...")

    a.join()
    b.join()

    print("Done!")
    print("finished in:", time.perf_counter(), "seconds")


if __name__ == '__main__':
    main()

# *********************************

#Lesson 66 Python tkinter GUI tutorial for beginners
from tkinter import *

window = Tk()
window.geometry("420x420")
window.title("FIRST GUI")
icon = PhotoImage(file='files/tomato_vegetables_vegetable_food_agriculture_fruit_icon_220780.png')
window.iconphoto(True, icon)
window.config(background="#f8fc44")


window.mainloop()

#Lesson 67 Python label labels tkinter GUI code example tutorial for beginners
# label = an area widget that holds text and/or an image within a window

from tkinter import *
wind = Tk()

photo = PhotoImage(file='files/tomato_vegetables_vegetable_food_agriculture_fruit_icon_220780.png')
label = Label(wind,
              text="Hello World",
              font=('Arial', 40, 'bold'),
              fg='#00FF00',
              bg='black',
              relief=RAISED,
              bd=15,
              padx=10,
              pady=30,
              image=photo,
              compound='bottom')
#label.place(x=0,y=0)
label.pack()

wind.mainloop()

#Lesson 68 Python tkinter button buttons GUI tutorial beginners code
# button = you click it, then it does stuff
from tkinter import *

count = 0

def click():
    global count
    count += 1
    print("You clicked the button")
    print(count)


window = Tk()
photo = PhotoImage(file='files/tomato_vegetables_vegetable_food_agriculture_fruit_icon_220780.png')
button = Button(window,
                text="Click",
                command=click,
                font=("Comic Sans", 30),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",
                state=ACTIVE,
                image=photo,
                compound="bottom")
button.pack()

window.mainloop()
# Lesson 69 entry box widget tkinter GUI code example tutorial beginners
# entry widget = textbox that accepts a single line of user input
from tkinter import *


def submit():
    username = entry.get()
    print("Hello", username)
    entry.config(state=DISABLED)


def delete():
    entry.delete(0, END)


def backspace():
    entry.delete(len(entry.get()) - 1, END)


window = Tk()

entry = Entry(window,
              font=("Arial", 30),
              fg="white",
              bg="blue")
# show="*")

entry.insert(0, "sponge:")
entry.pack(side=LEFT)

submit_button = Button(window,
                       text="Submit",
                       command=submit)

submit_button.pack(side=RIGHT)

delete_button = Button(window,
                       text="Delete",
                       command=delete)

delete_button.pack(side=RIGHT)
backspace_button = Button(window,
                          text="Backspace",
                          command=backspace)

backspace_button.pack(side=RIGHT)

window.mainloop()

# Lesson 70 checkbox checkbutton tkinter GUI tutorial for beginners
from tkinter import *


def display():
    if (x.get() == "YES"):
    #if (x.get() == True):
    #if(x.get()==1):
        print("U agree")
    else:
        print("U dont agree")


window = Tk()
#x = IntVar()
#x = BooleanVar()
x = StringVar()
photo = PhotoImage(file='files/tomato_vegetables_vegetable_food_agriculture_fruit_icon_220780.png')
check_button = Checkbutton(window,
                           text="I agree",
                           variable=x,
                           #onvalue=1,
                           #offvalue=0,
                           #onvalue=True,
                           #offvalue=False,
                           onvalue="YES",
                           offvalue="NO",
                           command=display,
                           font=("Arial", 30),
                           fg="red",
                           bg="blue",
                           activeforeground="white",
                           activebackground="blue",
                           pady=10,
                           padx=15,
                           image=photo,
                           compound=LEFT)

check_button.pack()
window.mainloop()
# Lesson 71 radio buttons
# radio button = similar to checkbox, but you can only select one from a group
from tkinter import *

food = ['pizza', 'hamb', 'hotdog']
def order():
    if(x.get()==0):
        print("You ordered piiza")
    elif (x.get() == 1):
        print("You ordered hamb")
    elif (x.get() == 2):
        print("You ordered hotdog")
    else:
        print("Huh?")
window = Tk()
x = IntVar()
pizza_image = PhotoImage(file="files/pngegg.png")
hamburger_image = PhotoImage(file="files/pngegg1.png")
hotdog_image = PhotoImage(file="files/pngegg1.png")
food_images = [pizza_image, hamburger_image, hotdog_image]
for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index],#adds text to radio buttons
                              variable=x, #groups radiobuttons together if they share the same variable
                              value=index, #assigns each radiobutton a different value
                              padx=25,  #adds padding on x-axis
                              font=("Impact", 50),
                              image=food_images[index], #adds image to radiobutton
                              compound=LEFT,
                              indicatoron=1, #eliminate circle indicators if 0
                              width=300, #sets width of radio buttons)
                              command=order)
    radiobutton.pack(anchor=W)


window.mainloop()

# Lesson 72 Scale
from tkinter import *

def submit():
    print(f"the temp is {scale.get()} degrees")

window = Tk()
hot = PhotoImage(file="files/pngegg2.png")
hot_label = Label(image=hot)
hot_label.pack()


scale = Scale(window, from_=100, to=0,
              length=600, orient=VERTICAL,
              font=("Consolas", 20),
              tickinterval=10,
              showvalue=0,
              resolution=5,
              troughcolor="#69EAFF",
              fg="black",
              bg="grey") #step
#scale.set(20) #set beginning
scale.set(((scale['from']-scale['to'])/2)+scale['to']) #set center

scale.pack()

ham = PhotoImage(file="files/pngegg1.png")
ham_label = Label(image=ham)
ham_label.pack()

button = Button(window, text="submit", command=submit)
button.pack()


window.mainloop()

# Lesson 73
# listbox = A listing of selectable text items within it's own container
from tkinter import *

def submit():
    food = []
    for index in list_box.curselection():
        food.insert(index,list_box.get(index))
    print("U have ordered: ",end="")
    #print(list_box.get(list_box.curselection()))
    for index in food:
        print(index)

def add():
    list_box.insert(list_box.size(), entry_box.get())

    list_box.config(height=list_box.size())
def delete():
    #list_box.delete(list_box.curselection())
    for index in reversed(list_box.curselection()):
        list_box.delete(index)

window = Tk()



list_box = Listbox(window,
                   bg="black",
                   fg="white",
                   font=("Constantia", 30,),
                   width=15,
                   selectmode=MULTIPLE)

list_box.pack()

list_box.insert(1, "pizza")
list_box.insert(2, "pasta")
list_box.insert(3, "garlic")
list_box.insert(4, "soup")
list_box.insert(5, "salad")

list_box.config(height=list_box.size())

entry_box = Entry(window)
entry_box.pack()

submit_button = Button(window, text="submit", command=submit)
submit_button.pack()
add_button = Button(window, text="add", command=add)
add_button.pack()
delete_button = Button(window, text="delete", command=delete)
delete_button.pack()

window.mainloop()

# Lesson 74 messagebox
from tkinter import *
from tkinter import messagebox

def click():
    #messagebox.showinfo(title="This info", message="You are human")
    #while True:
    #    messagebox.showwarning(title="This info", message="You are human")
    #messagebox.showerror(title="This info", message="Wrong")
    #if messagebox.askokcancel(title="ASK", message="DO YOu want?"):
    #    print("U did it")
    #else:
    #    print("U cancelled")
    #if messagebox.askretrycancel(title="ASK", message="DO YOu want?"):
    #    print("U did it")
    #else:
     #   print("U cancelled")
    #if messagebox.askyesno(title="Ask yes or no", message="Do u like cake?"):
    #     print("I like cake too")
    #else:
    #    print("Why not?")
    #answer = messagebox.askquestion(title="Question", message="Do you like pie")
    #if answer == "yes":
    #    print("I like also")
    #else:
    #    print("Why not")
    answer = messagebox.askyesnocancel(title="Yes No Cancel", message="Do you like coding", icon="warning")
    if answer == True:
        print("U like")
    elif answer == False:
        print("Why")
    else:
        print("You dodged")


window = Tk()

button = Button(window, command=click, text="clicl me")
button.pack()


window.mainloop()

# Lesson 75 colorchooser
from tkinter import *
from tkinter import colorchooser

def click():
    window.config(bg=colorchooser.askcolor()[1])
    #color = colorchooser.askcolor()
    #colorHex = color[1]


window = Tk()
window.geometry("500x500")
button = Button(text="click me", command=click)
button.pack()

window.mainloop()

# Lesson 76 text area

# text widget = functions like a text area, you can enter multiple lines of text
from tkinter import *

def submit():
    input = text.get("1.0", END) #any name for variable + .get with starting Index -1.0 and last index END
    print(input)
window = Tk()

text = Text(window, bg="light yellow",
            font=("Ink Free", 20),
            height=10,
            width=20,
            padx=20,
            pady=20,
            fg="red")

text.pack()

button = Button(window, text="submit", command=submit)
button.pack()



window.mainloop()

# Lesson 77 filedialog open

from tkinter import filedialog
from tkinter import *

def openFile():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\1\\PycharmProjects\\pythonProject1",
                                          title="open File okay",
                                          filetypes=(("text files", "*txt"),("maga files", "*.*")))
    if FileNotFoundError:
        return
    #filepath = filedialog.askopenfilename()
    file = open(filepath, 'r')
    print(file.read())
    file.close()

window = Tk()

button = Button(text="Open", command=openFile).pack()

window.mainloop()

# Lesson 78save a file (file dialog)

from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\1\\PycharmProjects\\pythonProject1",
                                    defaultextension='.txt',
                                    filetypes=[
                                        ('Text file', ".txt"),
                                        ('HTML file', ".html"),
                                        ('All files', ".*")
                                    ])
    if file is None:
        return
    #filetext = str(text.get(1.0, END))
    filetext = input("Enter some text: ")
    file.write(filetext)
    file.close()

window = Tk()
button = Button(text='save', command=saveFile)
button.pack()
text = Text(window)
text.pack()
window.mainloop()


# Lesson 79 menubar
from tkinter import *

def openFile():
    print("Opened")
def saveFile():
    print("Saved")
def cut():
    print("Cutted")
def copy():
    print("copied")
def paste():
    print("pasted")



window = Tk()

saveimage = PhotoImage(file='files/floppy-disk.png')
fileimage = PhotoImage(file='files/folder.png')
exitimage = PhotoImage(file='files/button.png')

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=0, font=("Ink free", 10))
menubar.add_cascade(label="file", menu=fileMenu)
#fileOpen = Menu(menubar)
#menubar.add_cascade(label='open', menu=fileOpen)
fileMenu.add_command(label="Open", command=openFile, image=saveimage, compound=LEFT)
fileMenu.add_command(label="save", command=saveFile, image=fileimage,compound=LEFT)
fileMenu.add_separator()
fileMenu.add_command(label="exit", command=quit, image=exitimage,compound=LEFT)

editMenu = Menu(menubar, tearoff=0,font=("Ink free", 10))
menubar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut", command=cut)
editMenu.add_command(label="Copy", command=copy)
editMenu.add_command(label="Paste", command=paste)


window.mainloop()

#Lesson 80 Frames
from tkinter import *
window = Tk()

frame = Frame(window, bg="pink", bd=6, relief=SUNKEN)
frame.place(x=100, y=100)


buttonW = Button(frame, text="W", font=("Consolas", 25), width=3).pack(side=TOP)
buttonA = Button(frame, text="A", font=("Consolas", 25), width=3).pack(side=LEFT)
buttonS = Button(frame, text="S", font=("Consolas", 25), width=3).pack(side=LEFT)
buttonD = Button(frame, text="D", font=("Consolas", 25), width=3).pack(side=LEFT)





window.mainloop()

#Lesson 81 New windows
from tkinter import *


from tkinter import *

def create_window():
    new_window = Tk()       #Toplevel() = new window 'on top' of other windows, linked to a 'bottom' window
                            #Tk() = new independent window
    #old_window.destroy()   #close out of old window

old_window = Tk()

Button(old_window,text="create new window",command=create_window).pack()

old_window.mainloop()

#Lesson 82 tabs

from tkinter import *
from tkinter import ttk

window = Tk()

notebook = ttk.Notebook(window) #widget that manages a collection of windows/displays

tab1 = Frame(notebook) #new frame for tab 1
tab2 = Frame(notebook) #new frame for tab 2

notebook.add(tab1,text="Tab 1")
notebook.add(tab2,text="Tab 2")
notebook.pack(expand=True,fill="both")  #expand = expand to fill any space not otherwise used
                                       #fill = fill space on x and y axis
Label(tab1,text="Hello, this is tab#1",width=50,height=25).pack()
Label(tab2,text="Goodbye, this is tab#2",width=50,height=25).pack()

window.mainloop()

#Lesson 83 #grid() = geometry manager that organizes widgets in a table-like structure in a parent widget

from tkinter import *

window = Tk()
titleLabel = Label(window, text="Enter your info", font=("Arial", 25)).grid(row=0, column=0, columnspan=2)

firstNameLabel = Label(window,text="First name: ").grid(row=1, column=0)
firstNameEntry = Entry(window).grid(row=1, column=1)

lastNameLabel = Label(window,text="Last name: ").grid(row=2, column=0)
lastNameEntry = Entry(window).grid(row=2, column=1)

emailNameLabel = Label(window,text="Last name: ").grid(row=3, column=0)
emailNameEntry = Entry(window).grid(row=3, column=1)

submitButton = Button(window, text="Submit").grid(row=4, column=0, columnspan=2)

window.mainloop()


#Lesson 84 progress bar
from tkinter import *
from tkinter.ttk import *
import time

def start():
    GB = 50
    download = 0
    speed = 2
    while(download<GB):
        time.sleep(0.05)
        bar['value']+=(speed/GB)*100
        download+=speed
        percent.set(str(int((download/GB)*100))+"%")
        text.set(str(download)+"/"+str(GB)+"GB completed")
        window.update_idletasks()
window = Tk()
percent = StringVar()
text = StringVar()
Button(window, text="download", command=start).pack()
bar = Progressbar(window, orient=HORIZONTAL, length=300)
bar.pack(pady=10)

percentLabel = Label(window, textvariable=percent).pack()
TaskLabel = Label(window, textvariable=text).pack()


window.mainloop()

#Lesson 85# canvas =  widget that is used to draw graphs, plots, images in a window

from tkinter import *

window = Tk()

canvas = Canvas(window,height=500, width=500)
#canvas.create_line(0,0,500,500, fill="blue",  width=5)
#canvas.create_line(0,500,500,0, fill="red",  width=5)
#canvas.create_rectangle(50,50,250,250, fill="purple")
#points = [250, 0,500,500,0,500]
#canvas.create_polygon(points, fill="green", outline="black", width=5)
#canvas.create_arc(0,0,500,500, style=PIESLICE,start=270, extent=180)
canvas.create_arc(0,0,500,500, fill="red",extent=180, width=10)
canvas.create_arc(0,0,500,500, fill="white",extent=180,start=180, width=10)
canvas.create_oval(190,190,310,310, fill="white", width=10)
canvas.pack()

window.mainloop()
#Lesson 86 key bind events
from tkinter import *

def doSomething(event):
    #print("U pressed: "+ event.keysym)
    label.config(text=event.keysym)

window = Tk()
window.bind("<Key>", doSomething)
label = Label(window, font=("Ink Free",100))
label.pack()

window.mainloop()

#Lesson 87 Mouse events
from tkinter import *

def doSomething(event):
    print("Mouse coordinates: " + str(event.x)+","+str(event.y))

window = Tk()

window.bind("<Button-1>",doSomething) #left mouse click
#window.bind("<Button-2>",doSomething) #scroll wheel
#window.bind("<Button-3>",doSomething) #right mouse click
#window.bind("<ButtonRelease>",doSomething)#mousebutton release
#window.bind("<Enter>",doSomething) #enter the window
#window.bind("<Leave>",doSomething) #leave the window
#window.bind("<Motion>",doSomething) #Where the mouse moved
window.mainloop()

#Lesson 88 drag & drop
from tkinter import *
def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y
def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x, y=y)

window = Tk()

label = Label(window, bg="red", width=10, height=5)
label.place(x=0, y=0)
label2 = Label(window, bg="blue", width=10, height=5)
label2.place(x=110, y=110)


label.bind("<Button-1>", drag_start)
label.bind("<B1-Motion>", drag_motion)

label2.bind("<Button-1>", drag_start)
label2.bind("<B1-Motion>", drag_motion)



window.mainloop()

#Lesson 89 move images w/ keys

from tkinter import *

def move_up(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()-10)
def move_down(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()+10)
def move_left(event):
    label.place(x=label.winfo_x()-10, y=label.winfo_y())
def move_right(event):
    label.place(x=label.winfo_x()+10, y=label.winfo_y()-10)

window = Tk()
window.geometry("500x500")

window.bind("<w>", move_up)
window.bind("<s>", move_down)
window.bind("<a>", move_left)
window.bind("<d>", move_right)

window.bind("<Up>", move_up)
window.bind("<Down>", move_down)
window.bind("<Left>", move_left)
window.bind("<Right>", move_right)


myImage = PhotoImage(file="files/race.png")
label = Label(window, image=myImage)
label.place(x=20, y=100)




window.mainloop()
#MOOOOOOOOOOOOOVING CANVAS IMAGE
from tkinter import *

def move_up(event):
    canvas.move(my_image,0,-10)
def move_down(event):
    canvas.move(my_image, 0, +10)
def move_left(event):
    canvas.move(my_image,-10,0)
def move_right(event):
    canvas.move(my_image,+10,0)


window = Tk()
window.bind("<w>", move_up)
window.bind("<s>", move_down)
window.bind("<a>", move_left)
window.bind("<d>", move_right)

window.bind("<Up>", move_up)
window.bind("<Down>", move_down)
window.bind("<Left>", move_left)
window.bind("<Right>", move_right)


canvas = Canvas(window,width=500, height=500)
canvas.pack()
photo = PhotoImage(file="files/race.png")

my_image = canvas.create_image(0,0,image=photo, anchor=NW)


window.mainloop()

#Lesson 90 Animations
import time
from tkinter import *

WIDTH = 500
HEIGHT = 500
xVelocity = 1
yVelocity = 1

window = Tk()
canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

bg_image = PhotoImage(file="files/spacce.png")
myBg_image = canvas.create_image(0,0, image=bg_image, anchor=NW)

photo_image = PhotoImage(file="files/race.png")
my_image = canvas.create_image(0,0, image=photo_image, anchor=NW)


image_width = photo_image.width()
image_height = photo_image.height()

while True:
    coordinates = canvas.coords(my_image)
    print(coordinates)
    if coordinates[0] >= WIDTH-image_width or coordinates[0] < 0:
        xVelocity = -xVelocity
    if coordinates[1] >= WIDTH-image_height or coordinates[1] < 0:
        yVelocity = -yVelocity
    canvas.move(my_image,xVelocity,yVelocity)
    window.update()
    time.sleep(0.01)




window.mainloop()
#Lesson 91 Multiple Animations
import time
from tkinter import *
from Ball import *
WIDTH = 500
HEIGHT = 500

window = Tk()
canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

volleyball = Ball(canvas, 0,0, 100, 1, 1, 'white')
tennisball = Ball(canvas, 0,0, 50, 4, 3, 'yellow')
basketsball = Ball(canvas, 0,0, 77, 7, 9, 'red')

while True:
    volleyball.move()
    tennisball.move()
    basketsball.move()
    window.update()
    time.sleep(0.01)


window.mainloop()
#Lesson 92 clock program
import time
from tkinter import *
from time import *

def update():
    time_string = strftime("%H:%M:%S")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d %Y")
    date_label.config(text=date_string)

    window.after(1000,update)

window = Tk()

time_label = Label(window, font=("Arial", 50),fg="White", bg="blue")
time_label.pack()
day_label = Label(window, font=("Ink Free", 25),fg="White", bg="blue")
day_label.pack(expand=True, fill="both")
date_label = Label(window, font=("Ink Free", 25))
date_label.pack()


update()

window.mainloop()

#Lesson 93 Send Email

import smtplib

sender = "ingarbi006@gmail.com"
receiver = "ibi-87@yandex.ru"
password = "Vaysite1993"
subject = "PYTHOOOOOOOOOOOn"
body = "TEEEEEEEEEEEEEEEEST"

#header
message = f""""From: Arbi{sender}
To: Hamzat {receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try:
    server.login(sender, password)
    print("Logged in...")
    server.sendmail(sender, receiver, message)
    print("Email has been sent")
except smtplib.SMTPAuthenticationError:
    print("unable to sign in")
#Lesson 94 Command prompt
# *****************************
# run .py file with cmd
# *****************************
# save file as .py (Python file)
# go to command prompt
# navigate to directory w/ your file: cd C:\Users\BroCode\Desktop
# invoke python interpreter + script: python hello_world.py
print("Hello world")

name = input("Whats name: ")

print("Hello " +name)
#Lesson 95 Pip

#Lesson 96 py to Exe

#Lesson 97 Calculator

from tkinter import *

def button_press(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

def equals():
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except SyntaxError:
        equation_label.set("Syntax Error")
        equation_text = ""
    except ZeroDivisionError:
        equation_label.set("Ariphmetic error")
        equation_text = ""
def clear():
    global equation_text
    equation_label.set("")
    equation_text = ""

window = Tk()
window.title("Calculator program by ARBY")
window.geometry('500x500')
equation_text = ""
equation_label = StringVar()
label = Label(window, textvariable=equation_label,font=("Ink Free", 20), bg="purple",fg="white", width=24, height=2)
label.pack()

frame = Frame(window)
frame.pack()
button1 = Button(frame, text=1, height=4,width=9, font=35,
                command=lambda: button_press(1))
button1.grid(row=0,column=0)
button2 = Button(frame, text=2, height=4,width=9, font=35,
                command=lambda: button_press(2))
button2.grid(row=0,column=1)
button3 = Button(frame, text=3, height=4,width=9, font=35,
                command=lambda: button_press(3))
button3.grid(row=0,column=2)
button4 = Button(frame, text=4, height=4,width=9, font=35,
                command=lambda: button_press(4))
button4.grid(row=1,column=0)
button5 = Button(frame, text=5, height=4,width=9, font=35,
                command=lambda: button_press(5))
button5.grid(row=1,column=1)
button6 = Button(frame, text=6, height=4,width=9, font=35,
                command=lambda: button_press(6))
button6.grid(row=1,column=2)

button7 = Button(frame, text=7, height=4,width=9, font=35,
                command=lambda: button_press(7))
button7.grid(row=2,column=0)

button8 = Button(frame, text=8, height=4,width=9, font=35,
                command=lambda: button_press(8))
button8.grid(row=2,column=1)

button9 = Button(frame, text=9, height=4,width=9, font=35,
                command=lambda: button_press(9))
button9.grid(row=2,column=2)

button0 = Button(frame, text=0, height=4,width=9, font=35,
                command=lambda: button_press(0))
button0.grid(row=3,column=0)

plus_button = Button(frame, text="+", height=4,width=9, font=35,
                command=lambda: button_press("+"))
plus_button.grid(row=0,column=3)

minus_button = Button(frame, text="-", height=4,width=9, font=35,
                command=lambda: button_press("-"))
minus_button.grid(row=1,column=3)

multiply_button = Button(frame, text="*", height=4,width=9, font=35,
                command=lambda: button_press("*"))
multiply_button.grid(row=2,column=3)

divide_button = Button(frame, text="/", height=4,width=9, font=35,
                command=lambda: button_press("/"))
divide_button.grid(row=3,column=3)

equal_button = Button(frame, text="=", height=4,width=9, font=35,
                command=equals)
equal_button.grid(row=3,column=2)

decimal_button = Button(frame, text=".", height=4,width=9, font=35,
                command=lambda: button_press("."))
decimal_button.grid(row=3,column=1)

clear_button = Button(window, text="Clear", height=4,width=15, font=35,
                command=clear)
clear_button.pack()


window.mainloop()


# Lesson 98 text editor program
import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *


def change_color():
    color = colorchooser.askcolor(title="Pick a color")
    text_area.config(fg=color[1])


def change_font(*args):
    text_area.config(font=(font_name.get(), size_box.get()))


def new_file():
    window.title("Untitled")
    text_area.delete(1.0, END)


def open_file():
    file = askopenfilename(defaultextension=".txt",
                           file=[("All Files", "*.*"),
                                 ("Text Documents", "*.txt")])

    if file is None:
        return

    else:
        try:
            window.title(os.path.basename(file))
            text_area.delete(1.0, END)

            file = open(file, "r")

            text_area.insert(1.0, file.read())

        except Exception:
            print("could not read file")
        finally:
            file.close()


def save_file():
    file = filedialog.asksaveasfilename(initialfile='unititled.txt',
                                        defaultextension=".txt",
                                        filetypes=[("All Files", "*.*"),
                                                   ("Text Documents", "*.txt")])

    if file is None:
        return
    else:
        try:
            window.title(os.path.basename(file))
            file = open(file, "w")
            file.write(text_area.get(1.0, END))
        except Exception:
            print("could not save file")
        finally:
            file.close()


def cut():
    text_area.event_generate("<<Cut>>")


def copy():
    text_area.event_generate("<<Copy>>")


def paste():
    text_area.event_generate("<<Paste>>")


def about():
    showinfo("ABOUT THIS PROGRAM", "THIS OUR PROGRAM")


def quit():
    window.destroy()


window = Tk()
window.title("text editor")
file = None

window_width = 500
window_height = 500

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))  # Center

font_name = StringVar(window)
font_name.set("Arial")
font_size = StringVar(window)
font_size.set("25")
text_area = Text(window, font=(font_name.get(), font_size.get()))

scroll_bar = Scrollbar(text_area)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
text_area.grid(sticky=N + E + S + W)
scroll_bar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scroll_bar.set)

frame = Frame(window)
frame.grid()
color_button = Button(frame, text="color", command=change_color)
color_button.grid(row=0, column=0)

font_box = OptionMenu(frame, font_name, *font.families(), command=change_font)
font_box.grid(row=0, column=1)

size_box = Spinbox(frame, from_=1, to=100, textvariable=font_size, command=change_font)
size_box.grid(row=0, column=2)

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="file", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)

edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="file", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)

window.mainloop()

# Lesson 99 Tic Tac Toe Fame
from tkinter import *
import random


def next_turn(row, column):
    global player

    if buttons[row][column]["text"] == "" and check_winner() is False:
        if player == players[0]:
            buttons[row][column]["text"] = player

            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1]+"turn"))

            elif check_winner() is True:
                label.config(text=(players[0]+"wins"))

            elif check_winner() == "Tie":
                label.config(text="Tie")
        else:
            buttons[row][column]["text"] = player

            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0] + "turn"))
            elif check_winner() is True:
                label.config(text=(players[1] + "wins"))
            elif check_winner() == "Tie":
                label.config(text="Tie")

def check_winner():
    for row in range(3):
       if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
           buttons[row][0].config(bg="green")
           buttons[row][1].config(bg="green")
           buttons[row][2].config(bg="green")

           return True
       for column in range(3):
           if buttons[0][column]["text"] == buttons[1][column]["text"] == buttons[2][column]["text"] != "":
               buttons[0][column].config(bg="green")
               buttons[1][column].config(bg="green")
               buttons[2][column].config(bg="green")
               return True
       if buttons[0][0]["text"] == buttons[1][1]== buttons[2][2] != "":
           buttons[0][0].config(bg="green")
           buttons[1][1].config(bg="green")
           buttons[2][2].config(bg="green")
           return True
       if buttons[0][2]["text"] == buttons[1][1] == buttons[2][0] != "":
           buttons[0][2].config(bg="green")
           buttons[1][1].config(bg="green")
           buttons[2][0].config(bg="green")
           return True
       elif empty_spaces() is False:
           for row in range (3):
               for column in range(3):
                   buttons[row][column].config(bg="yellow")
           return "Tie"
       else:
           return False
def empty_spaces():
    spaces = 9
    for row in range(3):
        for column in range(3):
            if buttons [row][column]["text"] != "":
                spaces -=1
    if spaces == 0:
        return False
    else:
        return True

def new_game ():
    global player
    player = random.choice(players)
    label.config(text=player+"turn")
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#F0F0F0")

window = Tk()
window.title("TIC TAC TOE")
players = ["x", "o"]
player = random.choice(players)
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]
label = Label(text=player+"turn", font=('ink free', 40))
label.pack(side='top')
reset_button = Button(text="restart", font=("consolas", 20), command=new_game)
reset_button.pack(side="top")
frame = Frame(window)
frame.pack()

for row in range(3):
   for column in range(3):
       buttons[row][column] = Button(frame, text="",font=('ink free', 40),
                                     width=5, height=2, command=lambda row=row, columm=column:next_turn(row,columm))
       buttons[row][column].grid(row=row, column=column)


window.mainloop()


# Lesson 100 Snake game
from tkinter import *
import random

GAME_WIDTH = 600
GAME_HEIGHT = 600
SPEED = 80
SPACE_SIZE = 40
BODE_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"



class Snake:
    def __init__(self):
        self.body_size = BODE_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODE_PARTS):
            self.coordinates.append([0,0])
        for x , y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)



class Food:
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE)-1) * SPACE_SIZE
        self.coordinates = [x,y]
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

def next_turn(snake, food):
    x, y = snake.coordinates[0]
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE
    snake.coordinates.insert(0,(x,y))
    square = canvas.create_rectangle(x, y, x +SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0,square)
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text="Score:{}".format(score))
        canvas.delete("food")
        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del  snake.squares[-1]
    if check_collisions(snake):
        game_over()
    else:
        window.after(SPEED,next_turn,snake,food)
def change_direction(new_direction):
    global direction

    if new_direction == "left":
        if direction != "right":
            direction = new_direction
    elif new_direction == "right":
        if direction != "left":
            direction = new_direction
    elif new_direction == "up":
        if direction != "down":
            direction = new_direction
    elif new_direction == "down":
        if direction != "up":
            direction = new_direction
def check_collisions(snake):
    x, y = snake.coordinates[0]
    if x < 0 or x >= GAME_WIDTH:
        return True
    if y < 0 or y >= GAME_HEIGHT:
        return True
    for bode_part in snake.coordinates[1:]:
        if x == bode_part[0] and y == bode_part[1]:
            return True
    return False

def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=("consolas", 50), text="Game Over",
                       fill="red", tag="gameover")

window = Tk()
window.title("Snake game")
window.resizable(False, False)


score = 0
direction = "down"

label = Label(window, text="Score: {}".format(score), font=("consolas", 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()
window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))
window.geometry(F"{window_width}x{window_height}+{x}+{y}")

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))


snake = Snake()
food = Food()
next_turn(snake, food)

window.mainloop()













