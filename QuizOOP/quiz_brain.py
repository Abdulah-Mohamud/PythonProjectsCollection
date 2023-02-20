class QuizBrain:
    def __init__(self, q_bank):
        self.question_number = 0
        self.question_list = q_bank

    def next_question(self):
        current_question = self.question_list[self.question_number]
        input(f"{current_question}, True or False?")



