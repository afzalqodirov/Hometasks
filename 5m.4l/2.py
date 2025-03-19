
class NameDescriptor:
    def __set__(self, inst, value: str):
        if all(x.isalpha() for x in value):inst.fname=value
        else:raise ValueError('Error! The given value must have contained only letters! not number nor any special character')

    def __get__(self, inst, owner):
        try:return inst.fname
        except:pass

    def __delete__(self, inst):
        try:del inst.fname
        except:print('it was deleted already or wasn\'t created at all')

class Person:
    name=NameDescriptor()

p=Person()
p.name='Afzal'
print(p.name)
s=Person()
s.name='Afzal01'
