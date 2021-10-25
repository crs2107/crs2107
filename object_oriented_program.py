class Phone : #when you are defining a class the name should starts with a capital letter
    
    def make_call(self):
        print("Making a call")

    def play_game(self):
        print("playing a game")

    def add_color(self,color):
        self.color = color

    def add_cost(self,cost):
        self.cost = cost

    def show_color(self):
        print(self.color)

    def show_cost(self):
        print(self.cost)


p1 = Phone()

p1.make_call()

p1.add_color("black")

p1.show_color()

p1.add_cost("20,000")

p1.show_cost()


class Iphone(Phone):

    def security(self):
        print("I am very secure")

ip2 = Iphone()

ip2.add_color("rose gold")

ip2.show_color()

ip2.security()

