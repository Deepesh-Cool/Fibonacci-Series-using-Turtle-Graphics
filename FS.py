import turtle
import time
import random
print("Enter the Blank")
n=input("The first _______  Fibonacci numbers\n")
wn = turtle.Screen()
wn.bgcolor("Black")
time.sleep(2)
point = turtle.Turtle()
point.color("Blue")
point.shape("circle")
point1 = turtle.Turtle()
point3 = turtle.Turtle()
point4 = turtle.Turtle()
point2 = turtle.Turtle()
point3.shape("square")
point2.setpos(250,-50)
point2.color("Yellow")
point2.speed(1)
point4.up()
point4.speed(0)
point4.setpos(-15,-50)
point4.down()
point4.color("red")
point.speed(0)
point1.speed(0)
point1.up()
point1.setpos(0,-100)
point1.down()
point1.begin_fill()
point1.fillcolor("Cyan")
point1.circle(250)
point1.end_fill()
point3.color("Yellow")
point3.up()
point3.setpos(-300,-200)
point3.write("FIBONACCI NUMBERS",font =("Times New Roman",50,"bold","underline"))
point.up()
point.setpos(-15,120)
point.down()
a = 0
b = 1
c = 0
if int(n)==0:
	point.write("0",font =( "Times New Roman",50,"normal"))
	point4.write("F0",font = ("TImes New Roman",25,"italic"))
for i in range(0,int(n)):
	point.penup()
	point.clear()
	point4.clear()
	point2.clear()
	point.color("Blue")
	l = len(str(c))
	if i == 2:
		point.color("Brown")
	if len(str(c))>=7 and len(str(c))<12:
		point.setpos(-15-(50*len(str(i))),120)
		point.write(c,font =( "Times New Roman",450//len(str(c)),"normal"))
	elif len(str(c))>=12:
		point.setpos(-15-(90*len(str(i))),120)
		point.write(c,font =( "Times New Roman",650//len(str(c)),"normal"))
	else:
		point.write(c,font =( "Times New Roman",65,"normal"))
	print(c)
	point2.write("No. of digit : "+str(l),font = ("Times New Roman",20,"normal"))
	point4.write("F"+str(i),font = ("TImes New Roman",25,"italic"))
	a = b
	b = c
	c = a+b
	time.sleep(0.1)
wn.exitonclick()
