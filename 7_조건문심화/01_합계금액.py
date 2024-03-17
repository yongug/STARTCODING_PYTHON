# 1. 사용자로부터 가방, 시계 금액 입력받기
# 2. 합계금액 10만원 이상 할인률 30%, 5~10만원 할인률 20%, 5만원 미만 할인률 10%
# 3. 합계금액 할인률 적용하여 출력

bag = int(input("가방 가격을 입력하세요 >>"))
watch = int(input("시계 가격을 입력하세요 >>"))
init_total_price = bag + watch

print("총 합계 금액은 다음과 같습니다.")
if init_total_price >=100000:
    print(str(init_total_price * 0.7) +"원")
elif init_total_price>=50000:
    print(str(init_total_price*0.8) +"원")
else:
    print(str(init_total_price*0.9) +"원")