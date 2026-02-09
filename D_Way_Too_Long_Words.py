n = int(input())
strs = [input().strip() for _ in range(n)]
for st in strs:
    if len(st) > 10:
        print(st[0] + str(len(st) - 2) + st[-1])
    else:
        print(st)