from OOP_Demo import Calculator     # import parent class


class ChildImplementation(Calculator):      # class childClass(parentClass)
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 2, 10)

    def getCompleteData(self):
        # can use "self." to call the class variable
        return ChildImplementation.num2 + self.num + self.num2 + self.Summation()


obj = ChildImplementation()
print(obj.getCompleteData())
