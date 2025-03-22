tick_num = input()

if abs(sum(map(int, tick_num[:3])) - sum(map(int,tick_num[3:]))) in (0,1):print('Yes')
else:print('No')
