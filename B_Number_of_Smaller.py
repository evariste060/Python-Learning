n,m = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
j=0
res=[]
i =0
while j<m:
    while i<n and A[i]<B[j]:
        i+=1
    res.append(i)
    j+=1
print(*res)
    

   
