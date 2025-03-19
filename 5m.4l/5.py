class Temperature:
    def __set__(self,inst,val):
        inst.selsiy=val

    def __get__(self,inst,owner):
        return inst.selsiy*9/5+32

class Weather:
    temp=Temperature()

w=Weather()
w.temp=25
print(w.temp)
