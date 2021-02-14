from cls.basic_method_class import MethodClass

m = MethodClass(); # --> Obj variable

m.anIntTest = 1;

print( "m anIntTest: " , m.getAnIntTest())
print( "m getAnIntTest   With  ClassMethod   : " , m.getAnIntTestWithClassMethod())
print( "m getAnIntTest   With  StaticMethod  : " , m.getAnIntTestWithStaticMethod(1))

del m