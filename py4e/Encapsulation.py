class Member:

    def __init__(self, name):

        self.name = name #Public

one = Member("Boutaina")
#print(one.name)
one.name = "Jamila"
#print(one.name)

class Member:

    def __init__(self, name):

        self._name = name #Protected

one = Member("Boutaina")
#print(one._name)
one._name = "Jamila"
#print(one._name)

class Member:

    def __init__(self, name):

        self.__name = name #Private 

    def say_hello(self):

        return f"Hello {self.__name}"

one = Member("Boutaina")
print(one.say_hello())
print(one._Member__name)


