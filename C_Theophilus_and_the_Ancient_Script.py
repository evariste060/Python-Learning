t = int(input())
for _ in range(t):
    n = int(input())
    count = 0
    characters = list(input())
    for i in range(n):
        min_i = i
        for j in range(i+1,n):
            if characters[min_i] == "A" and characters[j] == "B":
                min_i= j
                characters[i],characters[j] = characters[j],characters[i]
                count +=1
    print(count)
    