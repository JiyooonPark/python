class FourCal:
    class_var = "Calculator" # every instance shars the same address
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def setdata(self, x, y):
        self.x = x
        self.y = y
    def add(self):
        return self.x+self.y
    def mul(self):
        return self.x*self.y
    def sub(self):
        return self.x-self.y
    def div(self):
        return self.x/self.y

#inherit class
class AdvancedFourCal(FourCal):
    def pow(self):
        return self.x ** self.y

#extends class
class SafeCal(FourCal):
    #overriding
    def div(self):
        if(self.y == 0):
            print("cannot divide by 0")
            return None
        else:
            return self.x/self.y

if __name__ == "__main__":
    a = FourCal(3,3)
    a.setdata(4, 2)
    print(a.add())
    print(a.mul())
    print(a.sub())
    print(a.div())

    b = AdvancedFourCal(5,6)
    print(b.pow())

    c = SafeCal(9,0)
    print(c.div())
