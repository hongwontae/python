from question_model import Question;
from data import question_data;
from quiz_brain import QuizBrain

question_bank = []

for d in question_data :
    question_bank.append(Question(d.get('text'), d.get('answer')))

quiz = QuizBrain(question_bank)

while quiz.still_has_question() :
    quiz.next_question()