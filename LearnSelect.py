from tkinter import *
import sqlite3 as sql # 테스트 용
import flashCard as fc
import WordList as wl
from colors import bg_side, bg_center, btncol
import main

class LearnSelect:
    def __init__(self, win, date_vocab, date, Id) -> None:    
        self.lSelect = win
        self.lSelect.title("Select your study strategy")
        self.lSelect.resizable(0,0)
        self.lSelect.geometry("680x400")
        self.lSelect.config(bg=bg_side)
        self.date_vocab = date_vocab
        self.date = date
        self.id = Id
        
        self.logo = PhotoImage(file="image/QWQ 2번 로고.png", master=self.lSelect)
        self.logoLabel = Label(self.lSelect, image=self.logo, bg=bg_side)
        self.logoLabel.pack()

        PageDecs = Label(self.lSelect, text="원하시는 학습과정을 선택하세요", font=("SUITE Variable", "33", "bold"), bg=bg_side, fg="white")
        PageDecs.pack()

        btnFrame = Frame(self.lSelect, relief="solid", bd=3, bg=bg_center)
        btnFrame.pack(pady=20)
        flashBtn = Button(btnFrame, text="플래시카드", font=("SUITE Variable", "18"), bg=btncol, command=self.go_flash)
        flashBtn.pack(padx=20, pady=20, side=LEFT)
        listBtn = Button(btnFrame, text="단어 리스트 보기", font=("SUITE Variable", "18"), command=self.go_list, bg=btncol)
        listBtn.pack(padx=20, pady=20, side=LEFT)
        # self.lSelect.mainloop()

        back = Button(btnFrame, text="메뉴로 돌아가기", font=("SUITE Variable", 18), bg=btncol, command=self.goBack)
        back.pack(padx=20, pady=20, side=LEFT)

    def go_flash(self):
        win = Toplevel()
        fc.Flash(win,self.date_vocab, self.date, self.id)
        self.lSelect.withdraw()

    def go_list(self):
        win = Tk()
        wl.WordList(win, date_vocab=self.date_vocab, date=self.date, Id=self.id)
        self.lSelect.withdraw()
    
    def goBack(self):
        win = Toplevel()
        main.Main(win, self.id)
        self.lSelect.withdraw()

# if __name__ == '__main__':
#     db = sql.connect("DB/VocabDB/vocabs.db")
#     dbcs = db.cursor()
#     win = Tk()
#     top = Toplevel()
#     date_vocab = dict(dbcs.execute(f"SELECT * FROM day3"))
#     LearnSelect(top, date_vocab)
#     win.mainloop
