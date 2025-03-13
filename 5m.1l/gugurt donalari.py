n=input()

def gugurt(n):
    result=0
    for i in n:
        if i=='1':result+=2
        elif i in ('0','9','6'):result+=6
        elif i in ('2','3','5'):result+=5
        elif i=='8':result+=7
        elif i=='7':result+=3
        else:result+=4
    return result
print(gugurt(n))
