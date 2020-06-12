from tkinter import *

#1. 파티
yesterday = {'홍길동', '박길동', '김길동'}
today = {'홍길동', '정길동', '이길동'}

for y in yesterday:
    print(y, end=' ')
print()
for t in today:
    print(t, end = ' ')
print()
print("모두 참석한 사람: ", yesterday.intersection(today))
print("어제 오늘 참석한 사람: ", yesterday.union(today))
print(len(yesterday.union(today)))
print()
#2. 사과
sentence = input("문장을 입력>> ")
print('전체 글자 수: ',len(sentence),'자')

word = sentence.split(' ')
print('단어 수: ',len(word),'단어')
print('전체 단어:')
for w in word:
    print(w+' ',len(w),'글자')
print()
#3. 인기투표
print("인기투표 시스템")
print("----------------")
print("1)아이유 2)BTS 3)유재석 4)종료")
print("----------------")
count = {'아이유':0, 'BTS':0, '유재석':0}
while True:
    number = int(input("입력>> "))
    if number == 1:
        count['아이유'] += 1
    elif number == 2:
        count['BTS'] += 1
    elif number == 3:
        count['유재석'] += 1
    elif number == 4:
        break
    else:
        continue
print(count)
for c in count:
    print(c+': '+str(count[c])+'표')
print()
#4. 파일 입출력
w = Tk()
w.geometry('200x100')
w.config()
fruit = ['apple','banana','melon']
def file_write():
    file1 = open('fruit.txt','w')
    for f in fruit:
        file1.write(f+" ")
def file_read():
    file2 = open('fruit.txt','r')
    row = file2.readline().split(' ')
    for r in row:
        print(r)
fruit_label = Label(w, text='과일: apple, banana, melon')
fruit_label.pack()
button1 = Button(w,text='파일에 저장',command=file_write)
button1.pack()
button2 = Button(w,text='파일 읽기',command=file_read)
button2.pack()

w.mainloop()


