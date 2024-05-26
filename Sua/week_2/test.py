t = int(input())
li=[]
ans = 0
for test_case in range(1,t+1):
    n,k = map(int,input().split())
    li = list(map(int,input().split()))
    print("#"+str(test_case),str(ans))
