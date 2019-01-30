"""Exercises."""
# import turtle
# import random
from PIL import Image
# import numpy as np

# 1. Write Newton's sqrt function that prints out better result each
# time. Call your modified function with an argument 25.

'''
def newton_sqrt(n):
    """Find square of root of number n."""
    approx = n * 0.5
    better = 0.5 * (approx + n / approx)
    while approx != better:
        approx = better
        better = 0.5 * (approx + n / approx)
        print("The approx:", better)
    return better

print("The final:", newton_sqrt(25))
'''

# 2. Write print_triangular_numbers(n), that prints out the number
# of dot from a triangular numbers

'''
def print_triangular_numbers(n):
    """Function."""
    dot = n * (n + 1) // 2
    return dot

print(print_triangular_numbers(60))
'''


# 3. Write is_prime function, that takes a single integer argument and
# returns True when the argument is a prime number, False otherwise.

'''
def is_prime(n):
    """Return a number is a prime or not."""
    for m in range(2, n):
        if n % m == 0:
            return False
    return True

print(is_prime(4813))
'''


# 4. Modify the walking turtle so that rather than a 90 degree left or
# right turn, the angle of the turn will be randomly degree at each
# step.
'''
def walking_turtle(t1, t2, wn):
    """Function walking turtle with turtle t and window wn."""
    # turtles' positions:
    t1.up()
    t1.goto(random.randrange(-199, 200), random.randrange(-199, 200))

    t2.up()
    t2.goto(random.randrange(-199, 200), random.randrange(-199, 200))

    t1.down()
    t2.down()
    cond = True
    x_right = wn.window_width() / 2
    x_left = -(wn.window_width() / 2)
    y_top = wn.window_height() / 2
    y_btm = -(wn.window_height() / 2)

    while cond:
        if (t1.xcor() < x_left or t2.xcor() < x_left) or \
           (t1.xcor() or t2.xcor()) > x_right:
            break
        elif (t1.ycor() or t2.ycor()) < y_btm or \
             (t1.ycor() or t2.ycor()) > y_top:
            break

        coin = random.randrange(2)

        if coin == 0:
            t1.left(random.randrange(361))
            t2.left(random.randrange(361))
        else:
            t1.right(random.randrange(361))
            t2.right(random.randrange(361))

        t1.forward(50)
        t2.forward(50)


def main():
    """Main."""
    window = turtle.Screen()
    anton = turtle.Turtle()
    andrey = turtle.Turtle()
    window.setup(400, 400)
    walking_turtle(anton, andrey, window)
    window.exitonclick()

main()
'''


# 5. Modify the turtle walk program to create 2 turtles, each starts
# at random position. Keep the turtles moving until one of them
# reach out of screen.


# 6. Modify the turtle walk program so that the turtles will turn
# around when it hits borders of screen or one turtle hits another.
# (when the position of the two turtles are closer than some small
# number)
'''
window = turtle.Screen()
anton, andrey = turtle.Turtle(), turtle.Turtle()
anton.color("red")
andrey.color("blue")
window.setup(400, 400)

x_right = window.window_width() / 2
x_left = -(window.window_width() / 2)
y_top = window.window_height() / 2
y_btm = -(window.window_height() / 2)

for t in [anton, andrey]:
    t.up()
    t.goto(random.randrange(x_left + 1, x_right),
           random.randrange(y_btm + 1, y_top))
    t.setheading(random.randrange(361))
    t.down()


def move(t):
    """Turtle moving."""
    coin = random.randrange(2)

    if coin == 0:
        t.left(random.randrange(361))
    else:
        t.right(random.randrange(361))
    t.forward(50)


def is_collides(t1, t2):
    """Function is_collides."""
    if t1.distance(t2) < 20:
        t1.left(180)
        t1.forward(50)


def isin_screen(t, wn):
    """
    Doc.

    Function determines turtles are whether still in screen or not.
    """
    global x_right, x_left, y_top, y_btm

    stillin = True

    if t.xcor() < x_left or t.xcor() > x_right or \
       t.ycor() < y_btm or t.ycor() > y_top:
        t.left(180)
        t.forward(50)
    return stillin

while isin_screen(anton, window) and isin_screen(andrey, window):
    is_collides(anton, andrey)
    move(anton)
    move(andrey)

window.exitonclick()
'''

# 7. Write a function to remove all the red from luther.jpg
'''
img = Image.open("C:/Users/Administrator/Desktop/ThinklikeaCS" +
                 "/luther.jpg")


def remove_red(x):
    """Function remove_red."""
    for row in range(x.height):
        for col in range(x.width):
            old_color = x.getpixel((col, row))
            new_color = tuple(np.subtract(old_color, (old_color[0], 0, 0)))
            x.putpixel((col, row), new_color)

remove_red(img)
img.show()
'''


# 8. Write a function to convert img into grayscale
'''
img = Image.open("C:/Users/Administrator/Desktop/ThinklikeaCS" +
                 "/tien.jpg")
p = img.convert("L")
p.show()
p.save("tien2.jpg")
'''
# 9. Write a function to convert img into black and white
'''
img = Image.open("C:/Users/Administrator/Desktop/ThinklikeaCS" +
                 "/luther.jpg")
p = img.convert("1", dither=0)
p.show()
'''

# 10. Write a function to convert img to sepia tone. The formula for
# creating a sepia tone is as follows:
# newr = R*0.393+G*0.769+B*0.189
# newg = R*0.349+G*0.686+B*0.168
# newb = R*0.272+G*0.534+B*0.131

img = Image.open("C:/Users/Administrator/Desktop/ThinklikeaCS" +
                 "/margarethamilton.jpg")


def sopia_tone(input_img):
    """Function sopia_tone."""
    new_img = Image.new("RGB", (input_img.width, input_img.height))
    for row in range(input_img.height):
        for col in range(input_img.width):
            old_color = input_img.getpixel((col, row))
            newr = int(old_color[0] * 0.393 + old_color[1] * 0.769 +
                       old_color[2] * 0.189)
            newg = int(old_color[0] * 0.349 + old_color[1] * 0.686 +
                       old_color[2] * 0.168)
            newb = int(old_color[0] * 0.272 + old_color[1] * 0.534 +
                       old_color[2] * 0.131)

            new_img.putpixel((col, row), (newr, newg, newb))
    return new_img

newpic = sopia_tone(img)
newpic.save("margarethamilton1.jpg")



# 11. Write a function to uniformly enlarge an img by a factor of 2
# (Double the size)
'''
img = Image.open("C:/Users/Administrator/Desktop/ThinklikeaCS" +
                 "/luther.jpg")


def enlarge_img(input_img):
    """Function enlarge_img."""
    img_width = img.width * 2
    img_height = img.height * 2
    new_img = Image.new("RGB", (img_width, img_height))
    for row in range(input_img.height):
        for col in range(input_img.width):
            old_pic = input_img.getpixel((col, row))
            new_img.putpixel((col * 2, row * 2), old_pic)
            new_img.putpixel((col * 2 + 1, row * 2), old_pic)
            new_img.putpixel((col * 2, row * 2 + 1), old_pic)
            new_img.putpixel((col * 2 + 1, row * 2 + 1), old_pic)
    return new_img

bigimg = enlarge_img(img)
bigimg.show()
'''

#### 12. Reducing the blockiness of the img is to replace each pixel with
# the average values of the pixels around it. Write a function that
# takes an img as a parameter. And return a new img
'''
img = Image.open("C:/Users/Administrator/Desktop/ThinklikeaCS" +
                 "/luther.jpg")


def enlarge(input_img):
    """Function enlarge."""
    img_width = input_img.width * 2
    img_height = input_img.height * 2
    new_img = Image.new("RGB", (img_width, img_height))

    for row in range(input_img.height):
        for col in range(input_img.width):
            old_color = input_img.getpixel((col, row))
            new_img.putpixel((col * 2, row * 2), old_color)
            new_img.putpixel((col * 2 + 1, row * 2), old_color)
            new_img.putpixel((col * 2 + 1, row * 2 + 1), old_color)
            new_img.putpixel((col * 2, row * 2 + 1), old_color)
    return new_img

bigimg = enlarge(img)
doublesz = bigimg.save("luther1.jpg")
img1 = Image.open("luther1.jpg")


def smooth_shape(input_img):
    """Funtion smooth_shape."""
    new_img1 = Image.new("RGB", (input_img.width, input_img.height))
    total = (0, 0, 0)
    for row in range(input_img.height):
        for col in range(input_img.width):
            if row == 0 and col != 0 and col != input_img.width - 1:
                for row_1 in range(2):
                    for col_1 in range(col - 1, col + 2):
                        if (col_1, row_1) == (col, 0):
                            continue
                        old_color = input_img.getpixel((col_1, row_1))
                        total += np.array(old_color)
                new_color = tuple(total // 5)
            elif row == input_img.height - 1 and col != 0 and\
                    col != input_img.width - 1:
                for row_2 in range(input_img.height - 2, input_img.height):
                    for col_2 in range(col - 1, col + 2):
                        if (col_2, row_2) == (col, input_img.height - 1):
                            continue
                        old_color = input_img.getpixel((col_2, row_2))
                        total += np.array(old_color)
                new_color = tuple(total // 5)
            elif col == 0 and row != 0 and row != input_img.height - 1:
                for row_3 in range(row - 1, row + 2):
                    for col_3 in range(2):
                        if (col_3, row_3) == (0, row):
                            continue
                        old_color = input_img.getpixel((col_3, row_3))
                        total += np.array(old_color)
                new_color = tuple(total // 5)
            elif col == input_img.width - 1 and\
                    row != 0 and row != input_img.height - 1:
                for row_4 in range(row - 1, row + 2):
                    for col_4 in \
                            range(input_img.width - 2, input_img.width):
                        if (col_4, row_4) == (input_img.width - 1, row):
                            continue
                        old_color = input_img.getpixel((col_4, row_4))
                        total += np.array(old_color)
                new_color = tuple(total // 5)
            elif row != 0 and col != 0 and row != input_img.height - 1 and\
                    col != input_img.width - 1:
                for row_0 in range(row - 1, row + 2):
                    for col_0 in range(col - 1, col + 2):
                        if (col_0, row_0) == (col, row):
                            continue
                        old_color = input_img.getpixel((col_0, row_0))
                        total += np.array(old_color)
                new_color = tuple(total // 8)
            else:
                new_color = input_img.getpixel((col, row))
            new_img1.putpixel((col, row), new_color)
    return new_img1


smooth = smooth_shape(img1)
smooth.show()
'''

# 13. Write a general pixel mapper function that will take an img and
# a pixel mapping function as parameters. The pixel mapping function
# will perform on a single pixel and return a new pixel.
'''
img = Image.open("C:/Users/Administrator/Desktop/ThinklikeaCS" +
                 "/luther.jpg")


def black_white(old_color):
    """Function pixel_mapping."""
    newred = int(old_color[0] * 0.299 + old_color[1] * 0.587 +
                 old_color[2] * 0.114)
    newgreen = int(old_color[0] * 0.299 + old_color[1] * 0.587 +
                   old_color[2] * 0.114)
    newblue = int(old_color[0] * 0.299 + old_color[1] * 0.587 +
                  old_color[2] * 0.114)
    new_color = (newred, newgreen, newblue)
    return new_color


def general_mapper(input_img, input_px):
    """Function general_mapper."""
    new_img = Image.new("RGB", (input_img.width, input_img.height))
    for row in range(input_img.height):
        for col in range(input_img.width):
            old_color = input_img.getpixel((col, row))
            new_img.putpixel((col, row), input_px(old_color))
    return new_img

mapper_func = general_mapper(img, black_white)
mapper_func.show()
'''

#### 14.
#### 15.
