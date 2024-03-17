# 함수를 사용하지 않는 경우

print("안녕하세요 민수 회원님 ")
print("현재 구독 서비스 사용 기간이 30일 남았습니다.")

print("안녕하세요 경수 회원님 ")
print("현재 구독 서비스 사용 기간이 15일 남았습니다.")

print("안녕하세요 다혜 회원님 ")
print("현재 구독 서비스 사용 기간이 7일 남았습니다.")


def print_message(name,date):
    print("안녕하세요. ",name,"회원님")
    print("현재 구독 서비스 사용 기간이 ",date,"일 남았습니다.")
    print()


print_message("민수",30)
print_message("경수",15)
print_message("다혜",7)