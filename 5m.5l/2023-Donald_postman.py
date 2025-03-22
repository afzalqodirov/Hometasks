
positions = [('A','P','O','R'),('B','M','S'),('D','G','J','K','T')]
curr_pos = 'A'
s=0
result=0

for i in range(int(input())):
    curr_pos=input()[0]
    if curr_pos in positions[0]:
        result+=abs(0-s)
        s=0
    elif curr_pos in positions[1]:
        result+=abs(1-s)
        s=1
    else:
        result+=abs(2-s)
        s=2

print(result)
