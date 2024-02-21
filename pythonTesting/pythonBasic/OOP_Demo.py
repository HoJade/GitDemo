# "self" keyword is mandatory for calling variable(s) into method

class Calculator:
    num = 100           # class variable

    # default constructor
    def __init__(self, a, b):
        self.firstNumber = a        # firstNumber is the instance variable
        self.secondNumber = b
        print("I'm called automatically when object is created")

    def getData(self):
        print("I'm now executing as a method in class")

    def Summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num


# to call any method, have to create object of that class; obj = class(), then call that method with object.method()
obj = Calculator(2, 3)      # syntax to create object in python
obj.getData()
print(obj.num)
print(obj.Summation())

print("**********")

obj1 = Calculator(4, 5)
obj1.getData()
print(obj1.Summation())
