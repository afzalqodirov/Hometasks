class LimitedValue:
    def __set__(self,inst,value:float) -> None:
        if value in range(101):inst.val=float(value)
        else:raise ValueError('The number must be in range from 0 to 100 (both including)')

    def __get__(self,inst,owner) -> float:
        try:return inst.val
        except:pass
    
    def __delete__(self,inst) -> None:
        try:del inst.val
        except:print('it was already removed or wasn\'t created at all')

class Example:
    value=LimitedValue()

obj=Example()
print(obj.value)
obj.value=50
print(obj.value)
obj.value=150
