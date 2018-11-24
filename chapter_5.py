"""Exercises."""
# I. Use for loops to print 10 random numbers generators
import random
import math

for i in range(10):
    print(random.random())


# II. Repeat the above exercise but print 10 random numbers between 25 and 35,
# inclusive

for i in range(10):
    print(random.randrange(25, 36))


# III. Find a function that will compute the relationship between the
# length of the hypotenuse of a right triangle and the lengths of the
# other 2 sides

"""
a = int(input("Enter the length of the first side at right angle: "))
b = int(input("Enter the length of the second side at right angle: "))
c = math.hypot(a, b)
print("the length of the hypotenuse: ", c)
"""


# IV. Create a program to caculate an approximation for pi.
# Then print its result as well as the value of math.pi

x = 9999999999999999999999999999
pi = x * math.sin(math.radians(180) / x)

print(pi, math.pi)
