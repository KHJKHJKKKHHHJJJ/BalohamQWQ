from tkinter import *
import selectDay as sd
from colors import bg_center, bg_side

# 메인메뉴 클래스로 정의
class Main:
    # 호출시 불러야할 매개 변수: 윈도우, 유저 ID
    def __init__(self, main_window, Id) -> None:
        # self로 매개변수를 정의를 해줘야 클래스 안에 있는 매소드에서 참조할 수 있음
        self.main_window = main_window
        # 창 설정
        self.main_window.title("Main")
        self.main_window.config(bg=bg_side)
        self.main_window.resizable(0,0)
        self.id = Id

        # 전체 프레임(디자인 하려고 만듦)
        entireFrame = Frame(main_window, bg=bg_center)
        entireFrame.pack(padx= 20, pady=20)

        # 로고 불러옴
        self.logo_image = PhotoImage(file="image/QWQ 2번 로고.png")
        logo_label = Label(entireFrame, image=self.logo_image, bg=bg_center)
        logo_label.pack(side=TOP, pady=10)

        # 버튼 프레임 만듦
        btnFrame = Frame(entireFrame, bg=bg_center)
        btnFrame.pack(side=BOTTOM, padx=15, pady=15)

        # 학습 버튼 만듦
        self.std_img = PhotoImage(file="image/학습 버튼.png")
        learn_button = Button(btnFrame, image=self.std_img, command=self.go_learn)
        learn_button.pack(side=LEFT, padx=15)

        # 퀴즈 버튼 만듦
        self.quiz_img = PhotoImage(file="image/퀴즈 버튼.png")
        word_quest_button = Button(btnFrame, image=self.quiz_img, command=self.go_quiz)
        word_quest_button.pack(side=RIGHT, padx=15)

    # 학습 버튼 정의
    def go_learn(self):
        # Toplevel() 메소드가 또 다른 창을 띄워주게 함
        win = Toplevel()
        # 중간에 s 혹은 q를 넣어서 학습인지, 퀴즈인지 구분하고, 후에 resultPage에서 쓸 id 정보를 넣어줌
        sd.DateSelWin(win, "s", self.id)

    def go_quiz(self):
        win = Toplevel()
        sd.DateSelWin(win, "q", self.id)

# 밑에는 로그인창 만들기전에 테스트 하려고 만든 것
# def window():
#     window = Tk()
#     Main(window)
#     window.mainloop()

# if __name__ == '__main__':
#     window()
