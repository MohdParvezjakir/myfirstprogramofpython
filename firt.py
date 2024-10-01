#this is my first program
print("hello world")
''' comment makes code more readable and comprehensible 
for other
thi is a example of multiline comment 
'''
#module is a file that contains code written by someone else we can use this in our code 
#therer are to types of modules 
#1st is built in module 
#and the nd i exeternel module
a = 2.0
b = 3.5
type(b)
print(type(b))
int(a)
print((a))
print(type(a))
b = "pythonproject"
#string slicing
print(b[0:5])
import pyjokes

import pyjokes
joke = pyjokes.get_joke(language='en', category='all')
print(f"here i a joke for you: {joke}")
import pyttsx3
engine = pyttsx3.init()
engine.say("hi what is your name")
engine.runAndWait()
name = (input("Enter your name:"))
engine.say(f"hello mr. {name} how can i help youy")
engine.runAndWait()
engine.say(f"here is a joke for you {joke} you like this")
engine.runAndWait()

