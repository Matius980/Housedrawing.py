import turtle as trtl

painter = trtl.Turtle()
painter.screen.bgcolor("#4a8bad")
painter.speed(5)

painter.color("#a14242")
painter.begin_fill()


for i in range(4):
    painter.forward(200)
    painter.right(90)
painter.end_fill()


painter.penup()
painter.goto(0,0)
painter.pendown()
painter.color("#d7b4ae")
painter.begin_fill()

for f in range(4):
    painter.forward(200)
    painter.right(-120)
painter.end_fill()


painter.penup()
painter.goto(175,-200)
painter.pendown()
painter.color("#484030")
painter.begin_fill()
painter.setheading(90)
width = 50
height = 100
 
for f in range(2):
    painter.forward(height) 
    painter.left(90)        
    painter.forward(width)  
    painter.left(90)       
painter.end_fill()


painter.penup()
painter.goto(59,-124)
painter.pendown()
painter.color("black")
painter.begin_fill()

for n in range(4):
    painter.forward(25)
    painter.left(90)
painter.end_fill()


painter.penup()
painter.goto(-250,258)
painter.pendown()
painter.color("yellow")
painter.begin_fill()

radius = 75

painter.circle(radius)
painter.end_fill()

painter.pendown()
painter.goto(-326,258)
painter.penup()
painter.color("yellow")

for g in range(12):
    painter.forward(100)
    painter.backward(60)
    painter.right(30)


import turtle

# Create a turtle object
t = turtle.Turtle()

# Function to get coordinates on click
def get_coordinates(x, y):
    print(f"You clicked at ({x}, {y})")

# Capture click events to get coordinates
turtle.onscreenclick(get_coordinates)

# Keep the window open
turtle.mainloop()

wn = trtl.Screen()
wn.mainloop()
