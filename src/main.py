#--- Imports ---#
import turtle as trtl
import random as rand

import cornerTurtle
import background

#--- Input ---#
name = str(input("What is your name?: "))

#--- Obj ---#
backgroundTurtle = trtl.Turtle() # Background
nameTurtle = trtl.Turtle() # Shows name.

quoteTurtle = trtl.Turtle() # Quotes
quoteTurtle.hideturtle()

turtle1 = trtl.Turtle() # The turtles that will be in the 4 corners.
turtle2 = trtl.Turtle()
turtle3 = trtl.Turtle()
turtle4 = trtl.Turtle()

#--- Variables ---#
quotes = [
  "Don't give up!", 
  "Believe in yourself!", 
  "Stay positive!", 
  "Push past failure!",
  "Be confident!",
  "Today is tomorrow's yesterday!",
  "Don't be in the past or future, be in the present!",
]

#--- Functions ---#

def writeName():
  nameTurtle.penup()
  nameTurtle.goto(0, 150)
  nameTurtle.write("Welcome, " + name, font=(("Ariel"), 20, "bold"), align="center")
  nameTurtle.hideturtle()
  

def writeQuote():
  quoteTurtle.clear()
  randQuote = rand.randint(0, 6)
  quoteTurtle.color("blue")
  quoteTurtle.write(quotes[randQuote], font=(("Ariel"), 20, "bold"), align="center")
  
def clickT1(x, y):
  cornerTurtle.clickTurtle1(turtle1)
  writeQuote()
  
def clickT2(x, y):
  cornerTurtle.clickTurtle2(turtle2)
  writeQuote()
  
def clickT3(x, y):
  cornerTurtle.clickTurtle3(turtle3)
  writeQuote()
  
def clickT4(x, y):
  cornerTurtle.clickTurtle4(turtle4)
  writeQuote()

#--- Function Calls --#
background.initBackground(backgroundTurtle, "red") # Init background
writeName() # Writing user name.
cornerTurtle.initCornerTurtles(turtle1, turtle2, turtle3, turtle4) # Init corner turtle to correct locations.
writeQuote() # Writing random quote on start

#--- Events ---#
turtle1.onclick(clickT1)
turtle2.onclick(clickT2)
turtle3.onclick(clickT3)
turtle4.onclick(clickT4)

wn = trtl.Screen()
wn.mainloop()
