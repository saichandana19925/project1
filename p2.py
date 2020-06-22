n=int(input())
arr=list(map(int,input().split()))
l=[]
l2=[]
for i in arr:
    l.append(i)
    l2.append(0)
#print(l)
l1=[]
l1=sorted(l)
c=1
for i in range(1,n+1):
    k=0
    #print(l1)
    for j in l:
        l2[j-1]=l1[k]
        k=k+1
    c=c+1
    #print(l2)
    l3=sorted(l)
    if(l2==l3):
        print(c)
        break
    else:
        l1=l2.copy()