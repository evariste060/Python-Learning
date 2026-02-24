
t = int(input())
for x in range(t):
    n = int(input())
    y,r = list(map(int,input().split()))
    suspended_red = min(r,n)
    remaining_players = n - suspended_red
    suspended_yellow = min(y//2,remaining_players)
    print(suspended_red + suspended_yellow)
    

    
 