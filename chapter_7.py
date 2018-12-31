"""Exercises."""
# 3. Write a function which is given an exam mark and returns its grade
# >= 90: A, [80-90): B, [70-80): C, [60-70): D, < 60: F
# import unittest
# import math
# import turtle

'''
def gradeformark(mark):
    """Define gradeformark function which returns students' grade."""
    """from exam grade."""
    if mark >= 90:
        return "A"
    elif 80 <= mark < 90:
        return "B"
    elif 70 <= mark < 80:
        return "C"
    elif 60 <= mark < 70:
        return "D"
    else:
        return "F"


class TestGetGrade(unittest.TestCase):
    """Class Test."""

    def testgetgrade(self):
        """Test."""
        self.assertEqual(gradeformark(79.9999), "C")

if __name__ == "__main__":
    unittest.main()
'''


# 4. Modify the turtle bar chart program. Any value greater or equal
# to 200 is filled with red, [100, 200): yellow, < 100: green.
# 5. One of data value in the list is a negative
# Put negative text on the 0 axis.
'''
def barchart(t, xs):
    """Draw bar chart."""
    t.pensize(3)
    if xs < 0:
        t.write(" " + str(xs))
    t.left(90)
    t.forward(xs)
    t.right(90)
    if xs >= 0:
        t.write(" " + str(xs))
    t.forward(40)
    t.right(90)
    t.forward(xs)
    t.left(90)


def main():
    """Main."""
    border = 10
    xs = [48, 117, 200, 240, 160, 260, 220, -160, -200, -550]
    maxheight = max(xs)
    minheight = min(xs)
    lenxs = len(xs)
    window = turtle.Screen()
    anton = turtle.Turtle()
    window.bgcolor("lightgreen")
    window.setworldcoordinates(0 - border, minheight - border,
                               40 * lenxs + border, maxheight + border)
    anton.color("blue")
    for i in xs:
        if i >= 200:
            anton.fillcolor("red")
        elif 100 <= i < 200:
            anton.fillcolor("yellow")
        else:
            anton.fillcolor("green")
        anton.begin_fill()
        barchart(anton, i)
        anton.end_fill()
    window.exitonclick()

main()
'''

# 6. Write a fruitful function which is given the length of two
# sides of a right-angled triangle and return the length of
# the hypotenuse (Return square of root: x ** 0,5 or use math library)

'''
def findhypot(a, b):
    """Find the length of the hypotenuse."""
    result = math.sqrt(a ** 2 + b ** 2)
    return result


class TestFindHypot(unittest.TestCase):
    """Class Test."""

    def testfindhypot(self):
        """Test."""
        self.assertEqual(findhypot(1, 1.73205), 1.99999930062)

if __name__ == "__main__":
    unittest.main()
'''


# 7. Write a function that takes an integer as an argument and return
# True when it's an even number, False when it's an odd.

'''
def is_even(a):
    """Function is_even."""
    return a % 2 == 0


class TestIsEven(unittest.TestCase):
    """Class Tess."""

    def testeven(self):
        """Test."""
        self.assertEqual(is_even(11), False)

if __name__ == "__main__":
    unittest.main()
'''


# 8. Write a function that takes an integer as an argument and return
# True when it's odd and False when it's even.
'''
def is_odd(a):
    """Function called is_odd."""
    return a % 2 != 0

print(is_odd(11))
'''


# 9. Modify is_odd so that it uses a call to is_even to determine its
# argument is an odd integer.
'''
def is_even(a):
    """Function called is_even."""
    return a % 2 == 0


def is_odd(a):
    """Function called is_odd."""
    if is_even(a):
        return False
    else:
        return True

print(is_odd(193))
'''


# 10. Function is_rightangled, given the length of three sides of
# a triangle, determine whether the triangle is right-angled.
# The third argument is the longest side.
'''
def is_rightangled(a, b, c):
    """Function called is_rightangled."""
    result = math.sqrt(a ** 2 + b ** 2)
    if abs(result - c) < 0.0001:
        return True
    else:
        return False


class TestRightAngled(unittest.TestCase):
    """Class Test."""

    def test_0(self):
        """Test."""
        self.assertEqual(is_rightangled(0.5, 0.4, 0.64031), True)


if __name__ == "__main__":
    unittest.main()
'''


# 11. Function is_rightangled, given the length of three sides of
# a triangle, determine whether the triangle is right-angled.
# The sides can be given to the function in any order.
'''
def is_rightangled(a, b, c):
    """Function is_rightangled."""
    is_rightangled = True
    if max(a, b, c) == a:
        is_rightangled = abs(math.hypot(b, c) - a) < 0.0001
    elif max(a, b, c) == b:
        is_rightangled = abs(math.hypot(a, c) - b) < 0.0001
    else:
        is_rightangled = abs(math.hypot(a, b) - c) < 0.0001
    return is_rightangled


class TestRightAngled(unittest.TestCase):
    """Class Test."""

    def test_isrightangled(self):
        """Test."""
        self.assertEqual(is_rightangled(0.5, 0.64031, 0.4), True)

if __name__ == "__main__":
    unittest.main()
'''


# 12. Write function called isleap, which takes year as an argument.
# Return True if it's a leap year, false otherwise.
'''
def isleap(year):
    """Function isleap."""
    return 1900 < year < 2078 and (year % 4 == 0 or year % 100 == 0 and
                                   year % 400 == 0)


class TestIsLeap(unittest.TestCase):
    """Class Test."""

    def test_isleap(self):
        """Test."""
        self.assertEqual(isleap(2056), True)

if __name__ == "__main__":
    unittest.main()
'''


# 13. Use algorithm to compute the Easter Sunday for any year between
# 1900 to 2099. Ask the user to enter a year.
# Special years: 1954, 1981, 2049, 2076. Then subtract 7 from the date
# year = int(input("Enter any year between 1900 to 2099: "))

'''
def easterday(year):
    """Easter day."""
    if year >= 1900 and year <= 2099:
        a = year % 19
        b = year % 4
        c = year % 7
        d = (19 * a + 24) % 30
        e = (2 * b + 4 * c + 6 * d + 5) % 7
        dateofeaster = 22 + d + e

        if year == 1954 or year == 1981 or year == 2049 or year == 2076:
            dateofeaster -= 7

        if dateofeaster > 31:
            return ("April", dateofeaster - 31, year)
        else:
            return ("March", dateofeaster, year)
    elif year < 1900 or year > 2099:
        return ("Error. You entered a year that is out of range.")


class TestEasterDay(unittest.TestCase):
    """Class Test."""

    def test_easterday(self):
        """Test."""
        self.assertEqual(easterday(1954), ("April", 18, 1954))

if __name__ == "__main__":
    unittest.main()
'''
