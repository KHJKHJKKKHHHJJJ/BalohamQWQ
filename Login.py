import sqlite3 as sql
from tkinter import *
# import pandas as pd
from main import Main
import SignUp as su

''' * 중요 *
테스트 할 때 아이디 하나 만들고 해야함
회원가입으로 하나 만들고 할 것.
'''


# DB 불러옴 (DB파일 안에 있음)
dbgen = sql.connect("DB/user.db")
dbcs = dbgen.cursor()

# 로그인 버튼 함수
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

# 메인메뉴로 이동하는 함수
def go_main():
    win = Toplevel()
    Main(win, Id.get())
    lP.withdraw()

# 회원 가입으로 이동하는 함수
def go_signUp():
    win = Toplevel()
    su.SignPage(win, Id.get())

# loginPage 로 Tk() 불러옴
lP = Tk()
lP.title("LogIn Page")

# 로고 불러옴
logo = PhotoImage(file="image/QWQ 2번 로고.png")
lo_label = Label(lP, image=logo)
lo_label.pack()

# Id, Pw 입력창, 텍스트 담을 프레임 생성
Idframe = Frame(lP)
pwFrame = Frame(lP)
Idframe.pack()
pwFrame.pack()
# Id, Pw 텍스트 생성
IdEX = Label(Idframe, width=10, height=2, font=('Arial'), text="ID")
pwEX = Label(pwFrame, width=10, height=2, font=('Arial'), text="PassWord")
# Id, Pw 입력창 생성
Id = Entry(Idframe, textvariable=str, width=20, font=('Arial 18'))
pw = Entry(pwFrame, textvariable=str, width=20, font=('Arial 18'))
# 로그인 버튼 생성
Lin_btn = Button(lP, text="Login", command=logIn, height=4, width=8)
# 비밀번호나 아이디 잘못 되었을 때 알려줄 결과 텍스트
Lin_result = Label(lP, text="아이디와 비밀번호를 입력하세요.",)
# 여기를 주로 고쳐야 할 것임
IdEX.pack(side=LEFT)
pwEX.pack(side=LEFT)
Id.pack(side=LEFT)
pw.pack(side=LEFT)
Lin_btn.pack(side=LEFT)
Lin_result.pack()

# 회원가입 버튼 생성
SignUpBtn = Button(lP, text="회원가입 하기", command=go_signUp, height=5)
SignUpBtn.pack(side=BOTTOM)

lP.mainloop()
dbgen.commit()
