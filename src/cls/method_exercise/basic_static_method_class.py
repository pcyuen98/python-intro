# more example - https://www.w3schools.com/python/python_classes.asp

class StaticMethodClass:

    @staticmethod 
    def sparePartStatic():
        x = 1
        y = 1
        a = x + y
        return a;
    
    @staticmethod 
    def sparePartStaticWithParameter(x):
        y = 1
        a = x + y
        return a;
    
def main():
    print ('main StaticMethodClass sparePartStatic-->', StaticMethodClass.sparePartStatic())
    print ('main StaticMethodClass sparePartStaticWithParameter-->', StaticMethodClass.sparePartStaticWithParameter(200))

if __name__ == "__main__":
    main()
