from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure 
from tkinter import *
from matplotlib import font_manager, rc
import pandas as pd
import sqlite3 as sql
import datetime as dtt

class ResultPage:
    font = font_manager.FontProperties(fname="image/fonts/malgun.ttf").get_name()
    rc('font', family=font)

    def __init__(self, rp, userId, date, corr) -> None:
        self.rP = rp
        self.rP.resizable(0,0)

        # 데이터 저장, 불러오기
        with sql.connect("DB/user.db") as dbop:
            dbcs = dbop.cursor()
            dbcs.execute(f"CREATE TABLE IF NOT EXISTS {userId}ResultTable(Date text not null, Day int not null, Result real not null);")
            dbcs.execute(f"INSERT INTO {userId}ResultTable VALUES(?,?,?)", (str(dtt.datetime.today())[:16], date, corr))
            dbop.commit()
            RTable = pd.DataFrame(dbcs.execute(f"SELECT Date, Result FROM  {userId}ResultTable WHERE Day = {date};"))
            UTable = dict(dbcs.execute("SELECT id, name FROM userTable;"))
            userName = UTable[userId]

        # 데이터 테스트
        print(RTable)

        # 그래프 띄우기
        fig = Figure(figsize=(6,6), dpi=100)
        graph = fig.add_subplot(111)
        graph.bar(RTable[RTable.columns[0]],RTable[RTable.columns[1]])
        graph.set_title(label=f"{userName}'s Day{date} Results")
        graph.set_xlabel("날짜")
        graph.set_ylabel("정답률\n(단위: %)")
        canva = FigureCanvasTkAgg(fig, master=self.rP)
        canva.get_tk_widget().pack()
        canva._tkcanvas.pack(side=TOP, padx=20, pady=20)
        self.menuBtn = Button(self.rP, text="메뉴로 돌아가기")
        self.menuBtn.pack()
    
    


'''

'''