from cls.basic_method_class import MethodClass

m = MethodClass(); # --> Obj variable

print( "Calling sparepart without Object: " , MethodClass.sparePartStatic())

print( "Calling sparepart with Object: " , m.sparePart())

print( "Calling without Object: " , MethodClass.noSelf())
