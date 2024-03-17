import random

lotto_num = [] # 빈 로또 번호 리스트 생성

def getRandomNumber():
    number = random.randint(1,45)
    return number

# for i in range(6): # 0 1 2 3 4 5
#     random_number = getRandomNumber()
#     print(random_number)

count = 0
while True:
    random_number = getRandomNumber() # 랜덤넘버 하나 구하기
    if random_number not in lotto_num: # 
        lotto_num.append(random_number)
        count = count+1

    if count ==6:
        break

print(lotto_num)

    


