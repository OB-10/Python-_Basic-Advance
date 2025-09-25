#print('Hello World!')  #use print function to print print anything


# result=10+5-2*(3/2)**2 #python follows BODMAS rule
# print(result)


# is used as a single line comment
"""
This is a multi-line comment"""

''' #This is also a multi-line comment'''


#Variables and Data Types
# x=10 #integer
# y=3.5 #float

# print(type(x)) #to check the data type of variable
# print(type(y))

# print(x+y) #addition
# print(x-y) #subtraction 
# print(x*y) #multiplication
# print(x/y) #division (always returns float)
# print(x//y) #floor division (returns integer value)
# print(x**y) #exponentiation (x raised to the power y)
# print(x%y) #modulus (returns the remainder value)



# #Comparison Operators
# x=10
# y=5

# print(x==y) #equal to
# print(x!=y) #not equal to
# print(x>y) #greater than
# print(x<y) #less than   
# print(x>=y) #greater than or equal to
# print(x<=y) #less than or equal to


"""Logical Operators

and=all conditions must be true to return true
or=at least one condition must be true to return true
not=negates the boolean value


"""
"""
age=20
is_student=False

print(age>18 and is_student) #True and False=False
print(age>18 or is_student) #True or False=True  
print(not is_student) #not False=True
print(not age>18) #not True=False
"""
"""
a=10
b=20

print(a==b) #False
print(a!=b)#True
print(a>b and a!=b) #False and True=False
print(a<b or a!=b) #True or True=True
print(not a>b) #not False=True
print(not a<b) #not True=False
"""



# a=10
# b=20
# a+=b
# print(a)

# a-=b
# print(a)    
# a*=b
# print(a)
# a/=b
# print(a)


"""
is=true if both variables point to the same object in memory
is not=true if both variables point to different objects in memory
"""

"""

a=[1,2,3]
b=a
c=[1,2,3]
print(a is b) #True
print(a is c) #False   not comparing values but memory location
print(a is not c) #True
print(a is not b) #False
print(1 in c) #True checeks if value is present in the list or not
print(5 in c) #False
print(5 not in c) #True
"""

"""
arithmetic operators=+,-,*,/,//,**,%  -all mathematical operations
assignment operators==,+=,-=,*=,/=,//=,**=,%= -assignment of values to variables
comparison operators==,!=,>,<,>=,<= -to compare two values
logical operators=and,or,not -to combine conditional statements
identity operators=is,is not -to compare memory locations of two objects
membership operators=in,not in -to test if a sequence contains a value
bitwise operators=&,|,^,~,<<,>> -to perform bit-level operations on integers
 """





#control statements
# if,elif,else


# pie=3.14
# radius=input("Enter the radius of circle: ")
# # area=pie*radius*radius
# # print("Area of circle is:",area)

# if radius<0:
#     print("Radius cannot be negative")
# elif radius==0:
#     print("Area of circle is 0")
# elif radius==str:
#     print("Please enter a valid number")
# else:
#     print("Area of circle is:",pie*radius**2)




# age=int(input("Enter your age: "))

# if age >= 18:
#     print("You are eligible to vote")
# elif age<=0:
#     print("Please enter a valid age")
# elif age<100:
#     print("You are not eligible to vote")
# else:
#     print("You are not eligible to vote")



######calculator#######
"""
num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
operator=input("Enter operator (+,-,*,/): ")

if operator=='+':
    print(num1+num2)
elif operator=='-':
    print(num1-num2)
elif operator=='*':
    print(num1*num2)
elif operator=='/':
    if num2==0:
        print("Cannot divide by zero")
    else:
        print(num1/num2)
else:
    print("Invalid operator")  """



#########loops##########
# for loop=used to iterate over a sequence (like a list, tuple, dictionary, set, or string)... used when number of iterations is known
#while loop =used to iterate as long as a condition is true ... used when number of iterations is unknown


# i=1
# while i<=5:
#     print(i)
#     i+=1 #it increases the value of i by 1 in each iteration to avoid infinite loop
# print("While loop ended")

# for i in range(1,6,1): #range(start,end,step)
#     print(i)
# print("For loop ended")



# for i in range(1,5):
#     for j in range(2,5):
#         print(f'{i},{j}')    


"""
for i in range(1,11):
    if i==8:
        break  #break statement is used to exit the loop
    if i==3:
        continue #continue statement is used to skip the current iteration and move to the next iteration
    if i==5:
        pass #pass statement is used as a placeholder when no action is required
    print(i)
"""



"""# print numbers from start to end except skip number
start=int(input("Enter start number: "))
end=int(input("Enter end number: "))

skip=int(input("Enter skip number: "))


if start>end:
    print("Invalid range")

elif skip<start or skip>end:
    print("Skip number should be between start and end")
else:
    for i in range(start,end+1):

        if i==skip:
            continue
        print(i)
"""



############strings and characters##########
# name='John Doe'

# name1="Jane Doe"

# name2='''Jane Doe'''

# print(name,name1,name2) #all three are same

#string are immutable i.e cannot be changed just modified
#indexing and slicing can be done on strings .starts from 0 and -1 from end
# name[0]='j' #this will give error as strings are immutable


#slicing
# text="Hello, welcome to Python programming"
# print(text[0:5]) #Hello
# print(text[7:14]) #welcome
# print(text[::-1]) #gnimmargorp nohtyP ot emoclew ,olleH
# print(text[-11:]) #programming

# print(text*10) #prints the string 10 times


#############membership operators############
"""
text="Hello, welcome to Python programming"
print('Python' in text) #True checks if the substring is present in the string or not
print('Java' in text) #False

email="user@gmail.com"

if '@' in email and '.' in email:
    print("Valid email")
else:
    print("Invalid email")

"""


"""


name="  Om Parag Bambale  "

print(name.lower()) #om parag bambale
print(name.upper()) #OM PARAG BAMBALE

print(name.title()) #Om Parag Bambale
print(name.capitalize()) #Om parag bambale
print(name.swapcase()) #om parag bambale
print(name.count('a')) #4 counts the number of occurrences of a substring in the string
print(name.find('Parag')) #3 returns the index of the first occurrence of the substring
print(name.replace('Bambale','Smith')) #Om Parag Smith replaces the substring with another substring
print(name.split(' ')) #['Om', 'Parag', 'Bambale']
print(name.join([", "])) #OmParagBambale joins the list of strings into a single string
print(name.strip()) #Om Parag Bambale removes leading and trailing whitespaces
print(name.lstrip()) #Om Parag Bambale removes leading whitespaces'
print(name.rstrip()) #  Om Parag Bambale removes trailing whitespaces
print(name.isalpha()) #False checks if all characters in the string are alphabetic
print(name.isdigit()) #False checks if all characters in the string are digits
print(name.isspace()) #False checks if all characters in the string are whitespaces

 """


##########list and tuples##########
# list is mutable i.e can be changed
# tuple is immutable i.e cannot be changed
# list=[]
# tuple=()


"""
list1=[1,2,3,4,5]
tuple1=(1,2,3,4,5)
print(type(list1)) #<class 'list'>
print(type(tuple1)) #<class 'tuple'>

list2=list((1,2,3,4,5)) #converting tuple to list
tuple2=tuple((1,2,3,4,5)) #converting list
print(type(list2)) #<class 'list'>
print(type(tuple2)) #<class 'tuple'>

print(f'Before modification list1:{list1}')

list1[0]=10 #modifying the first element of the list
print(f'After modification list1:{list1}')

list1[1:3]=[20,30,40] #modifying multiple elements of the list
print(f'After modification list1:{list1}')

"""

#alias


"""
list1=[1,2,3,4,5]
list2=list1 #both list1 and list2 point to the same memory location
list3=list1.copy() #list3 is a copy of list1 and points to a different memory location

# list1[0]=10
# list3[4]=50
# print(list1,list2,list3) #[10, 2, 3, 4, 5] [10, 2, 3, 4, 5] [1, 2, 3, 4, 50]

list3[0:4]=10,20,30,40 #modifying multiple elements of the list
list3.append(60) #adds an element to the end of the list
print(list3) #[1, 2, 3, 4, 50,


a=[1,2,3]
b=[4,5,6]
a.append(b) #appends the entire list b as a single element to list a
print(a) #[1, 2, 3, [4, 5, 6]]

a.extend(b) #extends the list a by adding elements of list b
print(a) #[1, 2, 3, [4, 5, 6], 4, 5, 6]

a.insert(0,10) #inserts an element at a specific index
print(a) #[1, 10, 2, 3, [4, 5, 6], 4, 5, 6]

print(len(a)) #8 returns the number of elements in the list

a.remove(1) #removes the first occurrence of the element from the list
print(a) #[1, 2, 3, [4, 5, 6], 4, 5, 6]

b.pop(0) #removes and returns the last element of the list
print(b) #[4, 5]

a.clear() #removes all elements from the list
print(a) #[]
"""
"""
a=[1,2,3,4,5,2,1,1,2,1,2,6,12,3,2,1]
print(a.index(4)) #returns the index of the first occurrence of the element in the list
print(a.count(1)) #returns the number of occurrences of the element in the list
a.sort() #sorts the list in ascending order
print(a) #[1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 5, 6, 12]
a.reverse() #reverses the list
print(a) #[12, 6, 5, 4, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1]

print(min(a)) #1 returns the minimum element in the list
print(max(a)) #12 returns the maximum element in the list

"""

# a=[1,2,3,4,5]
# b=[3,4,5,6,7]
# a1=set(a) #converting list to set to remove duplicates and perform set operations
# b1=set(b)
# c=a1.intersection(b1) #returns the common elements in both lists
# print(list(c)) #[3,4,5]




"""[Expression for item in iterable if condition]

e-x+c*2
item for item in iterable
iterable -range(1,10)
condition  opetional
"""
"""
a=[a for a in range (1,11) if a%2==0] #squares of numbers from 1 to 10
squares=[x:x**2 for x in range (1,11) if x%2==0] #squares of even numbers from 1 to 10
print(a,':',squares) #[4, 16, 36, 64, 100]
"""


##########dictionaries and sets##########
#dictionary is a collection of key-value pairs
# set is a collection of unique elements
#dictionary is mutable i.e can be changed
# set is mutable i.e can be changed
#dictionary={}
# set={}

#creating dictionary
"""
student={
    "name":"Om","Surname":"Bambale","DOB":"01-01-2000","age":24, "is_student":True, "marks":{"Maths":90,"Science":85,"English":88}
}

student["marks"]["Maths"]=95 #modifying the value of a key in the dictionary
student["marks"]["SST"]=80 #adding a new key-value pair to the dictionary

print(student["marks"]["Maths"]) #95
print(f'old_age,{student["age"]}') #24

student["age"]=25 #modifying the value of a key in the dictionary
print(f'new_age,{student["age"]}') #25


del student["marks"]["Science"]#deleting a key-value pair from the dictionary
print(student)

"""

#dic get methods



"""
profile={"name":"XYZ","age":24,"city":"Pune"}

age=profile.get("age2","Not Found") #returns the value of the key if it exists, else returns None
profile["country"]="India"
country=profile.get("country") #returns the value of the key if it exists, else returns the default value
print(age) #24
print(country) #India

Keys=profile.keys() #returns a list of all keys in the dictionary
Values=profile.values() #returns a list of all values in the dictionary
items=profile.items() #returns a list of all key-value pairs in the dictionary as tuples


print(Keys) #dict_keys(['name', 'age', 'city', 'country'])
print(list(Values)) #dict_values(['XYZ', 24, 'Pune', 'India'])
print(list(items)) #dict_items([('name', 'XYZ'), ('age', 24), ('city', 'Pune'), ('country', 'India')])


popped=profile.pop("age") #removes the key-value pair from the dictionary and returns the value of the key
print(popped) #24'

print(profile) #{'name': 'XYZ', 'city': 'Pune', 'country': 'India'}

popped_item=profile.popitem() #removes the last inserted key-value pair from the dictionary and returns it as a tuple
print(popped_item) #('country', 'India')



cleared=profile.clear() #removes all key-value pairs from the dictionary
print(cleared) #None
print(profile) #{}

for k in profiles.keys():
    print(k) #prints all keys in the dictionary
for v in profiles.values():
    print(v) #prints all values in the dictionary
for i in profiles.items():
    print(i) #prints all key-value pairs in the dictionary as tuples
"""


# squares={x:x**2 for x in range (1,11) if x%2==0} #dictionary comprehension
# print(squares)





############functions##########

"""
def add(a,b):
    return a+b

print(add(10,20))

def greet (name='raj',city='pune' ):
    print(f'Hello {name},welcome to {city}')

greet('ABC','pune')
greet() #uses default values
greet(city='mumbai',name='sam')
"""

#local and global variables 

"""
message="Hello, World!" #global variable

def greet():
    mes="Hello, Python!" #local variable
    print(mes)
    print(message) #accessing global variable inside the function

greet()
print(mes) #this will give error as mes is a local variable and cannot be accessed outside the function
print(message) #accessing global variable outside the function
"""



#decorators
"""
def decorator_function(func):
    def wrapper():
        print("Before function execution")
        func()
        print("Executing function...")
        func()
        print("After function execution")
    return wrapper

@decorator_function
def say_hello():
    print("Hello!")

say_hello()
"""
#############lambda functions##########
#anonymous functions
#used when a small function is required for a short period of time
#syntax lambda arguments: expression condition
# add_Ten=lambda x:x+10
# print(add_Ten(5)) #15







##################OOPs####################
# class=blueprint for creating objects
# object=instance of a class 
"""
class Character:
    def __init__(self,name,health,attack,color): #constructor
        self.name=name
        self.health=health
        self.attack=attack
        self.color=color
        
    def attack_enemy(self):
        print(f'{self.name} attacks with power of {self.attack} and has health of {self.health}.whos color is {self.color}' )
    
warrior=Character("Warrior",100,50,'white') #creating an object of the class
mage=Character("Mage",80,70,'black') #creating another object of the class
archer=Character("Archer",90,60,'grey') #creating another object of the class

warrior.attack_enemy()
mage.attack_enemy() 
archer.attack_enemy()
"""

"""
1-class and object:-
A class is a blueprint or templates for creating objects,
taking an example of a car, a class would define the properties and behaviors of a car, such as its make, model, color, and methods like start, stop, and accelerate.
and an object if the actual car that is created based on the class definition, with specific values for its properties and the ability to perform the defined behaviors.


class=cars blue print
object =actual car
Syntax to create a class :-



2-Inheritance:-
3-encapsulation:-
4-abstraction:-
5-polymorphism:-
"""

#eg of class and object


"""
class car():
#methods
    def start(self):                     #Templete /Model
        print("car is starting ...")
    def stop(self):
        print("car is stopping ...")

car1=car() #creating an object and giving properties to the object
car2=car() #creating another object of the class car


car1.start()    #calling the method using the object
car1.stop()

car2.start()
car2.stop()"""


"""
class Car:
    def set_details (self,brand,color):
        self.brand=brand
        self.color=color

    def show_details(self):
        print(f'This is a {self.color} car of brand {self.brand}')

car1=Car()
car1.set_details('BMW','Black')

car2=Car()
car2.set_details('Audi','White')

car1.show_details()
car2.show_details()


"""

#constructor example:-           __init__() is a constructor which is called when an object of the class is created
"""
class Car:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color

car1=Car('BMW','Black') #values are set automatically when the object is created
car2=Car('Audi','White')
print(f'Car1 is a {car1.color} car of brand {car1.brand}')
print(f'Car2 is a {car2.color} car of brand {car2.brand}')

"""


"""
syntax to create a constructor :-
class ClassName:
    def __init__(self,parameter1,parameter2):
        self.parameter1=parameter1
        self.parameter2=parameter2

__init__( ) is a constructor which is called when an object of the class is created
self.properties are used to define the properties of the object
"""
"""
class student:
    def __init__ (self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
student1=student('Om',24,'A')
student2=student('Parag',50,'B')

print(f'Student1 name is {student1.name},age is {student1.age} and grade is {student1.grade}')
print(f'Student2 name is {student2.name},age is {student2.age} and grade is {student2.grade}')
"""


###############polymorphism##############
#same function name but different functionality
#eg:-run: a person can run fast,a car can run fast,a dog can run fast

"""
class Dog ():
    def sound(self):
        print('Dogs Bark')

class Cat():
    def sound(self):
        print('Cats Meow')

Dog1=Dog()
Cat1=Cat()

Dog1.sound()
Cat1.sound()
"""

#############Encaptulation##############
#restricting access to some of the object's components
#eg:-private variables and methods
#public variables and methods
#protected variables and methods


"""
class BankAccount:
    def __init__(self,account_number,balance):
        self.account=account_number
        self.__balance=balance #the__ makes it private variable
    def deposit(self,amount):
        self.__balance+=amount
        print(f'Amount {amount} deposited. New balance is {self.__balance}')

    def get_balance(self):
        return self.__balance #gives controled access to the private variable


account =BankAccount('12345',5000) 

account.deposit(2000)
print(account.get_balance()) #7000

print(account.__balance) #this will give error as __balance is a private variable and cannot be accessed directly


"""

############Inheritance##############
#child class inherits properties and methods of parent class    
#eg:-car is a vehicle, bike is a vehicle


"""
class Animal:   #parent class
    def speak(self):
        print("Animals make sound") 


class Dog(Animal):      #child class
    def bark(self):
        print("Dog barks")

dog =Dog()
dog .speak() #Dog barks
dog.bark()

"""

################Abstraction##############
#hiding the complex implementation and showing only the essential features
#eg:-car has many complex parts but we only need to know how to drive it



###############Error and Exception Handling##############
"""
try,except,finally,raise
try block is used to test a block of code for errors
except block is used to handle the error
finally block is used to execute a block of code regardless of the try/except result

What are errors?--mistakes in the code that prevent it from running
types of errors--syntax errors, runtime errors, logical errors
What are exceptions?--events that occur during the execution of the code that disrupt the normal flow of the program
1.start running the code
2.if an exception occurs, the rest of the code in the try block is skipped
3.catch the exception in the except block


try-except-finally
try:
    #code that may raise an exception
except ExceptionType:
    #code to handle the exception

finally:
    #code that will always execute
"""

"""
try:
    num=int(input("Enter a number: "))
    result=10/num
    print(f'Result is {result}')

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid input. Please enter a valid number")

finally:
    print("Execution completed")
"""



###################file handling##################
"""
2 primary types of files:
1.text files: store data in plain text format eg .txt, .csv, .json
2.binary files: store data in binary format eg .jpg, .png, .exe

opening a file: open("file name","mode") function is used to open a file

"""
with open("example.txt","w") #opens a file in write mode
    content="Hello, welcome to Python file handling"
    file.write(content) #writes the content to the file
    print