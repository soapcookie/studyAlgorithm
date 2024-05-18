# 500엔, 100엔, 50엔, 10엔, 5엔, 1엔
#
# cnt = 0 동전 최소개수
# price = 물건가격 입력받기
# change = [500,100,50,10,5,1]
# rest  = 1000에서 물건가격 뺀값
# change 리스트의 첫번째 값이랑 비교하면서 적을 경우 빼기 , cnt값 1씩 증가


price = int(input())
change = [500,100,50,10,5,1]
rest = 1000-price
cnt=0

while rest>0:
	for coin in change:
		while rest>=coin:
			rest-=coin
			cnt+=1
print(cnt)