class Parent1:
    def __init__(self):
        self.name = "Inside Parent1"

    def show(self):
        print(self.name)

class Parent2:
    def __init__(self):
        self.name = "Inside Parent2"

    def show(self):
        print(self.name)

class Child(Parent1, Parent2):
    def __init__(self):
        Parent1.__init__(self)
        Parent2.__init__(self)

c = Child()
c.show()