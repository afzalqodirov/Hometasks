class AgeDescriptor:
    def __init__(self):
        print('The object was created')

    def __set__(self,inst,age:int):
        if type(age)==int and 0<age<120:
            inst.age=age
            return
        raise ValueError('The age must be integer!')

    def __delete__(self,inst):
        inst.age=0

    def __get__(self,inst,owner):
        result='age = '
        try:result+=str(inst.age)
        except: result+='0'
        return result

class AgeData:
    person=AgeDescriptor()

first=AgeData()

print(first.person)

first.person=99
print(first.person)

del first.person
print(first.__dict__)
