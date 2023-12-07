from tkinter import *
import sqlite3 as sql
import LearnSelect as LS
import quiz as qz
from colors import bg_center, btncol, bg_side
import main
from tkinter import messagebox as msb

class DateSelWin:
    def __init__(self, dateSel_window, sorq, Id):
        self.dateSel_window = dateSel_window
        self.dateSel_window.title("Day Selection")
        self.dateSel_window.config(bg=bg_side)
        self.dateSel_window.resizable(0,0)
        self.id = Id

        self.logo_image = PhotoImage(file="image/QWQ 2번 로고.png")

        logo_label = Label(self.dateSel_window, image=self.logo_image, bg=bg_side)
        logo_label.pack(pady=5)

        level_range_1_10 = list(range(1, 11)) 
        level_range_11_20 = list(range(11, 21))
        level_range_21_30 = list(range(21, 31))

        levels = [level_range_1_10, level_range_11_20, level_range_21_30]
        labels = ["DAY 1~10", "DAY 11~20", "DAY 21~30"]

        self.sorq = sorq

        DayFrame = Frame(dateSel_window, bg=bg_side)
        DayFrame.pack()

        for level_group, label in zip(levels, labels):
            frame = Frame(DayFrame, relief="solid", bd=5)
            frame.pack(side=LEFT, padx=5, pady=5)
            
            label_widget = Label(frame, text=label, font=("SUITE Variable", "14", "bold"))
            label_widget.pack(side=TOP, pady=10)

            for level in level_group:
                button = Button(frame, text=str(level), font=("SUITE Variable", "12", "bold"), command=lambda l=level: self.date_seled(l), width=20, height=2, bg=btncol)
                button.pack(side=TOP)

        back = Button(self.dateSel_window, text="메뉴로 돌아가기", font=("SUITE Variable", "12"), bg=btncol, command=self.goBack)
        back.pack(pady=10, side=BOTTOM)

    def date_seled(self, level):
        global date_vocab
        db = sql.connect("DB/VocabDB/vocabs.db")
        dbcs = db.cursor()
        date_vocab = dict(dbcs.execute(f"SELECT * FROM day{level}"))
        win = Tk()
        if self.sorq == "s":
            LS.LearnSelect(win, date_vocab, level, self.id)
            self.dateSel_window.withdraw()
        else:
            asking = msb.askokcancel(title="Are You Sure?", message="퀴즈는 중간에 돌아갈 수 없으며,\n 퀴즈 결과는 계정에 반영됩니다. 진행 하시겠습니까?")
            if asking == True:
                qz.Quiz(win, date_vocab, level, self.id)
                self.dateSel_window.withdraw()
            else:
                win.withdraw()
        db.commit()
    
    def goBack(self):
        win = Toplevel()
        main.Main(win, self.id)
        self.dateSel_window.withdraw()
