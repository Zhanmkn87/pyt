import turtle


turtle.bgcolor("grey")
t = turtle.Pen()

for x in range (4):
    for y in range (6):
        t.forward(50)
        t.right(90)
        t.forward(5)
        t.backward(10)
        t.forward(5)
        t.left(90)
    t.backward(300)
    t.right(90)
    
t.pencolor("blue")

t.penup()
t.setpos(4,1)
t.pendown()
t.write("0", font=("Arial", 16, "bold"))

t.penup()
t.setpos(4,300)
t.pendown()
t.write("Y", font=("Arial", 16, "bold"))

t.penup()
t.setpos(4,-300)
t.pendown()
t.write("-Y", font=("Arial", 16, "bold"))

t.penup()
t.setpos(-300,1)
t.pendown()
t.write("-X", font=("Arial", 16, "bold"))

t.penup()
t.setpos(300,1)
t.pendown()
t.write("X", font=("Arial", 16, "bold"))

t.penup()
t.setpos(42, -20)
b = 50
t.pendown()
for d in range (6):
    t.write(b)
    t.penup()
    t.forward(50)
    t.pendown()
    b = b + 50
    
t.penup()
t.setpos(-60,-20)
t.pendown()
b = -50 
for c in range (6):
    t.write(b)
    t.penup()
    t.backward(50)
    t.pendown()
    b = b - 50
    
t.penup()
t.setpos(-25,42)
t.right(90)
t.pendown()
b = 50
for z in range(6):
    t.write(b)
    t.penup()
    t.backward(50)
    t.pendown()
    b = b + 50
    
t.penup()
t.setpos(-28, -58)
t.pendown()
b = -50
for r in range(6):
    t.write(b)
    t.penup()
    t.forward(50)
    t.pendown()
    b = b - 50
    
t.left(90)

def circle(x,y):
    
    t.hideturtle()  
   
    size = 5
    t.penup()
    t.setpos(x,y)
    t.pendown()
    t.dot(size, "red")
    
    t.penup()
    t.pencolor("black")
    t.backward(40)
    t.pendown()
    t.write(x)
    t.penup()
    t.forward(50)
    t.pendown()
    t.write(y)
    
turtle.onscreenclick(circle)

