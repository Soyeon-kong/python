#콜렉션의 4가지
#리스트, 튜플, 딕셔너리, 셋

#person = ('홍길동',100,'mega') => row(레코드)

person = ('홍길동',100,'mega')
print(person)

#person[0]='김길동'
#바꿀수 없음

person2 = list(person)
person2[0]='김길동'
print(type(person2))

person3=tuple(person2)
print(type(person2))

me=dict()
me['name'] = 'hong'
me['age'] = 100
me['company'] = 'mega'
print(me)
print('이름은 '+me['name'])
del me['company']
print(me)

for x in me: #x는 key
    print(me[x])