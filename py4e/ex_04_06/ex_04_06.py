
def computepay(h,r):
    if h <= 40:
        x = h * r
        return x
    elif h > 40:
        y = h * r
        z = (h - 40.0)*r*0.5
        a = y + z
        return a
try:
    hrs = input("Enter Hours:")
    h = float(hrs)
    rte = input("Enter Rate:")
    r = float(rte)
except:
    print('please Enter only number')
    hrs = input("Enter Hours:")
    rte = input("Enter Rate:")
    h = float(hrs)
    r = float(rte)
p = computepay(h,r)
print(p)
