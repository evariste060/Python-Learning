import copy
n = int(input())
number = list(map(int,input().split()))
number1 = copy.deepcopy(number)
m = int(input())
queries = list(map(int,input().split()))
count1 = 0

for x in queries:
    for y in number:
        if x != y:
            count1+=1
        else:
            count1+=1
            break

count2 = 0
number1.reverse()
for x in  queries:
    for y in number1:
        if x != y:
            count2+=1
        else:
            count2+=1
            break

print(count1, count2)