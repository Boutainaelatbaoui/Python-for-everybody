class Member:

    not_allowed_name = ["Hell", "Shit", "Baloot"]

    users_num = 0

    @classmethod
    def show_users_count(cls):
        print(f"We Have {cls.users_num} Users In On System.")

    @staticmethod
    def say_hello():
        print("Hello from static method")

    def __init__(self, first_name, middle_name, last_name, gender):

        self.fname = first_name

        self.mname = middle_name

        self.lname = last_name 

        self.gender = gender

        Member.users_num += 1 # Member.users_num = Member.users_num +1

    def full_name(self):
        if self.fname in Member.not_allowed_name :
            raise ValueError("Name Not Allowed")
        else:
            return f"{self.fname} {self.mname} {self.lname}"

    def name_with_title(self):
        if self.gender == "Male":
            return f"Hello Mr {self.fname}"
        elif self.gender == "Female":
            return f"Hello Miss {self.fname}"
        else:
            return f"{self.fname}"

    def get_all_info(self):
        return f"{self.name_with_title()}, Your Full Name Is: {self.full_name()}"
    
    def delete_user(self):

        Member.users_num -= 1

        return f"User {self.fname} is deleted."


print(Member.users_num)
member_one = Member("Boutaina", "d", "a", "Female")
member_two = Member("Jamila", "r", "b", "Female")
member_three = Member("Hassan", "c", "t", "Male")
member_four = Member("Shit", "Hell", "Metal", "DD")
print(Member.users_num)
print(member_four.delete_user())
print(Member.users_num)

#print(member_one.fname, member_one.mname, member_one.lname)
#print(member_two.fname)
#print(member_three.lname)

#print(member_one.full_name())
#print(member_three.name_with_title())
#print(member_one.get_all_info())

print("#" * 50)

Member.show_users_count()

print("#" * 50)

Member.say_hello()