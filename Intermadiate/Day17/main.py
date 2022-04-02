from Intermadiate.Day17 import data
from Intermadiate.Day17.question_model import Question
from Intermadiate.Day17.quiz_brain import QuizBrain

question_bank = []
is_correct = True

for _ in data.question_data:
    question_bank.append(Question(_["text"], _["answer"]))

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions() and is_correct:
    is_correct = quiz_brain.next_question()
