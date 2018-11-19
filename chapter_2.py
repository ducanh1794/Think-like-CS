'''
1. Take the sentence: "All work and no play makes Jack a dull boy". Store each word in a separate variable, then print out the sentence on one line using print.
'''

word_1 = "All"
word_2 = " work"
word_3 = " and"
word_4 = " no"
word_5 = " play"
word_6 = " makes"
word_7 = " Jack"
word_8 = " a"
word_9 = " dull"
word_10 = " boy."

print(word_1 + word_2 + word_3 + word_4 + word_5 + word_6 + word_7 + word_8 + word_9 + word_10)


'''
2. Add parenthesis to expression "6 * 1 - 2" to change
its value from 4 to -6
'''

# This line is a comment. It starts with a hashtag
print(6 * (1 - 2))


'''
3. Place a comment before a line of code that previously worked, and record what happens when you rerun the program
'''


'''
4. Start the Python interpreter and enter "bruce + 4" at the prompt. This will give you an error:
'''

#print(bruce + 4)

#Assign a value to "bruce" so that "bruce + 4" evaluates to 10

bruce = 6
print(bruce + 4)


'''
5. The formula for computing the final amount if one is earning compound interest is given on Wikipedia as

A = P * (1 + r/n)**(n * t)
#Exponentiation has the next highest precedence

Where,
 P = principal amount (initial investment)
 r = annual nominal interest rate (as a decimal)
 n = number of times the interest is compounded per year
 t = number of years
'''

#t = int(input("Enter number of years: "))
P = 10000
n = 12
r = 0.08

#A = P * (1 + r/n)**(n*t)

#print("The final amount after " + str(t) + " years: " + str(A))


'''
6. Evaluate the following numerical expressions in your head, then use the Python interpreter to check your results:
'''

'''
print(5 % 2)
print(9 % 5)
print(15 % 12)
print(12 % 15)
print(6 % 6)
print(0 % 7)
print(7 % 0)
'''


'''
7. You look at the clock and it is exactly 2pm. You set an alarm to go off in 51 hours. At what time does the alarm go off? (Hint: you could count on your fingers, but this is not what we're after. If you are tempted to count on your fingers, change the 51 to 5100.)
'''

#Answer: The alarm goes off at 17:00


'''
8. Write a Python program to solve the general version of the above problem. Ask the user for the time now (in hours), and ask the number of hours to wait. Your program should output what the time will be on the clock when the alarm goes off.
'''

#Ask the user input the time now (in hours)
current_time = int(input("Enter the current time:"))

#Calculate the time remain a day from current time
time_remain = 24 - current_time

#Ask the user input number of hours to wait
hours_to_wait = int(input("Enter the number of hours to wait:"))

#Calculate the time will be on the clock after going off
time_on_clock = (hours_to_wait - time_remain) % 24

#Print the result
print("It will be " + str(time_on_clock) + ":00 after waiting for " + str(hours_to_wait) + " hours")
