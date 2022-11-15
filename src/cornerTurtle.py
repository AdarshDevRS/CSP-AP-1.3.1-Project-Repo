#// Canvas size may be different depending on your device or IDE! Change the numbers as needed.

import random as rand

colors = ["red", "purple", "green", "blue"] 

def initCornerTurtles(t1, t2, t3, t4):
  t1.goto(-190, 190)
  t2.goto(190,190)
  t3.goto(-190, -190)
  t4.goto(190, -190)
  
  t1.shape("circle")
  t2.shape("triangle")
  t3.shape("square")
  t4.shape("arrow")
  
def clickTurtle1(t):
    randColor = rand.randint(0, 3)
    t.color(colors[randColor])
  
def clickTurtle2(t):
    randColor = rand.randint(0, 3)
    t.color(colors[randColor])

def clickTurtle3(t):
    randColor = rand.randint(0, 3)
    t.color(colors[randColor])

def clickTurtle4(t):
    randColor = rand.randint(0, 3)
    t.color(colors[randColor])
    
