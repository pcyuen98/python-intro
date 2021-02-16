from cls.basic_method_class import MethodClass

print( "Calling sparepart without Object variable: " , MethodClass.sparePartStatic())

print( "Calling without Object variable: " , MethodClass.noSelf())

print( "Calling without Object variable with Param: " , MethodClass.noSelfWithParam('param'))