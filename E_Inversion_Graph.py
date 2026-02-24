
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    comp = 0
    cur = 0
    for i, val in enumerate(arr, start=1):
        if val > cur:
            cur = val
        if cur == i:
            comp += 1
    print(comp)



