import turtle
import random
screen = turtle.Screen()
screen.screensize(canvwidth=500, canvheight=500)
screen.bgcolor('black')

t=turtle.Turtle()
t.penup()
t.goto(0,200)
t.pendown()
t.pencolor("white")
t.write("Background Color: ",font=("arial",30,"normal"),align="center")
t.penup()

t.goto(-100,100)
t.pendown()
t.pencolor("tan")
t.write("1. Tan",font=("arial",20,"normal"),align="left")
t.penup()

t.goto(-100,50)
t.pendown()
t.pencolor("Azure")
t.write("2. Azure",font=("arial",20,"normal"),align="left")
t.penup()

t.goto(-100,0)
t.pendown()
t.pencolor("Aquamarine")
t.write("3. Aquamarine",font=("arial",20,"normal"),align="left")
t.penup()

t.goto(-100,-50)
t.pendown()
t.pencolor("DarkKhaki")
t.write("4. DarkKhaki",font=("arial",20,"normal"),align="left")
t.penup()

t.goto(0,-150)
t.pendown()
t.pencolor("white")
t.write("Select a Color",font=("arial",30,"normal"),align="center")

choose = int(input("Select a color: "))
if choose == 1:
    screen.bgcolor('Tan')
elif choose == 2:
    screen.bgcolor('Azure')
elif choose == 3:
    screen.bgcolor('aquamarine')
else:
    screen.bgcolor('DarkKhaki')

t.clear()

t.goto(0,0)
t.pendown()
t.pencolor("black")
t.write("Enter your name: ",font=("arial",30,"normal"),align="center")


name = input("Enter your name: ")
# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter another number: "))

operation = random.randint(1,4)
if operation == 1:
    symbol = "+"
    num1 = random.randint(-100,100)
    num2 = random.randint(-100,100)
    solution=num1+num2
elif operation == 2:
        symbol = "-"
        num1 = random.randint(-100, 100)
        num2 = random.randint(-100, 100)
        solution = num1 - num2
elif operation == 3:
        symbol = "x"
        num1 = random.randint(-10, 10)
        num2 = random.randint(-10, 10)
        sign = random.randint(1,2)
        if sign == 2:
            num2 = -1 * num2
        solution = num1 * num2
elif operation == 4:
        symbol= "/"
        num1 = random.randint(-10, 10)
        num2 = random.randint(1, 10)
        solution = num1 / num2
t.clear()
t.penup()
t.goto(0,100)
t.pendown()
# name=input("What's your name? ")
t.write(name,font=("arial",30,"normal"),align="center")


t.penup()
t.goto(-200,0)
t.pendown()
t.pencolor("blue")
# num1=int(input("Write a Number: "))
t.write(num1,font=("arial",30,"normal"),align="center")
#
#
t.penup()
t.goto(0,0)
t.pendown()
t.pencolor("green")
# num2=int(input("Write another Number: "))
t.write(num2,font=("arial",30,"normal"),align="center")
#
#
t.penup()
t.goto(-100,0)
t.pendown()
t.pencolor("hot pink")
t.write(symbol,font=("arial",30,"normal"),align="center")


t.penup()
t.goto(100,0)
t.pendown()
t.pencolor("black")
t.write("=",font=("arial",30,"normal"),align="center")

ans = int(input("Enter the answer: "))

t.penup()
t.goto(200,0)
t.pendown()
t.pencolor("red")
t.write(sum,font=("arial",30,"normal"),align="center")

t.penup()
t.goto(0,-100)
t.pendown()
t.pencolor("black")
t.write("Your answer: " + str(ans),font=("arial",30,"normal"),align="center")
if ans == sum:
    screen.bgcolor("Dodger Blue")
    t.penup()
    t.goto(0, 50)
    t.pendown()
    t.pencolor("black")
    t.write("Correct!", font=("arial", 30, "normal"), align="center")
else:
    screen.bgcolor("DARKORANGE")
    t.penup()
    t.goto(0, -200)
    t.pendown()
    t.pencolor("Red")
    t.write("Incorrect!", font=("arial", 30, "normal"), align="center")
# t.penup()
#
# t.goto(-80,15)

# t.pendown()
# t.pencolor("blue")
# t.setheading()
# t.circle(35)
# t.penup()
#
# t.goto(0,15)
# t.pencolor("Black")
# t.pendown()
# t.setheading()
# t.circle(35)
# t.penup()
#
# t.goto(80,15)
# t.pencolor("Red")
# t.pendown()
# t.setheading()
# t.circle(35)
# t.penup()
#
# t.goto(-80,15)
# t.pencolor("Yellow")
# t.pendown()
# t.setheading()
# t.circle(35)
# turtle.done()
# t.penup()
#
# t.goto(-40,0)
# t.pencolor("Green")
# t.pendown()
# t.setheading()
# t.circle(35)
# t.penup()
#
# t.goto(40,0)
# t.pendown()
# t.setheading()
# t.circle(35)
turtle.done()