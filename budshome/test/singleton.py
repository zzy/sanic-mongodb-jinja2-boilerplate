#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Singleton:
    __instance=None
    
    def __new__(cls, *args, **kwd):
        if Singleton.__instance is None:
            print(u'Create MotorObj instance')
            Singleton.__instance = object.__new__(cls, *args, **kwd)
            
        return Singleton.__instance
    
    @property
    @staticmethod
    def destroy(self):
        Singleton.__instance = None
        print(u'destroy MotorObj instance')
        
    @property
    def test(self):
        print('1111111111111')
    

Singleton().test

instance1 = Singleton()
instance2 = Singleton()
instance3 = Singleton()
instance4 = Singleton()
instance5 = Singleton()
instance6 = Singleton()

print(id(instance1))
print(id(instance2))
print(id(instance3))
print(id(instance4))
print(id(instance5))
print(id(instance6))

print(instance6==instance2)
print(instance1==instance5)


Singleton.__instance = None
Singleton.destroy


instance1.test

instance1 = Singleton()
instance2 = Singleton()
instance3 = Singleton()
instance4 = Singleton()
instance5 = Singleton()
instance6 = Singleton()

del  instance1
print(id(instance1))
print(id(instance2))
print(id(instance3))
print(id(instance4))
print(id(instance5))
print(id(instance6))

print(instance6==instance2)
print(instance1==instance5)
