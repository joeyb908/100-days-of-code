import random

class QuizBrain:

    def __init__(self, question_bank):
        # QuzBrain class contains attributes of: 
        # question bank - the question bank
        # question - the question (dictionary entry containing text and answer which is technically the memory address of the index)
        # text - actual text of the question
        # answer - actual text of the answer
        
        self.question_bank = question_bank
        self.question = QuizBrain.pick_question(self, question_bank)
        self.text = self.question.q_text
        self.answer = self.question.q_answer
        
    def pick_question(self, question_bank):
        """Randomly select an index in the question_bank and return it"""

        # go to random index and assign question variable, then return the variable
        return question_bank[random.randint(0, len(question_bank)-1)]