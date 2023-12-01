from tkinter import *
import sqlite3 as sql
from tkinter import messagebox as msb

# 로그인 페이지에서 불러와야 하므로 클래스로 정의
class SignPage:
    # 초기 설정
    def __init__(self, signPage) -> None:
        # 윈도우 설정
        self.signPage = signPage
        self.signPage.title("Sign-Up Page")
        self.signPage.resizable(0,0)

        # 유저 이름 적는 곳 프레임 세팅
        userNameFrame = Frame(self.signPage)
        userNameText = Label(userNameFrame, text="이름을 입력하세요")
        self.userName = Entry(userNameFrame, textvariable=str)
        userNameText.pack(side=LEFT)
        self.userName.pack(side=LEFT)
        userNameFrame.pack(pady=20)

        # 유저 아이디 적는 곳 프레임 세팅
        userIdFrame = Frame(self.signPage)
        userIdText = Label(userIdFrame, text="ID를 입력하세요.")
        self.userId = Entry(userIdFrame, textvariable=str)
        self.IdVerify = Button(userIdFrame, text="중복확인", command=self.IDVerifier)
        self.IdVerify.pack(side=RIGHT)
        userIdText.pack(side=LEFT)
        self.userId.pack(side=LEFT)
        userIdFrame.pack(pady=20)

        # 이메일 적는 곳 프레임 세팅
        userEmailFrame = Frame(self.signPage)
        self.userEmail_front = Entry(userEmailFrame, textvariable=str) 
        self.userEmail_back = Entry(userEmailFrame)
        sep = Label(userEmailFrame, text='@')
        self.userEmail_front.pack(side=LEFT)
        sep.pack(side=LEFT)
        self.userEmail_back.pack(side=LEFT)
        userEmailFrame.pack()

        # 비밀번호 적는 곳 프레임 세팅
        userPWFrame = Frame(self.signPage)
        userPWText = Label(userPWFrame, text="비밀번호를 입력하세요.")
        self.userPW = Entry(userPWFrame, textvariable=str)
        userPWText.pack(side=LEFT)
        self.userPW.pack(side=LEFT)
        userPWFrame.pack(pady=20)

        # 입력 버튼
        Enter = Button(self.signPage, text="회원가입 하기", height=5, command=self.insertFunc)
        Enter.pack(side=BOTTOM)

    # DB연결해서 유저 정보 넣음
    def insertFunc(self):
        dbop = sql.connect("DB/user.db")
        dbcs = dbop.cursor()
        name = self.userName.get()
        Id = self.userId.get()
        email = str(self.userEmail_front.get()+ '/' + self.userEmail_back.get())
        pw = self.userPW.get()
        dbcs.execute(f"INSERT INTO userTable VALUES(?,?,?,?)", (Id, name, email, pw))
        # users = dbcs.execute("SELECT * FROM userTable;") # 테이블 조회
        # print(list(users))
        dbop.commit()
        dbcs.close()
        self.signPage.withdraw()

    # ID 중복확인 버튼 함수
    def IDVerifier(self):
        dbop = sql.connect("DB/user.db")
        dbcs = dbop.cursor()
        Id = self.userId.get()
        users = dict(dbcs.execute("SELECT id, name FROM userTable;"))
        if Id in users.keys():
            msb.showerror(title="중복된 ID", message="이미 동일한 ID가 존재 합니다.")
            self.userId.delete(0, END)
        else:
            msb.showinfo(title="중복확인", message="확인 되었습니다.")


        
