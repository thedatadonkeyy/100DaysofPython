# print & input commands  👇
print("Hello World!")
print("Hello World!\nHello World!")
print("Hello" + " " + "World!")

input("What is your name?")

print("Hello " + input("what is your name?")+ " !")

#This code prints the number of characters in a user's name.
print( len( input("What is your name? ") ) )

#variables
name = input("What is your name? ")
length = len(name)
print(length)

a = input("a: ")
b = input("b: ")

#Changing variables 
c=a
a=b
b=c

num_hours ="5"
print("There are "+num_hours+ " hours until midnight")