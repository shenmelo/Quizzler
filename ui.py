from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        self.score_label = Label(text="Score: 0", background=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(
            width=300,
            height=250,
            background="white",
            highlightthickness=0,
            border=0
        )
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="text here",
            fill="Black",
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=true_img, highlightthickness=0, border=0, command=self.is_true)
        self.true_btn.grid(column=0, row=2)
        false_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=false_img, highlightthickness=0, border=0, command=self.is_false)
        self.false_btn.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You have finished the quiz.\n\n"
                                                            f"Thank you!\n\n")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def is_true(self):
        self.answer_feedback(self.quiz.check_answer("True"))

    def is_false(self):
        self.answer_feedback(self.quiz.check_answer("False"))

    def answer_feedback(self, is_right):
        if is_right:
            self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")
        self.window.after(1000, func=self.get_next_question)