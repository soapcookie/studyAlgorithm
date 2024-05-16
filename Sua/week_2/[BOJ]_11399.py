n= int(input())
waiting = list(map(int,input().split()))

waiting.sort()
ans=0

for i in range(0,n+1):
    ans+=sum(waiting[0:i])

print(ans)
