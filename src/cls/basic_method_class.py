# more example - https://www.w3schools.com/python/python_classes.asp

class MethodClass:
    
    anIntTest = 0; 
    
    @classmethod
    def sparePart(self):
        x = 1
        y = 1
        z = 1
        a = x + y + z

        return a;
         
    @classmethod    
    def printHelloWorld(self):  
        return "hello World from class"

    def noSelf():  # @NoSelf
        return "This is No Self"

    def noSelfWithParam(param):  # @NoSelf
        return "This is No Self with Parameter ===>" + param
    
    def getAnIntTest(self): 
        #print(self._str_)
        return self.anIntTest
