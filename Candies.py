a=int(input())
def su(t):
    s=0
    d=[int(x) for x in range(1,len(t)+1)]
    for o in range(0,len(d),2):
        s=s+d[o]*t[o]
    for n in range(1,len(d),2):
        s=s+d[n]*t[n]*-1
    return s    
def ti(d):
    e=0
    for j in range(c):
        r=[x for x in input().split()]
        w=[r[0],int(r[1]),int(r[2])]
        w1=w[1]-1
        w2=w[2]
        if r[0]=="Q":
            e=e+su(d[w1:w2])
        elif r[0]=="U":
            d[w1]=w2
        else:
            pass
    return e
for i in range(1,a+1):
    b,c=map(int,input().split())
    d=[int(x) for x in input().split()]
    
    t=ti(d)
    print("Case #"+str(i)+": "+str(t))