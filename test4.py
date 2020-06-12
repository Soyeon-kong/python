#1. 임의로 지정한 숫자를 맞추는 게임
import random

random.seed(100)
ans = random.randint(0,100)
while True:
    i = int(input("숫자를 입력하세요(0부터 100까지)>> "))
    if i == ans:
        print("정답입니다")
        break
    elif i < ans:
        print("너무 작아요")
    else:
        print("너무 커요")
#2. 극장예매시스템(10자리 예매)
print("-------------------")
print("극장 예매 시스템입니다")
print("0: 예매 가능, 1: 예매 완료")
seat = [0]*10
while True:
    print("좌석번호: 1 2 3 4 5 6 7 8 9 10")
    print("예매상태: ",end=" ")
    for i in seat:
        print(i, end=" ")
    print("\n")
    num = input("예매할 좌석의 번호를 입력해주세요(예매 종료: x)>>")
    if num == 'x' or num =='X':
        print("예매 시스템을 종료합니다")
        break
    elif 1<=int(num) and int(num) <=10:
        seat[int(num)-1] = 1
    else:
        print("잘못된 입력입니다")


