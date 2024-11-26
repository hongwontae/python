from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import ui

question_bank = []
# question_data => http 요청을 통해 CS 질문 get => list
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    # new_question이라는 객체를 list의 숫자만큼 얻는다.
    new_question = Question(question_text, question_answer)
    # 해당 객체를 전역의 question_bank에 append한다.
    question_bank.append(new_question)


# requests로 받은 응답 정제후 리스트로 만들고 넘김
quiz = QuizBrain(question_bank)
# ui 설계 class 호출
quiz_ui = ui.QuizInterface(quiz)


print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
