class Base1(object):
    def __init__(self):
        super(Base1, self).__init__()
        print("Base1 Class")

class Base2(object):
    def __init__(self):
        super(Base2, self).__init__()
        print("Base2 Class")

class Derived(Base1, Base2):
    def __init__(self):
        super(Derived, self).__init__()
        print("Derived Class")

D = Derived()