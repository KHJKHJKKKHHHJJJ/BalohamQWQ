from tkinter import *
from tkinter import ttk
from colors import bg_center, bg_side, btncol
import sqlite3 as sql #테스트 용
import main 

class WordList:
    def __init__(self, wList, date_vocab, date, Id) -> None:

        self.wordList = wList
        self.wordList.title(f"Day{date} Word List")
        self.wordList.resizable(0,0)
        self.wordList.config(bg=bg_side)
        self.id = Id

        self.style = ttk.Style(master=self.wordList)
        self.style.configure("Treeview", rowheight=25)

        self.logo = PhotoImage(file="image/QWQ 2번 로고.png", master=self.wordList) 
        logoLabel = Label(self.wordList, image=self.logo, bg=bg_side)
        logoLabel.pack(anchor="center")

        ListFrame = Frame(self.wordList, bg=bg_side)
        ListFrame.pack(padx=10, pady=20)


        columns = ["영단어", "뜻"]
        self.wordTree = ttk.Treeview(ListFrame, columns=columns, show="headings", height=len(date_vocab)//2)

        self.wordTree.column("#1", width=150, anchor="center")
        self.wordTree.column("#2", width=600, anchor="center")

        for column in columns:
            self.wordTree.heading(column=column, text=column)
        index = 1
        for words in date_vocab.items():
            self.wordTree.insert('', 'end', values=words, tags=f"index{index}")
            self.wordTree.tag_configure(f"index{index}", background=bg_center, font=("SUITE Variable", 16))
            index += 1
        
        self.wordTree.grid(row=0, column=0)

        scrollbar = ttk.Scrollbar(ListFrame, orient=VERTICAL, command=self.wordTree.yview)
        self.wordTree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

        BtnFrame = Frame(self.wordList, background=bg_center, relief="solid", bd=3)
        checker = Button(BtnFrame, text="체크\n하기", anchor="center", font=("SUITE Variable",16, "bold"), bg=btncol, command=self.checker)
        mainBtn = Button(BtnFrame, text="메인 메뉴로 \n 돌아가기", anchor="center", font=("SUITE Variable", 16, "bold"), bg=btncol, command=self.go_main)
        BtnFrame.pack(padx=10, pady=20)
        checker.grid(row=0, column=0, padx=25, pady=10)
        mainBtn.grid(row=0, column=1, padx=25, pady=10)
        # self.wordList.mainloop()

    def go_main(self):
        win = Toplevel()
        main.Main(win, self.id)
        self.wordList.withdraw()

    def checker(self):
        word = self.wordTree.item(self.wordTree.selection(), 'tags')
        self.wordTree.tag_configure(word, background="#FFB5A5")
        # print(self.wordTree.item(word, 'tags'))

if __name__ == "__main__":
    win = Tk()
    db = sql.connect("DB/VocabDB/vocabs.db")
    dbcs = db.cursor()
    date_vocab = dict(dbcs.execute(f"SELECT * FROM day3"))
    WordList(win, date_vocab, 3, Id="scottjoon")
    win.mainloop()
