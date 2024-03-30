listfrom data import question_data
from question_model import QuestionModel
from quiz_brain import QuizBrain


Questions = [QuestionModel(Item["text"],Item["answer"]) for Item in question_data]



with open("Score-Board.txt",mode="w") as File :
    File.write("Hehe") 