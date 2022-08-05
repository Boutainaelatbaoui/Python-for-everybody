class skill:

    def __init__(self):

        self.skills = ["Html", "Css", "Js"]

    def __str__(self):

        return f"This is My Skills => {self.skills}"

    def __len__(self):

        return len(self.skills)
    
profile = skill()
print(profile)
print(len(profile))

profile.skills.append("PHP")
profile.skills.append("MySQL")

print(len(profile))

#print(skill())
#print(profile.__class__)
my_string = "Boutaina"
#print(type(my_string))
#print(my_string.__class__)
#print(str.upper(my_string))
