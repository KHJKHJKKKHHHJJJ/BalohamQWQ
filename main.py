from tkinter import *
import selectDay as sd
from colors import bg_center, bg_side

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
        word_quest_button.pack(side=RIGHT, padx=15)

    def go_learn(self):
        win = Toplevel()
        sd.DateSelWin(win, "s", self.id)

    def go_quiz(self):
        win = Toplevel()
        sd.DateSelWin(win, "q", self.id)

# def window():
#     window = Tk()
#     Main(window)
#     window.mainloop()

# if __name__ == '__main__':
#     window()
