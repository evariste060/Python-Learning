t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    list_n = list(map(int,input().split()))
    list_m = list(map(int,input().split()))
    print(list_n)
    i = 0
    j = 0
    ouput = []
    while i < n and j < m:
        if list_n[i]< list_m[j]:
           ouput.append(list_n[i])
           i+=1
        else:
            ouput.append(list_m[j])
            j +=1
           
