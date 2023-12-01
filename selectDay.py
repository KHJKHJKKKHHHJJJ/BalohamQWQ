from tkinter import *
import sqlite3 as sql
import flashCard as fC
import quiz as qz
from colors import bg_center, btncol

# 클래스 정의
class DateSelWin:
    # 초기 매개 변수: 창, s냐 아님 q냐, 유저 ID)
    def __init__(self, dateSel_window, sorq, Id):
        # 창 셀프화
        self.dateSel_window = dateSel_window
        self.dateSel_window.title("Day Selection")
        self.dateSel_window.config(bg=bg_center)
        self.dateSel_window.resizable(0,0)
        self.id = Id

        self.logo_image = PhotoImage(file="image/QWQ 2번 로고.png")

        # 본인이 만드신 것이니 주석 안넣겠습니다.
        logo_label = Label(self.dateSel_window, image=self.logo_image, bg=bg_center)
        logo_label.pack(pady=5)

        level_range_1_10 = list(range(1, 11))
        level_range_11_20 = list(range(11, 21))
        level_range_21_30 = list(range(21, 31))

        levels = [level_range_1_10, level_range_11_20, level_range_21_30]
        labels = ["DAY 1~10", "DAY 11~20", "DAY 21~30"]

        self.sorq = sorq

        for level_group, label in zip(levels, labels):
            frame = Frame(dateSel_window, relief="solid", bd=5)
            frame.pack(side=LEFT, padx=5, pady=5)
            
            label_widget = Label(frame, text=label, font=("", "14", "bold"))
            label_widget.pack(side=TOP, pady=10)

            for level in level_group:
                button = Button(frame, text=str(level), font=("", "12", "bold"), command=lambda l=level: self.date_seled(l), width=20, height=2, bg=btncol)
                button.pack(side=TOP)


    def date_seled(self, level):
        global date_vocab
        # 사전에 db에 넣어둔 단어db (테이블들 있는데) 불러옴
        db = sql.connect("DB/VocabDB/vocabs.db")
        dbcs = db.cursor()
        date_vocab = dict(dbcs.execute(f"SELECT * FROM day{level}"))
        # Toplevel이나 Tk()나 상관 없는 것 같네요
        win = Tk()
        if self.sorq == "s":
            # 이 부분에 창 하나 더 만들어서 플래시 카드를 할건지 단어 리스트를 볼 건지 결정하게 할 겁니다. 우선은 플래시 카드로만
            fC.Flash(win, date_vocab, level)
            win.mainloop()
        else:
            # 퀴즈 불러옴
            qz.Quiz(win, date_vocab, level, self.id)
            win.mainloop()
        db.commit()
