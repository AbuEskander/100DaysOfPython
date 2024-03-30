from data import question_data
class QuestionModel:
    def __init__(self,text,ans) -> None:
        self.text = text
        self.ans =  ans
    

Questions = [QuestionModel(Item["text"],Item["answer"]) for Item in question_data]
