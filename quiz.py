from tkinter import *
import random as rd
from colors import bg_center,bg2,btncol
import result as rs

class Quiz:
    def __init__(self, quiz_window, date_vocab, date, Id):
        self.quiz_window = quiz_window
        self.date = date
        quiz_window.title(f"Quiz Day{date}")
        quiz_window.resizable(0,0)
        quiz_window.config(bg=bg_center)
        self.corr_list = []
        self.id = Id
        
        # 문제 세팅
        self.date_vocab = date_vocab
        self.english = list(date_vocab.keys())
        rd.shuffle(self.english)

        # 문제창
        self.texts_frame = LabelFrame(self.quiz_window, relief="solid", bd=3, bg=bg2)
        self.Language_type = Label(self.texts_frame, text="단어", font=("SUITE Variable", "25"), fg="black", height=1, width=10, bg=bg2)
        self.word = Label(self.texts_frame, text=self.english[0], font=("Times New Roman", "40", "bold"), fg ="black", width=20, height=2, bg=bg2)
        self.texts_frame.pack(pady=10)
        self.Language_type.pack(side=TOP)
        self.word.pack(pady=10)
        self.progress = Label(self.texts_frame, text=f"0/{len(self.english) - 1}")
        self.progress.pack(side=BOTTOM)

        #보기 설정
        sel_btn_frame = Frame(quiz_window, relief="solid", bd=3)
        sel_btn_frame.pack(padx=15)

        # 보기 텍스트
        self.selections = []
        for i in range(3):
            btn = Button(sel_btn_frame, text=f"{i + 1}번", width= 53, height= 2, font=("SUITE Variable", 15, 'bold'), command=self.incorrect, bg=btncol)
            self.selections.append(btn)
        self.answer = Button(sel_btn_frame, text=date_vocab[self.english[0]], width= 53, height= 2, font=("", 15, 'bold'), command=self.correct, bg=btncol)
        self.selections.append(self.answer)
        rd.shuffle(self.selections)
        selections_txt = []
        for selection in self.selections:
            while True:
                Nselection = date_vocab[rd.sample(self.english, 1)[0]]
                if selection != self.answer:
                    if Nselection == date_vocab[self.english[0]] or selection in selections_txt:
                        continue
                    else:
                        selection["text"] = Nselection
                break
            selection.pack()
        
        #건너뛰기 or 다음 문제
        self.nextbtn = Button(quiz_window, text="건너뛰기", width= 38, height=3, font=("SUITE Variable",15,'bold'), bg="light yellow", command=self.next_word)
        self.nextbtn.pack(pady= 10, side=BOTTOM)

        self.quiz_window.bind("<space>", self.skip)


    # next_self.word 함수
    def next_word(self):
        self.answer.config(bg=btncol)
        for selection in self.selections:
            selection.config(state="normal")

        # 안댁스로 정의
        self.index = self.english.index(self.word["text"]) + 1

        if self.nextbtn["text"] == "결과 보기":
            self.go_result()
            self.quiz_window.withdraw()
        else:
            # 다음 정답 결정
            self.nextbtn['text'] = "건너뛰기"
            if self.index != len(self.english)- 1:
                self.word.config(text=self.english[self.index])
                self.answer.config(text=self.date_vocab[self.word["text"]])
            elif self.index == len(self.english) - 1:
                self.nextbtn["text"] = "결과 보기"
                for selection in self.selections:
                    selection.config(state="disabled")
            selections_txt = []
            for selection in self.selections:
                selection.config(bg=btncol)
                selection.pack_forget()
                while True:
                    Nselection = self.date_vocab[rd.sample(self.english, 1)[0]]
                    if selection != self.answer:
                        if Nselection == self.date_vocab[self.english[self.index]] or Nselection in selections_txt:
                            continue
                        else:
                            selections_txt.append(Nselection)
                            selection["text"] = Nselection
                    break
                selection.pack()
            # 보기 재설정
            rd.shuffle(self.selections)
            self.progress.config(text=f"{self.index}/{len(self.english)-1}")


    def correct(self):
        self.corr_list.append(self.word["text"])
        self.next_word()


    def incorrect(self):
        self.answer.config(bg="light green")
        for selection in self.selections:
            selection.config(state="disabled")
        self.nextbtn.config(text="다음 문제")
    

    def go_result(self):
        win = Toplevel()
        corr = round(len(self.corr_list)/len(self.english), 3) * 100
        userId = self.id
        date = self.date
        rs.ResultPage(win, userId, date, corr)

    def skip(self, event):
        self.next_word()