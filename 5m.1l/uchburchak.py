n=int(input())
l1=list(map(int,input().split()))

def uchburchak(l :list):
    l.sort()
    a=l[-3]
    b=l[-2]
    c=l[-1]
    if a+b>c and a+c>b and b+c>a:
        return a,b,c
    else:
        return -1