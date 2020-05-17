b=int(input())
for o in range(1,b+1):
    xl=int(input())
    L=[int(x) for x in input().split()]
   
   
    a=[1 for i in range(0,len(L)) for j in range(1,len(L)-i+1) if  sum(L[i:i+j])**.5==int(sum(L[i:i+j])**.5)]
    print("Case #"+str(o)+": "+str(len(a)))