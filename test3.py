import random

# print(random.randint(0,10)) #0~10
# print(random.randrange(0,10)) #0~9
# print(random.choice(['가위','바위','보']))

person = []
random.seed(100)
sum = 0
for i in range(0,1000):
    score = []
    for x in range(0,5):
        score.append(random.randint(50,100))
    person.append(score)

print(person)

for p in person:
    sum += p[0]

print(sum/len(person))

#파일에 저장
file = open('total.txt','w')
for p in person:
    file.write(str(p)+"\n")

file2 = open('total.txt','r')

row = file2.readline().split(",")
print(type(row))
print(row)
person2 = list(row)
print(person2[1])

