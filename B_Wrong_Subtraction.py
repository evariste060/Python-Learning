# n,k = map(int, input().split())
# my_list = list(str(n))
# for i in range(k):
#     if( not int(my_list[-1])==0):
#         n-=1
#         my_list = list(str(n))
#     else:
#         n//=10
#         my_list = list(str(n))
# print(n)
n,k = map(int,input().split())

while k:
    if n%10:
        n -= 1
    else:
        n//=10
    k-=1

print(n)