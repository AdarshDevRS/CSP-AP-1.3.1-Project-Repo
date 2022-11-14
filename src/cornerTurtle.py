#// Make sure to set the "rand.randint" to corresponding list range.
import random as rand

colors = ["purple", "green", "blue"] 
## REMOVING RED FOR NOW SINCE BACKGROUND IS COLOR RED.

def initCornerTurtles(t1, t2, t3, t4):
  turtles = [t1, t2, t3, t4]
  
  for t in turtles:
    t.penup()
    t.shape("circle")
    
  t1.goto(-190, 190)
  t2.goto(190,190)
  t3.goto(-190, -190)
  t4.goto(190, -190)
  
def clickTurtle1(t):
    randColor = rand.randint(0, 2)
    t.color(colors[randColor])
  
def clickTurtle2(t):
    randColor = rand.randint(0, 2)
    t.color(colors[randColor])

def clickTurtle3(t):
    randColor = rand.randint(0, 2)
    t.color(colors[randColor])

def clickTurtle4(t):
    randColor = rand.randint(0, 2)
    t.color(colors[randColor])
    
