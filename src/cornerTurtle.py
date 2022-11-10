import random as rand

colors = ["red", "purple", "green", "blue"]

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
    
