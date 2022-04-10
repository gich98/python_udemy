from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 12, "normal"))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.question = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Question",
            font=("Arial", 16, "italic"),
            fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.is_true)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.is_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz_brain.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz_brain.score}")
            question = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question, text=question)
        else:
            self.canvas.itemconfig(self.question, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def is_true(self):
        self.color_canvas(self.quiz_brain.check_answer("True"))

    def is_false(self):
        self.color_canvas(self.quiz_brain.check_answer("False"))

    def color_canvas(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
