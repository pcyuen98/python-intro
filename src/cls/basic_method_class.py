class MethodClass:
    
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
        return "This is No Self with Param," + param