#question

class Question:
    def __init__(self, text, choice, answer):
        self.text = text
        self.choice = choice
        self.answer = answer
    def checkAnswer(self, answer):
        return self.answer ==answer

q1 = Question('Elle ... Marianne.', ["m'appelle", "t'appelles", "s'appelle"], "s'appelle")
q2 = Question('Elle ... 20 ans.', ['as', 'ai', 'a', 'avons','avez', 'vont'], 'a')
q3 = Question('Un, deux, ... , quatre', ['cinq', 'trois', 'huit'], 'trois')
# print(q1.text)
# print(q1.checkAnswer(str(input('Answer: '))))

# print(q2.text)
# print(q2.checkAnswer(str(input('Answer: '))))
questionList = [q1, q2, q3]

#quiz
class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0 
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()
        print(f'Question {self.questionIndex + 1 }: {question.text}')

        for q in question.choice:
            print('-' +q)
        answer = (input('Answer: '))
        self.checker(answer)
        self.loadquestion()

    def checker(self, answer):
        question = self.getQuestion()

        if question.checkAnswer(answer):
            self.score += 1

        self.questionIndex += 1

       
    def loadquestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else: 
            self.displayQuestion()
    def showScore(self):
        print(str(self.score) + '/'+ str(len(questionList)))



quiz = Quiz(questionList)
question = quiz.getQuestion
quiz.displayQuestion()