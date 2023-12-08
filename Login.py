import sqlite3 as sql
from tkinter import *
import main
import SignUp as su
from colors import bg_side, bg_center, btncol

class LoginPage:
    def __init__(self, lP) -> None:
        self.lP = lP
        dbgen = sql.connect("DB/user.db")
        self.dbcs = dbgen.cursor()

        self.lP.title("LogIn Page")
        self.lP.resizable(0,0)
        self.lP.geometry("600x450")
        self.lP.config(bg=bg_side)


        self.logo = PhotoImage(file="image/QWQ 2번 로고.png", master=self.lP)
        lo_label = Label(self.lP, image=self.logo, bg=bg_side)
        lo_label.place(x=55, y=10)

        fullEntire = Frame(self.lP, bg=bg_center)
        fullEntire.place(x=10, y=200, width=580, height=220)

        IdEX = Label(fullEntire, height=2, font=("SUITE Variable","18"), text="ID", bg=bg_center)
        pwEX = Label(fullEntire, height=2, font=("SUITE Variable","18"), text="PassWord", bg=bg_center)
        self.Id = Entry(fullEntire, textvariable=StringVar(), width=20, font=("SUITE Variable","18"))
        self.pw = Entry(fullEntire, textvariable=StringVar(), show='●',  width=20, font=("SUITE Variable","18"))
        IdEX.place(x=20, y=25)
        self.Id.place(x=140, y=40)
        pwEX.place(x=20, y=85)
        self.pw.place(x=140, y=100)

        Lin_btn = Button(fullEntire, text="로그인", command=self.logIn, font=("SUITE Variable", 16), height=3, bg=btncol)
        Lin_btn.place(x=490, y=40)
        self.Lin_result = Label(fullEntire, text="아이디와 비밀번호를 입력하세요.",font=("SUITE Variable", 16), bg=bg_center)
        self.Lin_result.place(x=125, y=145)

        SignUpBtn = Button(fullEntire, text="회원가입 하기", command=self.go_signUp, bg=btncol)
        SignUpBtn.place(y=145, x=480)
        dbgen.commit()


        self.lP.bind("<Return>", self.enter)

    def logIn(self):
        userId = self.Id.get()
        userPW = self.pw.get()
        # 유저 테이블을 딕셔너리로 불러옴
        userTable = dict(self.dbcs.execute(f"select id, pw from userTable;"))
        # 유저 로그인 실패시
        if userId not in userTable.keys() or userTable[userId] != userPW:
            self.Lin_result.config(text="아이디 혹은 비밀번호가 잘못 되었습니다.")
        else:
            self.go_main()

    def go_main(self):
        win = Toplevel()
        main.Main(win, self.Id.get())
        self.lP.withdraw()

    def go_signUp(self):
        win = Toplevel()
        su.SignPage(win)
        self.lP.withdraw()

    def enter(self, event):
        self.logIn()


if __name__ == "__main__":
    win = Tk()
    LoginPage(win)
    win.mainloop()