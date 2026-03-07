t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    size = len(arr)
    if size % 2 == 1:
        portion = size // 2
        if sum(arr[0:portion]) > sum((arr[portion:])):
            print('YES')
        else:
            print('NO')
    else:
        portion = int(size / 2 - 1)
        if sum(arr[0:portion]) > sum((arr[portion:])):
            print('YES')
        else:
            print('NO')

