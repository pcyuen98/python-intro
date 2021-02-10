from cls.basic_method_class import MethodClass

print( "Calling sparepart without Object variable: " , MethodClass.sparePart())

print( "Calling without Object variable: " , MethodClass.noSelf())

print( "Calling without Object variable with Param: " , MethodClass.noSelfWithParam('param'))