"""Exercises."""
# 1. Use the drawsquare function to draw 5 squares, each side is
# 20 units.
import turtle
# import math
# import unittest

'''
def drawsquare(t, sz):
    """Turtle t draw a square with sz units per size."""
    for i in range(4):
        t.forward(sz)
        t.left(90)
    t.up()
    t.forward(sz * 2)
    t.down()


def main():
    """Main."""
    window = turtle.Screen()
    window.bgcolor("lightgreen")
    anton = turtle.Turtle()
    anton.pensize(3)
    anton.color("hotpink")
    for i in range(5):
        drawsquare(anton, 20)
    window.exitonclick()

main()
'''


# 2. Draw 5 squares with square in square. The innermost square is 20
# each side. The next one is 20 units bigger than the one inside it.
'''
def drawsquare(t, sz):
    """Turtle t draw a square with sz units per size."""
    for i in range(4):
        t.pendown()
        t.forward(sz)
        t.left(90)
        t.penup()


def main():
    """Main."""
    window = turtle.Screen()
    window.bgcolor("lightgreen")
    anton = turtle.Turtle()
    anton.color("hotpink")
    anton.pensize(3)
    len_side = 0
    coordinate = 0
    for i in range(5):
        len_side += 20
        drawsquare(anton, len_side)
        coordinate -= 10
        anton.goto(coordinate, coordinate)
    window.exitonclick()

main()
'''


# 3. Write a non-fruitful function drawpoly(t, side, sz) which makes
# a turtle draw a regular polygon.
def drawpoly(t, side, sz):
    """Draw a regular polygon."""
    for i in range(side):
        t.forward(sz)
        t.left(360 / side)

'''
def main():
    """Main."""
    window = turtle.Screen()
    window.bgcolor("lightgreen")
    anton = turtle.Turtle()
    anton.color("hotpink")
    anton.pensize(3)
    drawpoly(anton, 8, 50)
    window.exitonclick()

main()
'''


# 4. Draw a pattern with Pretty pattern title window.
'''
def drawsquare(t, sz):
    """Turtle t draw 1 square."""
    for i in range(4):
        t.forward(sz)
        t.left(90)


def main():
    """Main."""
    window = turtle.Screen()
    window.bgcolor("lightgreen")
    window.title("Pretty pattern")
    anton = turtle.Turtle()
    anton.color("blue")
    anton.shape("blank")
    anton.pensize(4)
    for i in range(20):
        drawsquare(anton, 150)
        anton.right(18)
    window.exitonclick()

main()
'''


# 5. Draw 2 spiral patterns.
'''
def drawspiral1(t):
    """The first spiral."""
    sz = 0
    t.left(180)
    for i in range(51):
        sz += 5
        t.forward(sz)
        t.right(90)
        t.forward(sz)
        t.right(90)


def drawspiral2(t):
    """The second spiral."""
    sz = 0
    angle = 90
    t.left(180)
    for i in range(51):
        sz += 5
        t.forward(sz)
        t.right(angle)
        t.forward(sz)
        t.right(angle)
        angle -= 0.03


def main():
    """Main."""
    window = turtle.Screen()
    window.bgcolor("lightgreen")
    anton = turtle.Turtle()
    anton.color("blue")
    anton.pensize(2)
    anton.speed(0)
    drawspiral2(anton)
    window.exitonclick()
main()
'''


# 6. Non-fruitful function drawequitriangle(t, sz), which calls
# drawpoly to have a equilateral triangle.
'''
def drawequitriangle(t, sz):
    """Equitriangle."""
    side = 3
    drawpoly(t, side, sz)


def main():
    """Main."""
    window = turtle.Screen()
    window.bgcolor()
    anton = turtle.Turtle()
    anton.pensize(2)
    drawequitriangle(anton, 80)
    window.exitonclick()

main()
'''


# 7. Fruitful function sumto(n), return the sum of all integer numbers
# up to and including n. Use (n * (n + 1)) / 2
'''
def sumto(n):
    """The sum of all integer numbers."""
    result = n * (n + 1) / 2
    return result

print(sumto(11))
'''


# 8. Function areaofcircle(r) which returns the area of a circle
# of radius r. Use the math library.
'''
def areaofcircle(r):
    """Area of a circle."""
    area = math.pi * r ** 2
    return area

t = areaofcircle(8)
print(t)
'''


# 9. A non-fruitful function draw a five pointed star.
# Length of each side: 100
'''
def drawstar():
    """Draw 5 pointed star."""
    for i in range(5):
        anton.forward(100)
        anton.right(144)


window = turtle.Screen()
anton = turtle.Turtle()
anton.shape("blank")
anton.pensize(3)
drawstar()
window.exitonclick()
'''


# 10. Extend #9 program above.
'''
def drawfivestar():
    """Draw five star."""
    for i in range(5):
        for i in range(5):
            anton.forward(100)
            anton.right(144)
        anton.up()
        anton.forward(350)
        anton.down()
        anton.right(144)

window = turtle.Screen()
window.bgcolor("lightgreen")
anton = turtle.Turtle()
anton.color("hotpink")
anton.pensize(3)
anton.up()
anton.goto(-170, 50)
anton.down()
drawfivestar()
window.exitonclick()
'''


# 11. Create the star function, which draw an n pointed star.
# n is odd number greater or equal to 3
'''
n = int(input("Enter your pointed star: "))


def oddpointedstar():
    """Odd pointed star."""
    for i in range(n):
        anton.forward(100)
        anton.right(180 - (180 / n))

window = turtle.Screen()
anton = turtle.Turtle()
window.bgcolor("lightgreen")
anton.color("hotpink")
oddpointedstar()
'''


# 12. Create a sprite which has 15 legs of length 120.
# The function has parameters for the turtle, number of legs
# and length of legs.
'''
def drawsprite(t, legs, len):
    """Draw turtle t with n legs and m length of legs."""
    for i in range(legs):
        t.forward(len)
        t.forward(-len)
        t.right(360 / legs)


def main():
    """Main."""
    window = turtle.Screen()
    window.bgcolor("lightgreen")
    anton = turtle.Turtle()
    anton.color("hotpink")
    anton.shape("turtle")
    drawsprite(anton, 15, 120)
    window.exitonclick()

main()
'''


# 13. Write function sumto(n), which use the accumulator pattern.
'''
def sumto(n):
    """Return the sum of all integer numbers up to and including n."""
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


class TestSum(unittest.TestCase):
    """Class Test Sum."""

    def testsum(self):
        """Test the sum of all integer numbers up to and including n."""
        self.assertEqual(sumto(10), 55)

if __name__ == "__main__":
    unittest.main()
'''


# 14. Create a function called mysqrl which use Newton's algorithm
# to find the square root of a number.
'''
def mysqrt(n):
    """Square root of number n."""
    newguess = n / 2
    for i in range(20):
        newguess = (1 / 2) * (newguess + (n / newguess))
    return newguess

print(mysqrt(6))
'''


# 15. Write a function called mypi which return a PI (3.14159..)
# Use the Leibniz formula
'''
def mypi(k):
    """Leibniz formula for pi."""
    pi = 0
    sign = 1
    denominator = 1
    for i in range(k):
        pi = pi + (sign / denominator)
        sign *= -1
        denominator += 2
    return pi * 4

print(mypi(100000))
'''


# 16. Write a function called mypi that will return a pi.
# Use the Madhava approximation.
'''
def mypi_1(k):
    """Find pi number by using the Madhava approach."""
    pi = 0
    sign = 1
    denominator = 1
    for i in range(k):
        pi += (sign / (denominator * 3 ** i))
        sign *= -1
        denominator += 2
    return pi * 12 ** (1 / 2)

print(mypi_1(9))
'''


# 17. Write a function called fancysquare that will draw a square
# with fancy corners
'''
def drawsprite(t, legs, len1):
    """Sprite."""
    for i in range(legs):
        t.forward(len1)
        t.forward(-len1)
        t.right(360 / legs)


def fancysquare(t, len, legs, len1):
    """Function fancySquare."""
    for i in range(4):
        t.forward(len)
        drawsprite(t, legs, len1)
        t.left(90)

window = turtle.Screen()
anton = turtle.Turtle()
fancysquare(anton, 100, 8, 15)
anton.up()
anton.goto(-100, 0)
window.exitonclick()
'''


# 18. Use the program in A turtle bar chart and modify it.
# Make the label appear completely above the top line,
# instead the top of the bar through the bottom of the label.
xs = [48, 117, 200, 240, 160, 260, 220]  # here is the data
maxheight = max(xs)
numbars = len(xs)
border = 10


def drawbar(t, height, maxheight):
    """Draw bar chart."""
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.up()
    t.forward(maxheight - height)
    t.write(" " * 10 + str(height))
    t.forward(-(maxheight - height))
    t.down()
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()


def main():
    """Main."""
    window = turtle.Screen()
    anton = turtle.Turtle()
    window.bgcolor("lightgreen")
    window.setworldcoordinates(0 - border, 0 - border, numbars * 40 + border,
                               maxheight + border)
    anton.color("blue")
    anton.pensize(3)
    anton.speed(0)
    anton.fillcolor("red")
    for i in xs:
        drawbar(anton, i, maxheight)
    window.exitonclick()

main()
