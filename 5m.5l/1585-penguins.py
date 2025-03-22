res={'a':'Emperor Penguin','b':'Macaroni Penguin','c':'Little Penguin'}

a=0
b=0
c=0

for i in range(int(input())):
    checking=input()
    if 'Emp' in checking:a+=1
    elif 'Mac' in checking:b+=1
    else:c+=1

result=[a,b,c].index(max(a,b,c))

if result==0:
    print(res['a'])
elif result==1:
    print(res['b'])
else:
    print(res['c'])
