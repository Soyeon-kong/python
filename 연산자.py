#연산자 종류
#산술연산자, 비교연산자, 논리연산자

#산술 연산자 : + - * / % //(나눗셈 - 정수)
#비교 연산자: == != > <
#논리 연산자: and, or

id = "root"
pw = "1234"

id2 = input("아이디:")
pw2 = input("비밀번호:")

if id == id2 and pw ==pw2:
    print("로그인 성공")
else:
    print("로그인 실패")