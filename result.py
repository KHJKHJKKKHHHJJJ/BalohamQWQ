from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure 
from tkinter import *
from matplotlib import font_manager, rc
import pandas as pd
import sqlite3 as sql
import datetime as dtt
import main
from random import randint
from colors import bg_center, bg_side, btncol

class ResultPage:
    # rc('font', family=font)

    def __init__(self, rp, userId, date, corr) -> None:
        # font = font_manager.findSystemFonts(fontpaths="image/fonts/SUITE-Variable.ttf")
        vari = font_manager.FontProperties(fname="image/fonts/SUITE-Variable.ttf")

        self.rP = rp
        self.rP.resizable(0,0)
        self.rP.title("Result Page")
        self.rP.config(bg=bg_side)
        self.id = userId

        # 데이터 저장, 불러오기
        with sql.connect("DB/user.db") as dbop:
            dbcs = dbop.cursor()
            dbcs.execute(f"CREATE TABLE IF NOT EXISTS {userId}ResultTable(Date text not null, Day int not null, Result real not null);")
            dbcs.execute(f"INSERT INTO {userId}ResultTable VALUES(?,?,?)", (str(dtt.datetime.today())[:16], date, corr))
            dbop.commit()
            RTable = pd.DataFrame(dbcs.execute(f"SELECT Date, Result FROM {userId}ResultTable WHERE Day = {date};"))
            UTable = dict(dbcs.execute("SELECT id, name FROM userTable;"))
            userName = UTable[userId]
            # print(list(RTable[RTable.columns[0]][len(RTable)-5:]), list(RTable[RTable.columns[1]]))
        # 데이터 테스트
        # print(RTable)  

        # 그래프 띄우기
        fig = Figure(figsize=(15,8), dpi=80, facecolor=bg_center)
        graph = fig.add_subplot(111) # face color 옵션으로 색 변경 가능
        graph.bar(list(RTable[RTable.columns[0]][len(RTable)-30:]), list(RTable[RTable.columns[1]][len(RTable)-30:]), width=0.3, color="#8050FF")
        graph.set_title(label=f"{userName}'s Day{date} Results",fontproperties=vari, fontsize=36)
        graph.set_xlabel("날짜", fontproperties=vari, size=18)
        graph.set_ylabel("정답률\n(단위: %)", fontproperties=vari, size=18)
        fig.autofmt_xdate(rotation=20)
        # graph.set_xticks()
        canva = FigureCanvasTkAgg(fig, master=self.rP)
        canva.get_tk_widget().pack()
        canva._tkcanvas.pack(side=TOP, padx=20, pady=20)
        self.menuBtn = Button(self.rP, text="메뉴로 돌아가기", command=self.go_main)
        self.menuBtn.pack()

    def go_main(self):
        win = Toplevel()
        main.Main(win, self.id)
        self.rP.withdraw()

if __name__ == '__main__':
    win = Tk()
    ResultPage(win, 'scottjoon', 4, randint(30, 100))
    win.mainloop()
