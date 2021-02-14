# more example - https://www.w3schools.com/python/python_classes.asp

class MethodClass:
    
    anIntTest = 0; 
    
    def sparePart(self):
        x = 1
        y = 1
        z = 1
        a = x + y + z
        print(self.anIntTest)
        return a;         
  
    def printHelloWorld(self):  
        return "hello World from class"

    def noSelf():  # @NoSelf
        return "This is No Self"

    def noSelfWithParam(param):  # @NoSelf
        return "This is No Self with Parameter ===>" + param
    
    def getAnIntTest(self): 
        return self.anIntTest

# https://www.programiz.com/python-programming/methods/built-in/classmethod
    @classmethod  
    def getAnIntTestWithClassMethod(self): 
        return self.anIntTest
    
    @staticmethod  
    def getAnIntTestWithStaticMethod(num): 
        return num + 1