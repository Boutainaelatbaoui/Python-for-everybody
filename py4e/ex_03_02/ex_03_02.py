#compute gross Pay
a = input("Enter Hours: ")
b = input("Enter Rate: ")
try:
    hr = float(a)
    rt = float(b)
except:
    print("Error, please enter numeric input")
    quit()
if hr > 40 :
    x = (hr - 40.0) * rt * 1.5
    y = rt*(hr-(hr-40.0))
    z = x+y
else:
    z = hr * rt
print("Pay: ", z, "$")
