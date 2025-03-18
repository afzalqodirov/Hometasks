class TaxedPriceDescriptor:
    def __set__(self,inst,val):
        inst.val=val
        inst.with_tax=val*1.15
        print('the value is set')
        return

    def __get__(self,inst,owner):
        try:return f'original price {inst.val}'
        except:pass

    def __delete__(self,inst):
        try:del inst.val, inst.with_tax
        except:print('it doesn\'t exist')


class Price:
    price=TaxedPriceDescriptor()
    
    def get_total_price(self):
        try:return f'The total price is {self.with_tax}'
        except:return 'it was deleted or wasn\'t existed at all'

first=Price()
first.price=40
print(first.price)

del first.price

print(first.get_total_price())
