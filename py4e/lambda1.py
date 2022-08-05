def say_hello(name, age):
    return f"Hello {name} my age is: {age}"
print(say_hello("Boutaina",21))

hello = lambda name, age : f"Hello {name} my age is: {age}"
print(hello("Boutaina", 21))

#print(say_hello.__name__)
#print(hello.__name__)
#print(type(hello))
#print(type(say_hello))

print("#"*50)

# bulit in function map
#def formatText(text):
    #return f"- {text.strip().capitalize()} -"
myTexts = [" OSama ", "AHMED", "  sAYed  "]
for name in list(map((lambda text : f"- {text.strip().capitalize()} -"), myTexts)):
    print(name)

print("#"*50)
# ----------------------------------
# -- Built In Functions => Filter --
# ----------------------------------
# [1] Filter Take A Function + Iterator
# [2] Filter Run A Function On Every Element
# [3] The Function Can Be Pre-Defined Function or Lambda Function
# [4] Filter Out All Elements For Which The Function Return True
# [5] The Function Need To Return Boolean Value
# ---------------------------------------------------------------

# Example 1
#def checkNumber(num):
    #return num > 10
#myNumbers = [0, 0, 1, 19, 10, 20, 100, 5, 0]

#myresult = filter(checkNumber, myNumbers)
#for number in myresult:
    #print(number)

# Example 2

#def checkName(name):
    #return name.startswith("O")
#myTexts = ["Osama", "Omer", "Omar", "Ahmed", "Sayed", "Othman"]
#myresult = filter(checkName, myTexts)
#for person in myresult:
    #print(person)

# Example 3

myNames = ["Osama", "Omer", "Omar", "Ahmed", "Sayed", "Othman", "Ameer"]
for person in filter(lambda name : name.startswith("A"), myNames):
     #print(person)

# ----------------------------------
# -- Built In Functions => Reduce --
# ----------------------------------
# [1] Reduce Take A Function + Iterator
# [2] Reduce Run A Function On FIrst and Second Element And Give Result
# [3] Then Run Function On Result And Third Element
# [4] Then Run Function On Rsult And Fourth Element And So On
# [5] Till One ELement is Left And This is The Result of The Reduce
# [6] The Function Can Be Pre-Defined Function or Lambda Function
# ---------------------------------------------------------------

 from functools import reduce

#def sumAll(num1, num2):
    #return num1 + num2
numbers = [1, 8, 2, 9, 100]
#result = reduce(sumAll, numbers)
result = reduce(lambda num1, num2 : num1 + num2, numbers)
print(result)
