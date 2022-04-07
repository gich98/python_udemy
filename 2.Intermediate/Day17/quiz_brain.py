class QuizBrain:

    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def next_question(self):
        question = self.questions_list[self.question_number]
        correct_answer = question.answer
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question.text} (True/False)? ").capitalize()
        self.check_answer(user_answer, correct_answer)
        return self.score == self.question_number

    def still_has_questions(self):
        if self.question_number < len(self.questions_list):
            return True
        else:
            print("You answer all the questions correctly!")
            return False

    def check_answer(self, user_answer, correct_answer):
        is_correct = False
        if user_answer == correct_answer:
            print("You got it right!")
            self.score += 1
            is_correct = True
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        return is_correct
