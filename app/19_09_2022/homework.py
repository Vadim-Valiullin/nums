
class Question:
    def __init__(self, question, difficulty, right_answer):
        self.question = question
        self.difficulty = difficulty
        self.right_answer = right_answer
        self.score = 0
        self.asked = False
        self.answer = None

    def get_points(self):
        return self.difficulty * 10 if self.is_correct() else 0

    def is_correct(self):
        return self.answer == self.right_answer

    def build_question(self):
        print(f'Вопрос: {self.question}\nСложность {self.difficulty}/5')

    def build_feedback(self):
        if self.is_correct():
            print(f'Ответ верный, получено {self.score} баллов')
        else:
            print(f'Ответ неверный, верный ответ: {self.right_answer}')







