def koshi(a,b):
    c=(a+b)/2
    d=(a*b)**0.5
    if c>d:
        print('>')
    elif c<d:
        print('<')
    else:
        print('=')