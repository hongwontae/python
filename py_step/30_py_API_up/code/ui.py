import tkinter
import quiz_brain

THEME_COLOR = "#375362"

class QuizInterface :
    def __init__(self, quiz_brain : quiz_brain.QuizBrain):
        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        # ui
        self.score_label = tkinter.Label(text='Score : 0', fg='white', bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = tkinter.Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(150, 125, 
        text='Some Question Text',
        fill= THEME_COLOR,
        width=280,
        font=("Arial", 20, 'italic')
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = tkinter.PhotoImage(file='./images/true.png')
        false_image = tkinter.PhotoImage(file='./images/false.png')

        self.true_button = tkinter.Button(image=true_image, highlightthickness=0, command=self.o_check_handler)
        self.false_button = tkinter.Button(image=false_image, highlightthickness=0, command=self.x_check_handler)
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()
    

    def get_next_question (self) :
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions() :
            self.score_label.config(text=f"Score : {self.quiz.score}")
            # 이미 quiz 객체는 초기화가 완료된 상태입니다. => 그렇기에 next_question() 메서드 정상 작동
            q_text = self.quiz.next_question()
            # canvas.itemconfig를 통해 text 해결
            self.canvas.itemconfig(self.question_text, text=q_text)
        else :
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')
    
    def o_check_handler (self) :
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
    
    def x_check_handler (self) :
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)
    

    def give_feedback (self, is_right) :
        if is_right :
            self.canvas.config(bg='green')
        else :
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)