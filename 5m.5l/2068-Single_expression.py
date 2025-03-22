a=int(input())
b=int(input())
c=int(input())
for_check=[a+b-c,a+b*c,a+b+c,a-b+c,a-b*c,a-b-c,a*b+c,a*b-c,a*b*c]
print(min(for_check))

