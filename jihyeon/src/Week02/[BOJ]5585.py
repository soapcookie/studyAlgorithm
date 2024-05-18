# 인풋받음
# 1000 - 인풋받은 돈의 잔돈
# 500엔 잔돈수 = 인풋/500의 몫
# 100엔 잔돈 = 500엔 잔돈/100의 나머지의 몫
# 잔돈3 = 잔돈2/

# 리스트 정렬 = [500, 100, 50, 10, 5, 1]

# 리스트로 순서대로 나눈다
# for 리스트개수 in range:
# 	나머지 = 동전

N = int(input())
rest = 1000 - N #620
result = 0
count = 0

coins = [500, 100, 50, 10, 5, 1]

for coin in coins:
    count = rest // coin #몫
    result +=count
    rest %= coin

    #rest = rest - (rest % coin)


print(result)