data = []
sum = 0
#0. 데이터 입력받아서 리스트에 넣기
for i in range(0,3):
    num = int(input("숫자 입력: "))
    data.append(num)
    sum += num
#1. 데이터 출력(for)
for i in range(0,3):
    print(data[i])
#for-each
for d in data:
    print(d, end=' ')
#2. 데이터 더해서 출력
print("총합은 " + str(sum))
#3. 짝수만 프린트
for i in data:
    if i % 2 == 0:
        print(i)