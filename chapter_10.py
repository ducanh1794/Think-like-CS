"""Exercises."""
import random
import turtle

# 1. Draw a reference diagram for a and b before and after b[0] = 5
# is executed.
'''
a = [1, 2, 3]
b = a[:]

# Before b[0] = 5 is executed
print(a == [1, 2, 3])
print(b == [1, 2, 3])
print((a == b) is True)
print((a is b) is False)

# After b[0] = 5 is executed
b[0] = 5
print(a == [1, 2, 3])
print(b == [5, 2, 3])
'''

# 2. Create a list called my_list with the following 6 items: 76, 92.3
# "hello", True, 4, 76. Do it with both append and with concatenation,
# one item at a time
my_list = []
# Do it with append
'''
my_list.append(76)
my_list.append(92.3)
my_list.append("hello")
my_list.append(True)
my_list.append(4)
my_list.append(76)

print(my_list)
'''

# Do it with concatenation
'''
my_list += [76]
my_list += [92.3]
my_list += ["hello"]
my_list += [True]
my_list += [4]
my_list += [76]

print(my_list)


# 3. Starting with the list of the previous exercise,
# write Python statements to do the following:
# Append "apple" and 76 to the list
my_list.append("apple")
my_list.append(76)

# Insert "cat" at position 3
my_list.insert(3, "cat")

# Insert value 99 at the start of the list
my_list.insert(0, 99)

# Find the index of "hello"
print(my_list.index("hello"))

# Count the number of 76s in the list
print(my_list.count(76))

# Remove the first occurrence of 76 from the list
my_list.remove(76)

# Remove True from the list using pop and index
value_pos = my_list.index(True)
print(my_list.pop(value_pos))

print(my_list)
'''

# 4. Create a list that contains 100 random integers between 0 and 1000
# (Use iteration, append and the random module). Then write a function
# called average that will take list as a parameter and return average
'''
my_list = [random.randrange(0, 1000) for i in range(100)]


def average(alist):
    """Function average."""
    total = 0
    for num in alist:
        total += num
    average = total / len(alist)

    return average

print(average(my_list))
'''

# 5. Write a function that will take a list of 100 random integer
# between 0 and 1000 and return maximum number in the list.
'''
my_list = [random.randrange(0, 1000) for i in range(100)]


def max_number(alist):
    """Function max_number."""
    maxnum = 0
    for num in alist:
        if maxnum < num:
            maxnum = num

    return maxnum

print(max_number(my_list))
print(max(my_list))
'''

# 6. Write a function that returns the sum of the square of numbers
# in a list.
'''
my_list = [2, 3, 4]


def sum_of_squares(alist):
    """Function sum_of_squares."""
    total = 0
    for num in alist:
        total += num ** 2

    return total

print(sum_of_squares(my_list))
'''

# 7. Write a function to count how many the odds are in the list
'''
my_list = [0, 1, 2, -1, -3]


def count(alist):
    """Function count."""
    count = 0
    for num in alist:
        if num % 2 != 0:
            count += 1

    return count

print(count(my_list))
'''

# 8. Sum up all the even numbers in the list
'''
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

total = 0
for num in my_list:
    if num % 2 == 0:
        total += num

print(total)
'''

# 9. Sum up all the negative numbers in the list
'''
my_list = [-1, -2, -3, -4, 1, 2, 3, 4]

total = 0

for num in my_list:
    if num < 0:
        total += num

print(total)
'''

# 10. Count how many words in a list have length 5
'''
my_textlist = ["dfdfdfd", "dfdfd", "asddf", ""]

count = 0

for value in my_textlist:
    if len(value) == 5:
        count += 1

print(count)
'''

# 11. Sum up to all the numbers in the list but not including the first
# even number
'''
my_list = [1, 2, 1, 1, 0, 3]

total = 0

for num in my_list:
    if num % 2 != 0:
        total += num
    else:
        print(total)
        break
'''

# 12. Count how many words occur in a list up to but not including the
# first occurrence of the word "sam"
'''
my_textlist = ["sdfa", "fdfds", "sam", "ddfd"]

count = 0

for word in my_textlist:
    if word != "sam":
        count += 1
    else:
        count += 1
        print(count)
        break
'''

# 13. Write your own functions to do list methods: count, reverse,
# in, index, insert
'''
my_list = [1, 2, 3, 4, 5, 6]
my_textlist = ["a", "b", "c", "d", "e", "f"]
my_mixlist = [1, "a", 2, "b", 3, "c", 4, "d"]


def count(alist, ch):
    """Function count."""
    count = 0
    for value in alist:
        if value == ch:
            count += 1

    return count

print(count(my_textlist, "a"))


def reverse(alist):
    """Function reverse."""
    new_list = []
    for index in range(len(alist) - 1, -1, -1):
        new_list.append(alist[index])

    return new_list

my_list = reverse(my_list)
print(my_list)


def is_inlist(alist, ch):
    """Function is_inlist."""
    for value in alist:
        if value == ch:
            return True
        else:
            return False

print(is_inlist(my_textlist, "ab"))


def index(alist, ch):
    """Function index."""
    for index in range(len(alist)):
        if alist[index] == ch:
            return index

# print(index(my_list, 2))

print(my_list[:-1])
print(my_list[-1:])


def insert(alist, pos, ch):
    """Function insert."""
    new_list = alist[:pos] + [ch] + alist[pos:]

    return new_list

my_list = insert(my_list, 6, 999)
print(my_list)
'''

# 14. Write a function replace(s, old, new) that replace all
# occurrences of old with new in a string s
'''
my_str = "I love spom!  Spom is my favorite food.  Spom, spom, spom, yum!"


def replace(s, old, new):
    """Function replace."""
    temp_list = s.split(old)
    print(temp_list)
    new_str = new.join(temp_list)
    return new_str

print(replace(my_str, "om", "am"))
'''

# 15. Apply the rules for an L-system that creates a common garden herb
# H, H -> HFX[+H][-H], X -> X[-FFF][+FFF]FX

'''
def apply_rule(lhch):
    """Function apply_rule."""
    rhstr = ""
    if lhch == "H":
        rhstr = "HFX[+H][-H]"
    elif lhch == "X":
        rhstr = "X[-FFF][+FFF]FX"
    else:
        rhstr = lhch

    return rhstr


def process_str(oldstr):
    """Function process_str."""
    newstr = ""
    for ch in oldstr:
        newstr += apply_rule(ch)

    return newstr


def create_lsystems(numiters, originalstr):
    """Function create_lsystems."""
    newstr = ""
    for num in range(numiters):
        newstr = process_str(originalstr)
        originalstr = newstr

    return newstr


def draw_turtle(t, insts, distance, angle=25.7):
    """Function draw_turtle."""
    pos_list = []
    for cmd in insts:
        if cmd == "F":
            t.forward(distance)
        elif cmd == "+":
            t.right(angle)
        elif cmd == "-":
            t.left(angle)
        elif cmd == "[":
            pos_list.append([t.heading(), t.xcor(), t.ycor()])
            print(pos_list)
        elif cmd == "]":
            remove = pos_list.pop()
            t.up()
            t.setheading(remove[0])
            t.goto(remove[1], remove[2])
            t.down()


def main():
    """Function main."""
    window = turtle.Screen()
    anton = turtle.Turtle()
    anton.speed(0)
    anton.pensize(2)
    instructions = create_lsystems(5, "H")
    draw_turtle(anton, instructions, 7)
    window.exitonclick()

main()
'''

# 16. Write a function that uses an L-system to draw turtle. Use angle
# of 25

'''
def apply_rule(lhch):
    """Function apply_rule."""
    rhstr = ""
    if lhch == "F":
        rhstr = "F[-F]F[+F]F"
    else:
        rhstr = lhch

    return rhstr


def process_str(oldstr):
    """Function process_str."""
    newstr = ""
    for ch in oldstr:
        newstr += apply_rule(ch)

    return newstr


def create_lsystem(numiters, originalstr):
    """Function create_lsystem."""
    newstr = ""
    for num in range(numiters):
        newstr = process_str(originalstr)
        originalstr = newstr

    return newstr


def draw_turtle(t, insts, distance, angle=25):
    """Function draw_turtle."""
    pos_list = []
    for cmd in insts:
        if cmd == "F":
            t.forward(distance)
        elif cmd == "+":
            t.right(angle)
        elif cmd == "-":
            t.left(angle)
        elif cmd == "[":
            pos_list.append([t.heading(), t.xcor(), t.ycor()])
        elif cmd == "]":
            back_pos = pos_list.pop()
            t.up()
            t.setheading(back_pos[0])
            t.goto(back_pos[1], back_pos[2])
            t.down()


def main():
    """Function main."""
    window = turtle.Screen()
    anton = turtle.Turtle()
    anton.speed(0)
    anton.shape("blank")
    window.bgcolor("black")
    anton.color("hotpink")
    anton.up()
    anton.forward(-250)
    anton.down()
    anton.pensize(1)
    inst = create_lsystem(4, "F")
    draw_turtle(anton, inst, 7)
    window.exitonclick()

main()
'''
