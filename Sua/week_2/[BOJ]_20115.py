#1. 내림차순 정렬
#2. 첫번째 수 + 나머지 수들의 2분의 1 더하기

n = int(input())
li = list(map(int, input().split()))
li.sort(reverse=True)
print(li[0]+sum(li[1:n])/2)
