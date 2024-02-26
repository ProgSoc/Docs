from turtle import *

mode('logo')
speed(0)
pensize(8)

penup()
goto(80, 68)
right(180)
pendown()

forward(64)
circle(16,90)
left(180)
circle(16,90)
forward(16)
circle(-16,90)

penup()
forward(32)
forward(48)
forward(16)
forward(32)
pendown()

# p

circle(-16,90)
forward(16)
circle(16,90)
left(180)
circle(16,90)
forward(40)
circle(-24,180)

# r

forward(24)
penup()
right(180)
forward(24)
pendown()
circle(-24,90)
penup()
forward(16)
pendown()

# o

circle(-24,90)

# p

circle(24)

# o

circle(-24,270)
penup()
right(180)
forward(16)

# r

circle(24,90)
forward(24)
left(180)
forward(24)
pendown()
forward(24)
penup()
right(180)
forward(24)
pendown()

# p

circle(-24,180)
forward(24)
penup()

# s

goto(-42,-10)
pendown()
circle(10,30)
circle(10,240)
circle(-10,270)

# o

penup()
goto(-12,0)
right(90)
pendown()
circle(-20,360)

# c

penup()
goto(42,-12)
seth(0)
pendown()
circle(12,180)
forward(16)
circle(12,180)

# ;

penup()
goto(60,-12)
dot()
goto(60,-32)
dot()
seth(0)
left(135)
pendown()
forward(16)

hideturtle()
mainloop()
