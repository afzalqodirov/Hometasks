n=int(input())
l1=list(map(int,input().split()))

def uchburchak(l :list,i: int=0):
    a=l[-3+i]
    b=l[-2+i]
    c=l[-1+i]
    if a+b>c and a+c>b and b+c>a:
        return f'{a} {b} {c}'
    elif len(l)==3+(-i):
        return -1
    else:
        i-=1
        return uchburchak(l,i)
        

print(uchburchak(sorted(l1)))
