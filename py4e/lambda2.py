#num = input("Please Enter a number: ")
#func = lambda num : f"{num} + 15"
#print(func)

x = float(input('Please Enter a number: '))
y = float(input('Please Enter a second number: '))
b= x + y
fun = lambda x, y : f"{b}"
print(fun(x, y))