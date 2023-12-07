from tkinter import *
import selectDay as sd
from colors import bg_center, bg_side, btncol
from tkinter import messagebox as msb
import Login

class Main:
    def __init__(self, main_window, Id) -> None:
        self.main_window = main_window
        self.main_window.title("Main")
        self.main_window.config(bg=bg_side)
        self.main_window.resizable(0,0)
        self.id = Id

        entireFrame = Frame(main_window, bg=bg_center)
        entireFrame.pack(padx= 20, pady=20)

        self.logo_image = PhotoImage(file="image/QWQ 2번 로고.png")
        logo_label = Label(entireFrame, image=self.logo_image, bg=bg_center)
        logo_label.pack(side=TOP, pady=10)

        btnFrame = Frame(entireFrame, bg=bg_center)
        btnFrame.pack(side=BOTTOM, padx=15, pady=15)

        self.std_img = PhotoImage(file="image/학습 버튼.png")
        learn_button = Button(btnFrame, image=self.std_img, command=self.go_learn)
        learn_button.pack(side=LEFT, padx=15)

        self.quiz_img = PhotoImage(file="image/퀴즈 버튼.png")
        word_quest_button = Button(btnFrame, image=self.quiz_img, command=self.go_quiz)
        word_quest_button.pack(side=LEFT, padx=15)

        quitFrame = Frame(btnFrame, bg=bg_center)
        quitFrame.pack(side=LEFT)

        lout = Button(quitFrame, text="로그아웃", font=("SUITE Variable", 14), bg=btncol, command=self.log_out)
        lout.pack(side=TOP, pady=5)

        quit_btn = Button(quitFrame, text="종료하기", font=("SUITE Variable", 14), bg=btncol, command=self.quit_func)
        quit_btn.pack(side=BOTTOM)

    def go_learn(self):
        win = Toplevel()
        sd.DateSelWin(win, "s", self.id)
        self.main_window.withdraw()

    def go_quiz(self):
        win = Toplevel()
        sd.DateSelWin(win, "q", self.id)
        self.main_window.withdraw()
    
    def quit_func(self):
        asking = msb.askokcancel(title="Are You Sure?", message="정말로 QWQ를 종료하시겠습니까?")
        if asking == True:
            self.main_window.quit()
    
    def log_out(self):
        asking = msb.askokcancel(title="Are You Sure?", message="정말로 로그아웃 하시겠습니까?")
        if asking == True:
            win = Tk()
            Login.LoginPage(win)
            self.main_window.withdraw()

if __name__ == "__main__":
    win = Tk()
    Main(win, 'scottjoon')
    win.mainloop()