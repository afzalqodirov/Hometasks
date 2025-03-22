check=[('a','d','g','j','m','p','s','v','y','.',' '),('b','e','h','k','n','q','t','w','z',','),('c','f','i','l','o','r','u','x','!')]
res=0

for i in input():
    if i in check[0]:res+=1
    elif i in check[1]:res+=2
    else:res+=3

print(res)
