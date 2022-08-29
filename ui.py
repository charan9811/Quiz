from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        # label
        self.label = Label(text=f"score: {self.quiz.score} ", bg=THEME_COLOR, fg="white", font=('courier', 12, 'bold'))
        self.label.grid(column=1, row=0)

        # canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.text = self.canvas.create_text(150, 125, width=280, text="",
                                            font=('Arial', 20, 'italic'), fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # button
        self.img_true = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.img_true, bg=THEME_COLOR, highlightthickness=0, command=self.true_clicked)
        self.true_button.grid(column=0, row=2)
        self.img_false = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.img_false, bg=THEME_COLOR, highlightthickness=0,
                                   command=self.false_clicked)
        self.false_button.grid(column=1, row=2)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text)
        else:
            self.canvas.itemconfig(self.text, text=f"You have completed the quiz"
                                                   f"\nscore: {self.quiz.score}/{self.quiz.question_number}")

            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_clicked(self):
        is_true = self.quiz.check_answer("True")
        self.score_update(is_true)

    def false_clicked(self):
        is_true = self.quiz.check_answer("False")
        self.score_update(is_true)

    def score_update(self, bool_value):
        self.label.config(text=f"Score:{self.quiz.score}")
        if bool_value:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, func=self.get_next_question)