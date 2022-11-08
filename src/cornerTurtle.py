import random as rand

colors = ["red", "purple", "green", "blue"]
def initCornerTurtles(t1, t2, t3, t4):
  turtles = [t1, t2, t3, t4]
  
  for t in turtles:
    t.penup()
    t.shape("circle")
    
  t1.goto()
  t2.goto()
  t3.goto()
  t4.goto()
  
def clickTurtle1(t):
    randNum = rand.randint(0, 3)
    t.color(colors[randNum])
  
def clickTurtle2(t):
    randNum = rand.randint(0, 3)
    t.color(colors[randNum])

def clickTurtle3(t):
    randNum = rand.randint(0, 3)
    t.color(colors[randNum])

def clickTurtle4(t):
    randNum = rand.randint(0, 3)
    t.color(colors[randNum])
    
