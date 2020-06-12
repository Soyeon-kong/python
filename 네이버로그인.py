from tkinter.messagebox import *
from tkinter import *

def check():
    #입력값 가지고 오기
    #회원가입시의 데이터와 비교 인증
    get_id = id_text.get()
    get_pw = pw_text.get()
    showinfo('당신이 입력한 id는 ',get_id)
    showinfo('당신이 입력한 pw는 ',get_pw)

#showinfo("반갑습니다")
w = Tk()
w.geometry('500x400')
w.config(bg='lime')

id_label = Label(w, text = '사용자 ID입력', font =('맑은 고딕',30), bg='lime', fg='blue')
pw_label = Label(w, text = '사용자 PW입력', font =('맑은 고딕',30), bg='lime', fg='blue')

id_text = Entry(w, font =('맑은 고딕',30), bg='yellow', fg='red')
pw_text = Entry(w, font =('맑은 고딕',30), bg='yellow', fg='red')
id_label.pack()
pw_label.pack()
id_text.pack()
pw_text.pack()

icon = PhotoImage(file='naver.png')
button = Button(w, image = icon, command = check)
button.pack()

w.mainloop()

