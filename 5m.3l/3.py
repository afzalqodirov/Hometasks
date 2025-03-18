class CachedPropertyDescriptor:
    def __init__(self):
        print('The object was created')

    def __get__(self,inst,owner):
        try:
            return inst.val
        except:pass
            

    def __set__(self,inst,val):
        if type(val)!=str:
            inst.val=val
            return
        raise Exception('Invalid expression was given')

    def __delete__(self,inst):
        del inst.val

class ToCheck:
    solution=CachedPropertyDescriptor()

first=ToCheck()
first.solution=3*4*5+5*6*7+8/2+4
print(first.solution)

second=ToCheck()
second.solution=3*'a'
