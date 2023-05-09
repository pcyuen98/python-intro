# more example - https://www.w3schools.com/python/python_classes.asp

class BasicObjectClass:

    anIntTest = 0;

    def sparePart(self):
        x = self.anIntTest
        y = 1
        a = x + y
        return a;
    
    def sparePartWithParameter(self, y):
        a = self.anIntTest + y
        return a;
    
def main():
    m = BasicObjectClass(); # --> Obj variable
    m.anIntTest = 100;
    print ('BasicObjectClass sparePart-->', m.sparePart())
    print ('BasicObjectClass sparePartWithParameter-->', m.sparePartWithParameter(200))

if __name__ == "__main__":
    main()
