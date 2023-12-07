from tkinter import *
import random as rd
import main 

class Flash:
    def __init__(self, flash_window, date_vocab, date, Id):
        self.flash_window = flash_window
        self.flash_window.title(f"Flash Card Day{date}")
        self.flash_window.resizable(width=False, height=False)
        self.flash_window.config(background="black")
        self.id = Id

        self.date_vocab = date_vocab
        self.test_questions = list(date_vocab.keys())
        rd.shuffle(self.test_questions)
        self.Word = Button(self.flash_window, text=self.test_questions[0], font=('', 40), command=self.nextone, width=30, height=10, fg= "white", bg="black", wraplength=900, activebackground="black")

        self.Word.pack()

    def nextone(self):
        global passed
        if self.Word["text"] in self.test_questions:
            i = self.test_questions.index(self.Word["text"])
            self.Word["text"] = self.date_vocab[self.test_questions[i]]
            passed = []
            passed.append(self.test_questions[i])
        else:
            i = self.test_questions.index(passed[0])
            if i != len(self.test_questions)- 1:
                self.Word["text"] = self.test_questions[i + 1]
            else:
                win = Toplevel()
                main.Main(win, self.id)
                self.flash_window.withdraw()
