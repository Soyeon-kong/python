name = []
for i in range(0,5):
    name.append(input("신입 이름 입력>> "))
tuple(name)
print(name)
print("\n")
#name[0]='김다인'

computer = [{'id':'100','subject':'파이썬','class':'708','money':2000},
{'id':'100','subject':'자바','class':'709','money':3000},
{'id':'200','subject':'소켓','class':'709','money':5000}]
sum = 0
for c in computer:
    print(c)
    if(c['id']=='100'):
        sum = sum+c['money']

print("id가 100인 사람의 총 수강료는 "+str(sum)+"원")
