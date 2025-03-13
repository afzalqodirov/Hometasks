l1=list(map(int, input().split()))
def koshi(a,b):
    c=(a+b)/2
    d=(a*b)**0.5
    if c>d:
        return '>'
    elif c<d:
        return '<'
    else:
        return '='
  
print(koshi(l1[0],l1[1]))
