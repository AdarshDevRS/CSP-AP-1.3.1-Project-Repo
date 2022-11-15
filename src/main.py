#// Canvas size may be different depending on your device or IDE! Change the numbers as needed.

#// BACKGROUND IMAGE GOTTEN FROM PREVIOUS CSP AP PRINCIPLES ASSIGNMENT ("APPLE AVALANCHE").

#--- Imports ---#
import turtle as trtl
import random as rand

import cornerTurtle

#--- Input ---#
name = str(input("What is your name?: ")) # Showing input first then loading everything in.

#--- Setup ---#
wn = trtl.Screen()
wn.bgpic("CSP-AP-1.3.1-Project-Repo/background.gif")

#--- Obj ---#
nameTurtle = trtl.Turtle() # Shows name.
nameTurtle.hideturtle()

quoteTurtle = trtl.Turtle() # Quotes
quoteTurtle.hideturtle()

underLineTurtle = trtl.Turtle() # Under line below the quote
underLineTurtle.hideturtle()

indicatorTurtle = trtl.Turtle() # Indicates to click on the corner shapes.
indicatorTurtle.hideturtle()

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
  nameTurtle.write("Welcome, " + name, font=(("Ariel"), 25, "bold"), align="center")
  nameTurtle.hideturtle()
  

def writeQuote():
  quoteTurtle.clear()
  randQuote = rand.randint(0, 6)
  quoteTurtle.write(quotes[randQuote], font=(("Ariel"), 17, "bold"), align="center")
  
def writeUnderline():
  x = -120
  y = -30
  forwardAmount = 250
  underLineTurtle.pensize(3)
  underLineTurtle.pencolor("blue")
  for i in range(3):
    underLineTurtle.penup()
    if i == 1:
      underLineTurtle.pencolor("red")
    elif i == 2:
      underLineTurtle.pencolor("green")
    underLineTurtle.goto(x, y)
    underLineTurtle.pendown()
    underLineTurtle.forward(forwardAmount)
    y -= 30
    x += 45
    forwardAmount /= 2

def writeIndicate():
  indicatorTurtle.penup()
  indicatorTurtle.goto(0, 120)
  indicatorTurtle.write("(Click on the any one of the turtles on the corner!)", font=(("Ariel"), 15, "bold"), align="center")

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
writeName() # Writing user name.
writeIndicate() # Indicating the user to click on the corner turtles.
writeUnderline() # Underlines under the quote to make it look nicer.
cornerTurtle.initCornerTurtles(turtle1, turtle2, turtle3, turtle4) # Init corner turtle to correct locations.
writeQuote() # Writing random quote on start

#--- Events ---#
turtle1.onclick(clickT1)
turtle2.onclick(clickT2)
turtle3.onclick(clickT3)
turtle4.onclick(clickT4)

wn.mainloop()
