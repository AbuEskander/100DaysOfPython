class QuizBrain :
    def __init__(self,Questions) -> None:
        self.questionNum = 0
        self.questionList = Questions 
    def next_question(self)-> object:
        self.questionNum +=1
        return self.questionList[self.questionNum]
    def showQuestion(self)->None:
        Ans = input(f"Q.{self.questionNum+1} {self.questionList[self.questionNum].text}? (True or False)")
        if Ans == self.questionList[self.questionNum].ans:
            if self.questionNum + 1 >= len(self.questionList): return 
            self.next_question()
            self.showQuestion()
        else:
            print("Wrong")
            self.showQuestion()