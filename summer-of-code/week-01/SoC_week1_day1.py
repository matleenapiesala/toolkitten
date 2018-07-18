# Summer of Code
# Week1 day1 exercises.
# Printing the questions and answers to make it more readable.

# https://github.com/1millionwomentotech/toolkitten/blob/master/summer-of-code/week-01/day1.md
# (c) Matleena Piesala

# ==========================================================
print('Hours in a year. How many hours are in a year?')
# 24 hours * 365 days
print(24 * 365)

# Another way to do this
# Store the result in a variable end print it with some text
x = 24* 365

# both ' and " work when printing text with variables
print('There are ', x, ' hours in a year.')
print("There are ", x, " hours in a year.")
print("\n")     # prints a new line

# ==========================================================
print('Minutes in a decade. How many minutes are in a decade?')
# how many leap years there are in this decade. 2 or 3?
# 60 minutes * 24 hours * 365 days * 10 years
# plus 2 or 3 leap days 2*60*24 or 3*60*24

# first calculate and store in a variable
y = 60 * 20 * 365 * 10
# print the text, variable y, text and new line
print('There are', y, 'minutes in a decade.\n')

# In real world you need to take leap years into account.
# create a variable for minutes in one leap day
leapday = 60 * 24
# Include calculation in the print
print('Plus 2 or 3 leap years so add', 2*leapday, 'or', 3*leapday, 'minutes.')
print("\n")     # prints a new line

# ============================================================================
print('Your age in seconds. How many seconds old are you?')
# Simple solution: calculate 60*60*24*365*age in years and add 60*60*24* amount of days after your last bday
# for me: 60*60*24*365*44 + 60*60*24*216 (on 17.7.2018)
print('Simple solution:')
print(60*60*24*365*44 + 60*60*24*216)

# More elegant way
# import date function from datetime library. timedelta used later
print('Elegant solution:')
from datetime import date

today = date.today()            # store today in a variable. date.today() gets the current date from the computer
mybday = date(1973, 12, 13)     # my birthday as a date
myage = today - mybday          # calculate my age. Answer is in days
print('Print myage variable:',myage)    # print my age in days. See that it includes also some hours, minutes etc.
myageseconds = 60*60*24*myage.days # Take only days from myage  and make it into seconds
print('My age in seconds:', myageseconds )
print('Why are these different??? You know the answer.') # This is for you to think :D
print("\n")     # prints a new line

# ==============================================================================
print('Andreea Visanoiu​: I\'m 48618000 seconds old hahaha. Calculate @Andreea Visanoiu\'s age.')

andreaseconds = 48618000
andreadays = andreaseconds/(60*60*24)
print(andreadays)
# it is actually enough to calculate the days and then use the below print to show age

from datetime import timedelta
andreabday = today - timedelta(andreadays)
andreaage = today - andreabday
# this now works as Andreea is so young and and her age does not include leap years.
# Could also use 365.2425 as number of days per year and that estimates the leap years.
# That would give and approximation instead of an exact answer.
print('Andreea\'s age today is', andreaage.days, 'days. This equals to', andreaage.days//365, 'year(s) and', andreaage.days%365, 'days.')
print("\n")     # prints a new line

# Explanation
# andreaage.days//365       gives divisor only integer value
# andreaage.days%365        gives the remainder

# ==============================================================================
print('How many days does it take for a 32-bit system to timeout, if it has a bug with integer overflow?')
# I assume this relates to this: https://en.wikipedia.org/wiki/Year_2038_problem
# Maximun integer value is 2147483647 - just fyi.
overflowdate = date(2038, 1, 19)
today = date.today()
daysleft = overflowdate - today
print('In a 32-bit system ther are', daysleft.days, 'days left before integer overflow, if we start counting from 1.1.1970.')
print('Simpler way: 2147483647 / (60*60*24) is equal to', 2147483647/(60*60*24), 'days')

# How about a 64-bit system?
# 64-bit max integer value is 9223372036854775807
maxint = 9223372036854775807
maxintindays = maxint/(60*60*24) # divide by seconds in a minute  * minutes in hour * hours in a day
print('In a 64-bit system ther are', maxintindays, 'days left before integer overflow.')
print('That is eaqual to about', maxintindays/365.2425, 'years')
print("\n")     # prints a new line

# ==============================================================================
print('Calculate your age accurately based on your birthday (maybe use time of day e.g. 8:23am if you know it, use 12:00 noon midday) - you will need Python modules.')
import datetime
format = "%a %b %d %H:%M"   # here we tell the time format used
now = datetime.datetime.now()            # store this date and time in a variable. date.today() tells only date.
mybirthtime = datetime.datetime(1973, 12, 13, 5, 20)     # my birthday as a date
print('My birthday and time is', mybirthtime)
myage2 = now - mybirthtime # my age in days and hours and minutes
print('My age in days and hours:',myage2)
daysinyear = 365.2425 # this tries to take into account leap years and is accurate enough.
myageinyears = round(myage2.days/daysinyear, 2)  # round function rounds the numebr to two decimal places.
print('Is equal to', myageinyears, 'years')     # prints only one decimal place (today) as it rounds to .60 so 0 is left out.

# there is a ready made function to check if a year is a leap year in
# from calendar import isleap
