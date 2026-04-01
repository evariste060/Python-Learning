n,m = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
i = 0
j = 0
current = 0
merged = []
while i<n and j<m:
    if A[i]<B[j]:
        merged.append(A[i])
        i+=1
    else:
        merged.append(B[j])
        j+=1
merged.extend(A[i:])
merged.extend(B[j:])
print(*merged)


    
