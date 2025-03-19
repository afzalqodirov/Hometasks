class UpperCaseDescriptor:
    def __set__(self, inst, value:str) -> None:
        if type(value)==str:inst.txt=value.upper()
        else:raise ValueError('Invalid Value')
    
    def __get__(self,inst,owner) -> str:
        try:return inst.txt
        except:pass

class Message:
    text=UpperCaseDescriptor()

msg=Message()
msg.text='Today is my birthday! Can somebody congratulate me with that?'
print(msg.text)
