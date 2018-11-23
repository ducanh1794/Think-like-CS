"""first line."""

import turtle

"""
I. Write a program that prints We like Python's turtles! 100 times
for i in range (100):
    print("We like Python's turtles!")
"""

# II. Answer a question on runestone


# III. Write a program that uses a for loop to print each line is a mon-
# th of year
"""
choosing a list or a tuple to make repeat a fixed number of times in f-
or loop
month_tuple = ["January", "February", "March", "April", "May", "June",
 "July", "August", "September", "October", "November", "December"]

for month in month_tuple:
    print("One of the months of the year is", month)
"""


# IV. Assume you have a list of numbers 12, 10, 32, 3, 66, 17, 42, 99,
# 20
# a. Write a loop that prints each of the numbers on a new line.

"""
list_number = [12, 10, 32, 3, 66, 17, 42, 99, 20]

for number in list_number:
    print(number)

# b. Write a loop that prints each of the numbers and its square on a
new line
#for number in list_number:
    print("number in list number " + str(number) + ", its square is", \
    number ** 2)
"""


# V. Use for loops to make a turtle draw these regular polygons
# (regular means all sides the same lengths, all angles the same):


"""
window = turtle.Screen()
anton = turtle.Turtle()

anton.shape("blank")
anton.fillcolor("blue")
anton.begin_fill()

# An equilateral triangle
for i in range(3):
    anton.forward(150)
    anton.left(120)

# A square
for i in range(4):
    anton.forward(150)
    anton.left(90)

# A hexagon (six sides)
for i in range(6):
    anton.forward(150)
    anton.left(60)

# An octagon (eight sides)
for i in range(8):
    anton.forward(-100)
    anton.right(180 - 135)

anton.end_fill()
window.exitonclick()
"""


# VI. Write a program that asks the user for the number of sides, the
# length of the side, the color, and the fill color of a regular
# polygon. The program should draw the polygon and then fill it in

"""
numb_of_sides = int(input("Enter number of sides you want: "))
len_of_side = int(input("Enter the length of the side you want: "))
col = input("Enter your color: ")
fill_col = input("Enter your fill color: ")
window = turtle.Screen()
anton = turtle.Turtle()
anton.color(col)
anton.fillcolor(fill_col)
anton.shape("blank")
anton.begin_fill()

for i in range(numb_of_sides):
    anton.forward(len_of_side)
    anton.right(360 / numb_of_sides)

anton.end_fill()
"""


# VII. Make a program with a list of data that depict random turn each
# 100 steps forward (Positive angle are counter-clockwise)

"""
window = turtle.Screen()
pirate = turtle.Turtle()
rand_turn = [160, -43, 270, -97, -43, 200, -940, 17, -86]

for move in rand_turn:
    pirate.left(move)
    pirate.forward(100)

print(pirate.heading())

window.exitonclick()
"""


# IX. Write a program to draw a star with 5 peaks:

"""
window = turtle.Screen()
anton = turtle.Turtle()
anton.shape("blank")
anton.pensize(3)

for i in range(5):
    anton.forward(150)
    anton.right(180 - 36)

window.exitonclick()
"""


# X. Write a program to draw a face of a clock which use turtle shape
# to indicate each number

"""
window = turtle.Screen()
clock = turtle.Turtle()
window.bgcolor("lightgreen")
clock.shape("turtle")
clock.color("blue")
clock.pensize(2)
clock.up()

for i in range(12):
    clock.forward(70)
    clock.down()
    clock.forward(10)
    clock.penup()
    clock.forward(20)
    clock.stamp()
    clock.backward(100)
    clock.right(30)

window.exitonclick()
"""


# XI. Write a program to draw some kind of picture
# Create a snow flower with turtle module

"""
window = turtle.Screen()
snow = turtle.Turtle()
snow.speed(0)
window.bgcolor("mediumslateblue")
snow.fillcolor("deepskyblue")
snow.color("deepskyblue")
snow.pensize(3)
snow.begin_fill()

for i in range(6):
    for i in [21, 15, 10, 5]:
        snow.forward(8)
        snow.left(60)
        snow.forward(i)
        if i == 21:
            snow.forward(3)
            snow.right(30)
            snow.forward(5)
            snow.stamp()
            snow.forward(-5)
            snow.left(30)
            snow.forward(-3)
        snow.forward(-i)
        snow.right(120)
        snow.forward(i)
        snow.forward(-i)
        snow.left(60)
    snow.forward(10)
    snow.stamp()
    snow.forward(-42)
    snow.right(60)
    snow.forward(15)
    snow.right(120)
    snow.forward(15)
    snow.left(120)


# too long
    snow.forward(8)
    snow.left(60)
    snow.forward(21)
    snow.forward(-21)
    snow.right(120)
    snow.forward(21)
    snow.forward(-21)
    snow.left(60)
    snow.forward(8)
    snow.left(60)
    snow.forward(15)
    snow.forward(-15)
    snow.right(120)
    snow.forward(15)
    snow.forward(-15)
    snow.left(60)
    snow.forward(8)
    snow.left(60)
    snow.forward(10)
    snow.forward(-10)
    snow.right(120)
    snow.forward(10)
    snow.forward(-10)
    snow.left(60)
    snow.forward(8)
    snow.left(60)
    snow.forward(5)
    snow.forward(-5)
    snow.right(120)
    snow.forward(5)
    snow.forward(-5)
    snow.left(60)
    snow.forward(10)
    snow.stamp()
    snow.forward(-42)


snow.end_fill()
window.exitonclick()
"""


# XII. Assign a turtle to a variable and print its type

"""
window = turtle.Screen()
anton = turtle.Turtle()
print(type(anton))
"""

# XIII. Create a spider with n legs coming out from a center point. The
# each leg is 360 / n degrees

legs = int(input("Enter your spider legs: "))

window = turtle.Screen()
spider = turtle.Turtle()
spider.pensize(2)

for i in range(legs):
    spider.forward(30)
    spider.forward(-30)
    spider.right(360 / legs)

window.exitonclick()
