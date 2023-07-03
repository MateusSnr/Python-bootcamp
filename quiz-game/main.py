from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)

new_quiz_brain = QuizBrain(question_bank)
new_quiz_brain.update_question()

while new_quiz_brain.still_has_questions():
     new_quiz_brain.update_question()

print("You've completed the quiz")
print(f"Your final score was: {new_quiz_brain.score}/{len(question_bank)}")

#print(question_bank)
#print(question_bank[0].answer)