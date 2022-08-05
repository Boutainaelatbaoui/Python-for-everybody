# ------------------------
# -- Built In Functions --
# ------------------------
# enumerate()
# help()
# reversed()
# ------------------------

# enumerate(iterable, start=0)
mySkills = ["Html", "Css", "Js", "PHP"]
mySkillsWithCounter = enumerate(mySkills, 1)
print(type(mySkillsWithCounter))
for counter, skill in mySkillsWithCounter:
    print(f"{counter} - {skill}")

print("#" * 50)

# help()
print(help("keywords"))

print("#" * 50)

# reversed(iterable)
myString = "Elzero"
print(list(reversed(myString)))

for letter in reversed(myString):
    print(letter)

for skill in reversed(mySkills):
    print(skill)
