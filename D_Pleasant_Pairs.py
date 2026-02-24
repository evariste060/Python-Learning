t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    count = 0
    for i, c in enumerate(arr, start=1):
        max_k = (2 * n) //c
        for k in range(1, max_k + 1):
            j = k * c - i
            if j > i and j <= n and arr[j - 1] == k:
                count += 1

    print(count)





        

        

    