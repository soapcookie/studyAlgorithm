# 거스름돈 = N, 동전 최소 개수 = cnt
# 2원과 5원이 있으므로 5로 제일 먼저 나누기
# 5로 나누어지지 않을 경우 2로 나누기
# 2로도 나누어지지 않을 경우 -1 출력(예외처리)

import sys
input=sys.stdin.readline

N = int(input())
cnt=0

while N > 0:
    if N % 5 == 0:
        cnt += N // 5
        break #5로 나누어떨어지는 5의 배수라면 5로 나눈 횟수 출력
    else:
        N -= 2 #5로 나누어지지 않는 값 ex)4라면 계속 2를 빼기
        cnt += 1 #동전 갯수 증가

if N < 0:
    print(-1) #2로 나누어서 0이 되어버리면 -1 출력
else:
    print(cnt)

