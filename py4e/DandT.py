# -----------------------------------
# -- Date and Time => Introduction --
# -----------------------------------

import datetime

#print(dir(datetime))
#print(dir(datetime.datetime))

# Print The Current Date and Time
print(datetime.datetime.now())

print("#" * 40)

# Print The Current Year
print(datetime.datetime.now().year)

# Print The Current Month
print(datetime.datetime.now().month)

# Print The Current Day
print(datetime.datetime.now().day)

print("#" * 40)

# Print Start and End Of Date
print(datetime.datetime.min)
print(datetime.datetime.max)

print("#" * 40)

#print(dir(datetime.datetime.now()))

# Print The Current Time
print(datetime.datetime.now().time())

print("#" * 40)

# Print The Current Time Hour
print(datetime.datetime.now().time().hour)

# Print The Current Time Minute
print(datetime.datetime.now().time().minute)

# Print The Current Time Second
print(datetime.datetime.now().time().second)

print("#" * 40)

# Print Start and End Of Time
print(datetime.time.min)
print(datetime.time.max)

print("#" * 40)

# Print Specific Date
print(datetime.datetime(1998, 10, 2, 6, 25, 55, 15098))

print("#" * 40)

myBirthDay = datetime.datetime(1998, 10, 2)
dateNow = datetime.datetime.now()

print(f"My birthday is {myBirthDay} And ", end="")
print(f"Date Now is {dateNow}")
print(f" I Lived For {(dateNow - myBirthDay).days} Days.")

print("#" * 60)

# ----------------------------------
# -- Date and Time => Format Date --
# ----------------------------------
# https://strftime.org/
# ---------------------

print(myBirthDay.strftime("%a"))
print(myBirthDay.strftime("%A"))
print(myBirthDay.strftime("%b"))
print(myBirthDay.strftime("%B"))

print(myBirthDay.strftime("%d/%B/%Y"))
print(myBirthDay.strftime("%d - %B - %Y"))
print(myBirthDay.strftime("%B - %Y"))






