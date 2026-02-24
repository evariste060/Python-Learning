t = int(input())
for x in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    no = set(arr)
    print(len(no))