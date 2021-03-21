from cls.basic_method_class import MethodClass

returnValue = MethodClass.sparePartStatic();

convertToString = str(returnValue)

print ('convertToString-->' + convertToString)

print( MethodClass.noSelfWithParam(convertToString) )
