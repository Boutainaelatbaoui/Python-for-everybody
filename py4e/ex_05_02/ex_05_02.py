largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break

    try :
        num = int(num)
    except :
        print ("Invalid input, Please Enter only number or Enter done for view the result ")
        continue
    if largest is None :
        largest = num
    elif num > largest :
        largest = num
    if smallest is None :
        smallest = num
    elif num < smallest :
        smallest = num
print("Maximum is", largest)
print ("Minimum is", smallest)
