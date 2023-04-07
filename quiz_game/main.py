from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [] #starting out with an empty list
for question in question_data: #populating the question bank list with each of the question/answers in the dictionary
    question_text = question["text"] #grabs each dictionary key text and saves it in the list
    question_answer = question["answer"] #grabs each dictionary answer and saves it in the list with its question
    new_question = Question(q_text=question_text, q_answer=question_answer)#builds the question object
    question_bank.append(new_question) #appends each question object into the question_bank list as it goes
    # through the for loop

quiz = QuizBrain(question_bank)
while quiz.still_has_questions(): #checks to see if there is unused questions in the question bank
    quiz.next_question() #asks the question in the list order

print(f"You completed the quiz.  Your final score was: {quiz.score} / {quiz.question_number}.")


