#all() any()
#bin() we use it for give us a form which is mafhoma to the computer
#id the specifec thing of a variable


#x = [0, 0, []]

#if any(x):
    #print('there\'s at least one element is true')
#else:
    #print('there\'s no any true element')

#a = 1
#b= 1

#print(id(a))
#print(id(b))

# -------- BUILT IN FUNCTION PART 2 -------

#sum(iterable, start)  iterable darori mais start is not important osart howa ra9m kanzidoh man 3adna
#a = [1, 10, 19, 40]
#print(sum(a, 20))

# round(number, numofdigits) like exel ki 9arab ra9am oki3tina hasab ma ktabna man ra9m baghin wra lfasila
#print(round(150.86))
#print(round(150.554, 2))

#range(start, end, step) start not very import it considers 0, end is important and it is not included in the list, step fo rexample when we put 2 it jumb one number like this range(0, 10, 2) the result is [0, 2, 4, 6, 8]
#print(list(range(0, 21, 2)))

#print() sep="" and end==""

#print("Hola", "boutaina", sep="|") #sep on utilise sep quand on va replacer l'espace c'eta-à-dire le vergule dans python par quelque chose et c'est plus mieux que d'écrire hola bputaina sans nous utilise la vergule

#print('first line', end=" ") #end c'est pour remplacer enter car à la fin de chaque ligne on a enter = \n qui est invisible
#print('second line')


# ---------- Built in function part3 -------------------
# ------------------------------------------------------

# abs for countning the distance between 0 and your number (negative and positive number are simuler)

#print(abs(100))
#print(abs(-10.19))

# ------------------------------------------------------

#pow(base, exp, mod) => power = القوة أو الأس
print(pow(2, 5))  # 2*2*2*2*2 exp the number who is thz power howa num li ki kon fi loss
print(pow(2, 5, 10)) # (2*2*2*2*2) % 10 mod is the rest of the division of this number

print("#" * 50)

# -------------------------------------------------------
# min(item, item, item, iterator=(loop))
myNumbers = (1, 20, -50, -100, 100)
print(min(myNumbers))
print(min(1, 10, -50, 20, 30))
print(min("X", "Z", "Osama"))

print("#" * 50)

# max(item, item , item, or iterator)
myNumbers = (1, 20, -50, -100, 100)
print(max(1, 10, -50, 20, 30))
print(max("X", "Z", "Osama"))
print(max(myNumbers))

print("#" * 50)

# slice(start, end, step) is the same thing of a[:] but with using slice and colon not : (the most important the end is not including)
a = ["A", "B", "C", "D", "E", "F"]
print(a[:5])
print(a[slice(5)])
print(a[slice(2, 5, 2)])

print(f"- {a} -")
