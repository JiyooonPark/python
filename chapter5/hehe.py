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
