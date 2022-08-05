# ----------------------------------------
# -- Decorators => Practical Speed Test --
# ----------------------------------------

from time import time

#def myDecorator(func):

    #def nestedFunc(*numbers): # *numbers we use it for allowing us to put any numbers of parameters in our function calculate

        #for number in numbers:

            #if number < 0:

                #print("Beware One Of The Numbers Is Less Than Zero")

        #func(*numbers)
    
    #return nestedFunc

#@myDecorator

#def calculate(n1, n2, n3, n4):

    #print(n1 + n2 + n3 + n4)

#calculate(-5, 90, 50, 150)

def speedTest(func):

    def wrapper():

        start = time()

        func()

        end = time()

        print(f"Function Running Time Is: {end - start}")
    
    return wrapper

@speedTest

def bigLoop():

  for number in range(1, 2000):

    print(number)

bigLoop()