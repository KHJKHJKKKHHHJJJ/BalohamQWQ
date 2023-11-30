from tkinter import *
import sqlite3 as sql
from tkinter import messagebox as msb


class SignPage:
    def __init__(self, signPage) -> None:
        self.signPage = signPage
        self.signPage.title("Sign-Up Page")
        self.signPage.resizable(0,0)

        userNameFrame = Frame(self.signPage)
        userNameText = Label(userNameFrame, text="이름을 입력하세요")
        self.userName = Entry(userNameFrame, textvariable=str)
        userNameText.pack(side=LEFT)
        self.userName.pack(side=LEFT)
        userNameFrame.pack(pady=20)

        userIdFrame = Frame(self.signPage)
        userIdText = Label(userIdFrame, text="ID를 입력하세요.")
        self.userId = Entry(userIdFrame, textvariable=str)
        self.IdVerify = Button(userIdFrame, text="중복확인", command=self.IDVerifier)
        self.IdVerify.pack(side=RIGHT)
        userIdText.pack(side=LEFT)
        self.userId.pack(side=LEFT)
        userIdFrame.pack(pady=20)

        # 이메일 입력창은 수정 필요 함
        userEmailFrame = Frame(self.signPage)
        self.userEmail_front = Entry(userEmailFrame, textvariable=str) 
        self.userEmail_back = Entry(userEmailFrame)
        sep = Label(userEmailFrame, text='@')
        self.userEmail_front.pack(side=LEFT)
        sep.pack(side=LEFT)
        self.userEmail_back.pack(side=LEFT)
        userEmailFrame.pack()

        userPWFrame = Frame(self.signPage)
        userPWText = Label(userPWFrame, text="비밀번호를 입력하세요.")
        self.userPW = Entry(userPWFrame, textvariable=str)
        userPWText.pack(side=LEFT)
        self.userPW.pack(side=LEFT)
        userPWFrame.pack(pady=20)

        Enter = Button(self.signPage, text="회원가입 하기", height=5, command=self.insertFunc)
        Enter.pack(side=BOTTOM)

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


        