class PasswordDescriptor:
    def __init__(self):
        print(f'the object was created')
    
    def __get__(self,instance,owner):
        pass

    def __set__(self,instance,value):
        if instance:
            try:
                instance.password=hash(value)
                print('Your password is saved!')
                return
            except Exception as e:
                print(e)
                return
        raise Exception("Where's the object???")

    def __delete__(self,instance):
        try:
            del instance.password
            print('The object was successfully deleted')
        except:
            print('it was already deleted or it wasn\'t existed')


class ToCheck:
    pasw=PasswordDescriptor()

    def check_pass(self,two):
        return self.password==hash(two)

first=ToCheck()
first.pasw='12345678'

print(first.check_pass('12345678'))
