from tkinter import *
from tkinter import ttk, font
import sqlite3 as sql
from tkinter import messagebox as msb
import Login
from colors import bg_side, bg_center, btncol


class SignPage:
    def __init__(self, signPage) -> None:
        self.signPage = signPage
        self.signPage.title("Sign-Up Page")
        self.signPage.resizable(0,0)
        self.signPage.geometry("680x800")
        self.signPage.config(bg=bg_side)

        self.logo = PhotoImage(file="image/QWQ 2번 로고.png")
        logoLabel = Label(self.signPage, image=self.logo, bg=bg_side)
        logoLabel.pack()

        PageName = Label(self.signPage, text="회원가입", font=("SUITE Variable", "38","bold"), bg=bg_side, fg="white")
        PageName.place(x=10, y=180)

        usersFrame = Frame(signPage, bg=bg_center)
        usersFrame.place(x=10, y=250, width=660, height=400)
        userNameText = Label(usersFrame, text="이름을 입력하세요: ", font=("SUITE Variable","18"), bg=bg_center)
        self.userName = Entry(usersFrame, textvariable=str, font=("SUITE Variable", "18"))
        userNameText.place(x=20, y=10)
        self.userName.place(x=240, y=10)

        userIdText = Label(usersFrame, text="ID를 입력하세요: ", font=("SUITE Variable","18"), bg=bg_center)
        self.userId = Entry(usersFrame, textvariable=str, font=("SUITE Variable", "18"))
        self.IdVerify = Button(usersFrame, text="중복확인", command=self.IDVerifier, font=("SUITE Variable", "14"), background=btncol)
        userIdText.place(x=20, y=80)
        self.userId.place(x=240, y=80)
        self.IdVerify.place(x=550, y=80)

        self.userEmail_text = Label(usersFrame, text="이메일을 입력하세요: ", font=("SUITE Variable", "18"), bg=bg_center)
        self.userEmail_front = Entry(usersFrame, textvariable=str, font=("SUITE Variable", "18")) 
        self.userEmail_back = ttk.Combobox(usersFrame, values=["gmail.com", "naver.com", "daum.net"], font=("SUITE Variable", "18"))
        sep = Label(usersFrame, text='@', font=("SUITE Variable", "18"), bg=bg_center)
        self.userEmail_text.place(x=20, y=150)
        self.userEmail_front.place(x=20, y=200)
        sep.place(x=290, y=200)
        self.userEmail_back.place(x=320, y=200, width=300)

        userPWText = Label(usersFrame, text="비밀번호를 입력하세요: ", bg=bg_center, font=("SUITE Variable", "18"))
        self.userPW = Entry(usersFrame, textvariable=str, show="●", font=("SUITE Variable", "18"))
        userPWTextTwo = Label(usersFrame, text="비밀번호를 다시 한번 입력하세요: ", font=("SUITE Variable", "18"), bg=bg_center)
        self.userPWC = Entry(usersFrame, textvariable=str, show="●", font=("SUITE Variable", "18"))
        userPWText.place(x=20, y=270)
        self.userPW.place(x=300, y=270)
        userPWTextTwo.place(x=20, y=340)
        self.userPWC.place(x=400, y=340)

        self.Enter = Button(self.signPage, text="회원가입 하기", font=("SUITE Variable", "18"), width=15, height=2, command=self.insertFunc, state="disabled", bg=btncol)
        self.Enter.place(x=60, y=660)

        goBack = Button(self.signPage, text="로그인으로 돌아가기", font=("SUITE Variable", 18), width=15, height=2, bg=btncol, command=self.go_back)
        goBack.place(x=380, y=660)
        self.verifiedId = 0

    def insertFunc(self):
        checker = 0
        dbop = sql.connect("DB/user.db")
        dbcs = dbop.cursor()
        name = self.userName.get()
        Id = self.userId.get()
        email = str(self.userEmail_front.get()+ '/' + self.userEmail_back.get())
        pw = self.userPW.get()

        # 이름 형식 오류
        if len(name) >= 16 or len(name) <= 0:
            msb.showwarning(title="ERROR", message="이름의 최대 길이는 16, 최소 길이는 1입니다.")
            self.userName.delete(0,END)
        else:
            checker += 1

        # 이메일 형식 오류
        if '.' not in self.userEmail_back.get() or len(self.userEmail_front.get()) <= 0:
            msb.showwarning(title="ERROR", message="이메일을 올바르게 입력하세요")
            self.userEmail_back.delete(0, END)
        else:
            if self.userEmail_back.get() not in ["gmail.com", "naver.com", "daum.net"]:
                msb.showwarning(title="ERROR", message="지원하지 않는 이메일 형식입니다.")
                self.userEmail_back.delete(0,END)
            else:
                checker += 1

        if self.verifiedId == 1:
            checker += 1
        
        # 비밀 번호 불 일치
        if self.userPWC.get() != self.userPW.get():
            msb.showerror(title="ERROR", message="비밀번호를 확인하세요")
        else:
            checker += 1
        if checker == 4:
            self.Checked()

    def Checked(self):
        dbop = sql.connect("DB/user.db")
        dbcs = dbop.cursor()
        name = self.userName.get()
        Id = self.userId.get()
        email = str(self.userEmail_front.get()+ '/' + self.userEmail_back.get())
        pw = self.userPW.get()

        dbcs.execute(f"INSERT INTO userTable VALUES(?,?,?,?)", (Id, name, email, pw))
        dbop.commit()
        self.signPage.withdraw()
        self.go_back()
        

    def IDVerifier(self):
        dbop = sql.connect("DB/user.db")
        dbcs = dbop.cursor()
        Id = self.userId.get()
        users = dict(dbcs.execute("SELECT id, name FROM userTable;"))
        if len(Id) >= 20 or len(Id) <= 0:
            msb.showwarning(title="ERROR", message="ID를 확인하시오.")
            self.userId.delete(0,END)
        else:
            if Id in users.keys():
                msb.showerror(title="중복된 ID", message="이미 동일한 ID가 존재 합니다.")
                self.userId.delete(0, END)
            else:
                self.verifiedId = 1
                msb.showinfo(title="중복확인", message="확인 되었습니다.")
                self.Enter['state'] = "normal"
                self.userId['state'] = "disabled"
                self.IdVerify['state'] = "disabled"

    def go_back(self):
        win = Tk()
        Login.LoginPage(win)
        self.signPage.withdraw()
