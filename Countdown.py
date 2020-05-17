a=int(input())

def g(b,n,k):
    count=0
    c=[int(x) for x in range(k,0,-1)]
    for e in range(n-k+1):
        r=b[e:e+k]
        if r==c:
            count=count+1
    return count
        
for i in range(1,a+1):
    n,k=map(int,input().split())
    b=[int(x) for x in input().split()]
    
    d=g(b,n,k)
    print("Case #"+str(i)+": "+str(d))