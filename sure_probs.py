n = int(input())

probs = [list(map(int, input().split())) for _ in range(n)]

count = 0
for prob in probs:

    if sum(prob) >= 2:
        count += 1


print(count)