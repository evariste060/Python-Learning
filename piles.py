def maxCoins(piles):
    piles.sort()
    i = 0
    j = len(piles)
    res = 0
    while i<j:
        i+=1
        j-=2
        res+=piles[j]
    return res    
print(maxCoins([9,8,7,6,5,1,2,3,4]))
print(maxCoins([2,4,1,2,7,8]))