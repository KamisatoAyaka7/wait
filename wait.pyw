import turtle
import time as t
tr=turtle.Screen()
tr.setup(width=200,height=150)
tr.bgpic("./1.gif")

wait=10

p=turtle.Turtle()
p.pu()
p.speed(0)
p.hideturtle()
p.goto(-100,60)
p.write("wait "+str(wait)+" mins",align="left",font=("Lucida Console", 10, "normal"))
p.goto(-100,45)

for i in range(60*wait,0,-1):
    p.write(str(i//60)+":"+str(i%60),align="left",font=("Lucida Console", 10, "normal"))
    t.sleep(0.98)
    p.undo()
