str='가나다라마바사'

print(str[4:6])

str2='50,60,70,80,90'
str2_list = str2.split(",")
print(str2_list)

str3='100:200:300:400:500'
str3_list = str3.split(":")
sum = 0
for i in str3_list:
    sum += int(i)
print(sum)

int3_map = map(int, str3_list)
print(type(int3_map))
int3_list = list(int3_map)
print(int3_list)