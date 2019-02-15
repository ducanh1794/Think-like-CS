"""Exercise."""
import turtle
# 1. What is the result of each of the following:
# 'Python'[1]
# 'Strings are sequences of characters.'[5]
# len("wonderful")
# 'Mystery'[:4]
# 'p' in 'Pineapple'
# 'apple' in 'Pineapple'
# 'pear' not in 'Pineapple'
# 'apple' > 'pineapple'
# 'pineapple' < 'Peach'

'''
def main():
    """Function main."""
    print("Python"[1] == "y")
    print("Strings are sequences of characters."[5] == "g")
    print(len("wonderful") == 9)
    print("Mystery"[:4] == "Myst")
    print(("p" in "Pineapple") is True)
    print(("apple" in "Pineapple") is True)
    print(("pear" not in "Pineapple") is True)
    print(("apple" > "pineapple") is False)
    print(("pineapple" < "Peach") is False)

main()
'''

# 2. Create a loop which output a names list in order from each prefix
# (JKLMNOuPQu) plus suffix (ack)
'''
prefixes = "JKLMNOPQ"
suffix = "ack"

for achar in prefixes:
    if achar == "O" or achar == "Q":
        print(achar + "u" + suffix)
    else:
        print(achar + suffix)
'''

# 3. Assign a variable a triple-quoted string that contains your
# favorite paragraph of text.
# Write a function counts the number of alphabetic characters in text
# Then keep track of how many are the letter "e"
'''
text = """Assign to a variable in your program a triple-quoted string that
contains your favorite paragraph of text - perhaps a poem, a speech, inst-
ructions to bake a cake, some inspirational verses, etc.

Write a function that counts the number of alphabetic characters (a through
z, or A through Z) in your text and then keeps track of how many are the l-
etter ‘e’. Your function should print an analysis of the text like this:"""


def count_e(astring, achar="e"):
    """Function count_e."""
    count_char = 0
    countstr = 0
    for item in astring:
        if item == achar or item == achar.upper():
            count_char += 1
        countstr += 1
    print("Your text contains {} alphabetic characters".format(countstr),
          ", of which {} ({:.2%}) are".format(count_char,
                                              (count_char / countstr)), achar)

count_e(text, "z")
'''

# 4. Print out a neatly formatted multiplication table, up to 12 x 12.
'''
for i in range(13):
    for j in range(13):
        result = i * j
        print(str(i).rjust(5), "*", str(j).rjust(2), "=", str(result).rjust(3))
'''

# 5. Write a function that will return the number of digits in an int.

'''
def num_digit(anum):
    """Function num_digit."""
    astring = str(anum)
    count = 0

    for ch in astring:
        count += 1

    return count

print(num_digit(1))
'''

# 6. Write a function that reverses its string argument.

'''
def reverse(astring):
    """Function reverse."""
    newstr = ""

    for ch in astring:
        newstr = ch + newstr

    return newstr

print(reverse("letgo"))
'''

# 7. Write a function that mirrors its string argument, generating a
# string containing the original string and the string backwards.

'''
def mirror(astring):
    """Function mirror."""
    word = ""

    for ch in astring:
        word = ch + word

    mirror = astring + word
    return mirror

print(mirror("Le"))
'''

# 8. Write a function that removes all occurrences of a given letter
# from a string.

'''
def remove_letter(achar, astring):
    """Function remove_letter."""
    newstr = ""

    for ch in astring:
        if ch != achar:
            newstr += ch

    return newstr

print(remove_letter(" ", "Le Duc Anh"))
'''

# 9. Write a function that recognizes palindromes.

'''
def reverse(astring):
    """Function reverse."""
    newstr = ""

    for ch in astring:
        newstr = ch + newstr

    return newstr


def is_palindrome(astring):
    """Function is_palindrome."""
    newstr = reverse(astring)

    if astring == newstr:
        return True
    else:
        return False

print(is_palindrome(""))
'''

# 10. Write a function that counts how many non-overlapping occurrences
# of a substring appear in a string.

'''
def count_string(substr, astring):
    """Function count_string."""
    cond = True
    count = 0

    while cond:
        a = astring.find(substr)
        if a != -1:
            astring = astring[a + 1:]
            count += 1
        else:
            cond = False

    return count

count_substr = count_string("nanan", "banana")
print(count_substr)
'''

# 11. Write a function that removes the first occurrence of a string
# from another string.

'''
def remove_str(substr, astring):
    """Function remove_str."""
    first_substr = astring.find(substr)
    len_substr = len(substr)
    newstr = ""

    if first_substr != -1:
        newstr = astring[:first_substr] + astring[first_substr + len_substr:]
    else:
        return astring

    return newstr

print(remove_str("egg", "bicycle"))
'''

# 12. Write a function that removes all occurrences of a string from
# another string.

'''
def remove_all(substr, astring):
    """Function remove_str."""
    len_substr = len(substr)
    cond = True

    while cond:
        substr_pos = astring.find(substr)
        if substr_pos != -1:
            astring = astring[:substr_pos] + astring[substr_pos + len_substr:]
        else:
            cond = False

    newstr = astring
    return newstr

print(remove_all("eggs", "bicycle"))
'''

# 13. Write a function that creates a turtle which draws a Hilbert
# curve. Use 90 degrees.

'''
def apply_rule(lhch):
    """Function apply_rule."""
    rhstr = ""
    if lhch == "L":
        rhstr = "+RF-LFL-FR+"
    elif lhch == "R":
        rhstr = "-LF+RFR+FL-"
    else:
        return lhch

    return rhstr


def process_str(oldstr):
    """Function process_str."""
    newstr = ""
    for ch in oldstr:
        newstr += apply_rule(ch)

    return newstr


def create_lsystems(numiters, original_str):
    """Function create_lsystems."""
    for num in range(numiters):
        newstr = process_str(original_str)
        original_str = newstr

    return newstr


def draw_turtle(t, distance, instructions):
    """Function draw_turtle."""
    if instructions == "F":
        t.forward(distance)
    elif instructions == "+":
        t.right(90)
    elif instructions == "-":
        t.left(90)


def main():
    """Function main."""
    window = turtle.Screen()
    anton = turtle.Turtle()
    anton.speed(0)
    anton.up()
    anton.goto(-170, 160)
    anton.down()
    inst = create_lsystems(5, "L")
    for ch in inst:
        draw_turtle(anton, 5, ch)
    window.exitonclick()

main()
'''

# 14. Write a function that creates a turtle draws a dragon curve. Use
# 90 degrees.

'''
def apply_rule(lhch):
    """Function apply_rule."""
    rhstr = ""
    if lhch == "X":
        rhstr = "X+YF+"
    elif lhch == "Y":
        rhstr = "-FX-Y"
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
    for index in range(numiters):
        newstr = process_str(originalstr)
        originalstr = newstr

    return newstr


def draw_turtle(t, distance, instructions):
    """Function draw_turtle."""
    if instructions == "F":
        t.forward(distance)
    elif instructions == "+":
        t.right(90)
    elif instructions == "-":
        t.left(90)


def main():
    """Function main."""
    window = turtle.Screen()
    anton = turtle.Turtle()
    anton.speed(0)
    anton.up()
    anton.goto(-170, 80)
    anton.down()
    inst = create_lsystems(6, "FX")
    anton.fillcolor("blue")
    anton.begin_fill()
    for ch in inst:
        draw_turtle(anton, 10, ch)
    anton.end_fill()
    window.exitonclick()

main()
'''

# 15. Write a function that draws an arrowhead curve via turtle library

'''
def apply_rule(lhch):
    """Function apply_rule."""
    rhstr = ""
    if lhch == "X":
        rhstr = "YF+XF+Y"
    elif lhch == "Y":
        rhstr = "XF-YF-X"
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
    for index in range(numiters):
        newstr = process_str(originalstr)
        originalstr = newstr

    return newstr


def draw_turtle(t, distance, instructions):
    """Function draw_turtle."""
    if instructions == "F":
        t.forward(distance)
    elif instructions == "+":
        t.right(60)
    elif instructions == "-":
        t.left(60)


def main():
    """Function main."""
    window = turtle.Screen()
    anton = turtle.Turtle()
    anton.speed(0)
    anton.up()
    anton.goto(-170, 80)
    anton.down()
    inst = create_lsystems(5, "YF")
    anton.fillcolor("blue")
    anton.begin_fill()
    for ch in inst:
        draw_turtle(anton, 7, ch)
    anton.end_fill()
    window.exitonclick()

main()
'''

# 16. Write a function that draws Peano-Gosper curve.

'''
def apply_rule(lhch):
    """Function apply_rule."""
    rhstr = ""
    if lhch == "X":
        rhstr = "X+YF++YF-FX--FXFX-YF+"
    elif lhch == "Y":
        rhstr = "-FX+YFYF++YF+FX--FX-Y"
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
    for index in range(numiters):
        newstr = process_str(originalstr)
        originalstr = newstr

    return newstr


def draw_turtle(t, distance, instructions):
    """Function draw_turtle."""
    if instructions == "F":
        t.forward(distance)
    elif instructions == "+":
        t.right(60)
    elif instructions == "-":
        t.left(60)


def main():
    """Function main."""
    window = turtle.Screen()
    anton = turtle.Turtle()
    anton.speed(0)
    anton.up()
    anton.goto(-170, 80)
    anton.down()
    inst = create_lsystems(3, "FX")
    anton.fillcolor("blue")
    anton.begin_fill()
    for ch in inst:
        draw_turtle(anton, 7, ch)
    anton.end_fill()
    window.exitonclick()

main()
'''

# 17. Write a function that creates the Sierpinski Triangle

'''
def apply_rule(lhch):
    """Function apply_rule."""
    rhstr = ""
    if lhch == "F":
        rhstr = "FF"
    elif lhch == "X":
        rhstr = "--FXF++FXF++FXF--"
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
    for index in range(numiters):
        newstr = process_str(originalstr)
        originalstr = newstr

    return newstr


def draw_turtle(t, distance, instructions):
    """Function draw_turtle."""
    if instructions == "F":
        t.forward(distance)
    elif instructions == "+":
        t.right(60)
    elif instructions == "-":
        t.left(60)


def main():
    """Function main."""
    window = turtle.Screen()
    anton = turtle.Turtle()
    anton.speed(0)
    anton.up()
    anton.goto(-170, 80)
    anton.down()
    inst = create_lsystems(3, "FXF--FF--FF")
    anton.fillcolor("blue")
    anton.begin_fill()
    for ch in inst:
        draw_turtle(anton, 7, ch)
    anton.end_fill()
    window.exitonclick()

main()
'''

# 18.
