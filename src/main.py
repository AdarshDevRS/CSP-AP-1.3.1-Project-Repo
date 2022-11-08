#--- Imports ---#
import turtle as trtl
import random as rand

import cornerTurtle
#--- Input ---#
name = str(input("What is your name?: "))

#--- Obj ---#
quoteTurtle = trtl.Turtle() # Quotes
quoteTurtle.hideturtle()

turtle1 = trtl.Turtle() # The turtles that will be in the 4 corners.
turtle2 = trtl.Turtle()
turtle3 = trtl.Turtle()
turtle4 = trtl.Turtle()

#--- Config ---#
quoteTurtle.penup() # Write quote
quoteTurtle.write("Belive in yourself! " + name, font=("Ariel", 20, "bold"), align="center")


#--- Variables ---#


#--- Functions ---#
def clickT1(x, y):
  cornerTurtle.clickTurtle1(turtle1)
  
def clickT2(x, y):
  cornerTurtle.clickTurtle2(turtle2)
  
def clickT3(x, y):
  cornerTurtle.clickTurtle3(turtle3)
  
def clickT4(x, y):
  cornerTurtle.clickTurtle4(turtle4)

#--- Function Calls --#
cornerTurtle.initCornerTurtles(turtle1, turtle2, turtle3, turtle4) # Init corner turtle to correct locations.


#--- Events ---#
turtle1.onclick(clickT1)
turtle2.onclick(clickT2)
turtle3.onclick(clickT3)
turtle4.onclick(clickT4)

wn = trtl.Screen()
wn.mainloop()
