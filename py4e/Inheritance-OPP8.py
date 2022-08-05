class Food: #Base Class

    def __init__(self, name, price):

        self.name = name

        self.price = price

        print(f"{self.name} is created from Base Class")

    def eat(self):

        print("Eat Method from Base Class")

class Apple(Food): #Derived Class

    def __init__(self, name, price, amount):

        #Food.__init__(self, name) #create instance From Base Class

        super().__init__(name, price)

        self.amount = amount

        print(f"{self.name} is created from derived class and Price is {self.price} and amount is {self.amount}")
    
    def get_from_tree(self):

        print("Get from tree from derived class")


#food_one = Food("Pizza")
food_two = Apple("Pizza", 150, 500)
food_two.eat()
food_two.get_from_tree()