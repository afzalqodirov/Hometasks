class PhoneNumberDescriptor:
    def __init__(self) -> str:
        print(f'The object was created')

    def __get__(self,instance,owner) -> str:
        if instance:
            try:
                a=instance.number
                print(f'+998 ({a[4:6]}) {a[6:9]}-{a[9:11]}-{a[11:]}')
                return 
            except Exception as e:
                print(e)
                print('the number doesn\'t exist')
                return
        return

    def __set__(self,instance,value:str) -> str:
        if type(value)==str and value.startswith('+998') and len(value)==13 and '+'+''.join(filter(lambda x:x.isdigit(),value))==value:
            instance.number=value
            print('The number is saved')
            return
        raise ValueError('invalid value was given')
    
    def __delete__(self,instance) -> str:
        try:
            del instance.number
            print(f'The number was successfully removed')
            return
        except Exception as e:
            print(e)
            return

class ToCheck:
    customer=PhoneNumberDescriptor()

first=ToCheck()
first.customer='+998900967069'
first.customer

second=ToCheck()
second.customer='+12312'
