numbers = [1,2,3,4,5]*2
print(numbers)

numbers2 = [0]*5
print(numbers2)

numbers3 = [11.1, 22.2, 33.3, 44.4, 55.5]
numbers4 = list(map(int, numbers3))
print(numbers4)
data2= input("숫자 여러개 입력>> ").split()
data = list(map(int, data2))
print(data)