# ----------------------------------------------------
# -- Practical => Loop on Many Iterators With Zip() --
# ----------------------------------------------------
# zip() Return A Zip Object Contains All Objects
# zip() Length Is The Length of Lowest Object
# ------------------------------------------------

list1 = [1, 2, 3, 4, 5]
list2 = ["A", "B", "C", "D"]
tuple1 = ("Man", "Woman", "Girl", "Boy")
dict1 = {"Name": "Osama", "Age": 36, "Country": "Egypt", "Skill": "Python"}

for item1, item2, item3, item4 in zip(list1, list2, tuple1, dict1):

    print("list 1 item =>", item1)
    print("list 2 item =>", item2)
    print("Tuple 1 item =>", item3)
    print("Dict 1 key =>", item4, "Value =>", dict1[item4])

ultimateList = zip(list1, list2)

print(ultimateList)

for item in ultimateList:
    print(item)