from tkinter import *
import random as rd

# 클래스 정의
class Flash:
    # 초기 함수 정의 매개 변수에 윈도우, 날짜에 해당하는 단어들을 가져옴
    def __init__(self, flash_window, date_vocab):
        # 윈도우를 self화 시켜서 함수에서도 호출 시킬수 있게 함
        self.flash_window = flash_window
        
        # 윈도우 설정
        self.flash_window.title("Flash Card")
        self.flash_window.resizable(width=False, height=False)
        self.flash_window.config(background="black")

        # SelectDay 에서 결정한 날짜를 불러옴
        self.date_vocab = date_vocab
        # date_vocab은 딕셔너리 형태로 {영단어:한글 뜻} 형태임
        self.test_questions = list(date_vocab.keys()) # 따라서 key만 가져와 영단어 리스트를 만든다.
        # 랜덤 모듈에서 셔플 메소드를 가져와 영단어 리스트를 를 섞어준다 
        rd.shuffle(self.test_questions)
        # 버튼 자체가 창의 크기, 텍스트를 영단어의 첫번째로
        self.Word = Button(self.flash_window, text=self.test_questions[0], font=('', 40), command=self.nextone, width=30, height=10, fg= "white", bg="black", wraplength=900, activebackground="black")
        self.Word.pack()

    # 버튼에 쓸 함수 정의 self를 넣어야 self.<변수 이름>으로 정의 한 변수들을 쓸 수 있음
    def nextone(self):
        global passed
        # 버튼의 텍스트가 한국어인지 영어인지 구분하기 위한 if문
        if self.Word["text"] in self.test_questions: # 버튼 텍스트가 영어일 때
            # index를 정의하여 몇 번째 값인지 알아냄
            i = self.test_questions.index(self.Word["text"])
            # index를 이용해 버튼의 텍스트를 변경함 
            self.Word["text"] = self.date_vocab[self.test_questions[i]]
            # 한국어에서 영어로 넘어갈 때도 index를 정의 하기 위해 
            passed = []
            passed.append(self.test_questions[i])
        else: # 버튼 텍스트가 한국어일 때
            # 정의한 passed로 index 정의 
            i = self.test_questions.index(passed[0])
            # i가 끝날 때, 안 끝날 때로 케이스 분류
            if i != len(self.test_questions)- 1: # 마지막이 아니라면
                # 버튼 텍스트를 i + 1로 정의 함
                self.Word["text"] = self.test_questions[i + 1] 
            else:
                # 아니라면 플래시 카드를 종료함 (후에 메뉴로 이동으로 수정 함.)
                self.flash_window.quit()
