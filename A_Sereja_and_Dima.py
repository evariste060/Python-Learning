n = int(input())
cards = list(map(int,input().split()))
sereja = 0
dima = 0
sorted_cards = sorted(cards)
for _ in range(len(cards)):
    if len(sorted_cards)>0:
        sereja += sorted_cards.pop()
    if len(sorted_cards)>0:
        dima += sorted_cards.pop()
result = [sereja,dima]
print(*result)
