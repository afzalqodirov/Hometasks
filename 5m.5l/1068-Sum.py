N=int(input())

if N>1:
  print(sum([i for i in range(1,N+1)]))
else:
  if N<1:
    print(sum([i for i in range(N,2)]))
  else:
    print(1)

