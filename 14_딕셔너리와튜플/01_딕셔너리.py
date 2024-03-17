# 1. 승패여부
# 2. 챔피언 이름
# 3. 킬
# 4. 데스
# 5. 어시스트

# 변수를 사용할 때

result = '승리'
champ_name = '비에고'
kill = 15
death = 4
assist = 7

#리스트 사용할 때
play_data = ['승리', '비에고', 15,4,7]

# 딕셔너리 사용할 때

play_data = {
    'result' : '승리',
    'champ_name' : '비에고',
    'kill' : 15,
    'death' : 4,
    'assist' : 7
}

# keys()
for key in play_data.keys():
    print(key)

for value in play_data.values():
    print(value)


# items()
    
for key, value in play_data.items():
    print(key, value)