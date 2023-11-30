import sqlite3 as sql
from tkinter import *
# import pandas as pd
from main import Main
import SignUp as su

# class Login:
#     def __init__(self, lP) -> None:
#         self.lP = lP
dbgen = sql.connect("DB/user.db")
dbcs = dbgen.cursor()

def logIn():
    userId = Id.get()
    userPW = pw.get()
    # 유저 테이블을 딕셔너리로 불러옴
    userTable = dict(dbcs.execute(f"select id, pw from userTable;"))
    # 유저 로그인 실패시
    if userId not in userTable.keys() or userTable[userId] != userPW:
        Lin_result.config(text="아이디 혹은 비밀번호가 잘못 되었습니다.")
    else:
        go_main()

def go_main():
    win = Toplevel()
    Main(win, Id.get())
    lP.withdraw()

def go_signUp():
    win = Toplevel()
    su.SignPage(win, Id.get())

lP = Tk()
lP.title("LogIn Page")

logo = PhotoImage(file="image/QWQ 2번 로고.png")
lo_label = Label(lP, image=logo)
lo_label.pack()

Idframe = Frame(lP)
pwFrame = Frame(lP)
Idframe.pack()
pwFrame.pack()

IdEX = Label(Idframe, width=10, height=2, font=('Arial'), text="ID")
pwEX = Label(pwFrame, width=10, height=2, font=('Arial'), text="PassWord")

Id = Entry(Idframe, textvariable=str, width=20, font=('Arial 18'))
pw = Entry(pwFrame, textvariable=str, width=20, font=('Arial 18'))

Lin_btn = Button(lP, text="Login", command=logIn, height=4, width=8)
Lin_result = Label(lP, text="아이디와 비밀번호를 입력하세요.",)

IdEX.pack(side=LEFT)
pwEX.pack(side=LEFT)
Id.pack(side=LEFT)
pw.pack(side=LEFT)
Lin_btn.pack(side=LEFT)
Lin_result.pack()

SignUpBtn = Button(lP, text="회원가입 하기", command=go_signUp, height=5)
SignUpBtn.pack(side=BOTTOM)

lP.mainloop()
dbgen.commit()
