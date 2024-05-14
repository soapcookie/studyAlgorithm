# 리스트로 풀기
# 원소 내림차순 정렬 시키기
# 3으로 나누고 가장 작은 원소는 제외하기
# 3으로 나누어지지 않는건 tot 증가하기

import sys
input=sys.stdin.readline

n=int(input())
sales=[]

for i in range(n):
  sales.append(int(input()))
sales.sort(reverse=True)

free=0
for i in range(2,len(sales),3):
  free+= free[i]

print(sum(sales)-free)