#리스트 생성

animals = ["사자","호랑이","토끼","악어"]

#인덱스 / 데이터 접근하기
name = animals[0]

# print(name)

# 데이터 추가

animals.append("하마")
animals.append(1)

# print(animals)

# 데이터 삭제하기

del animals[-1]

#리스트 슬라이싱
# 시작 : 끝 +1

slicing = animals[1:3]

print(slicing)

length = len(animals)

print(length)

animals.sort()

print(animals)

animals.sort(reverse=True)

print(animals)

for a in animals:
    print(a)