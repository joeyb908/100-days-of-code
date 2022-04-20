from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

def gen_question_bank():
    """Generate a question valid iterable question bank based on classes"""

    # my method
    # loop through each index in question_data
    # then input the value for text and answer into a class
    # into each index

    # empty list to hold question and answers
    questions_and_answers = []
    # generate a list with range of question_data length
    for ind in range(0, len(question_data)):
        # assign variable question with question class with the actual                 question and answer then append it to the list
        question = Question(question_data[ind]["text"], question_data[ind]["answer"])   
        questions_and_answers.append(question)

    # teacher method
        
    # generate question bank list
    # question_bank = []

    # for each question in question_data
    # grab the text, answer, and create a new variable that
    # is an object of Question's class with text and answer within
    # then, append it to the list
        
    # for question in question_data:
    #     question_text = question['text']
    #     question_answer = question['answer']
    #     new_question = Question(question_text, question_answer)
    #     question_bank.append(new_question)


    return questions_and_answers

def true_or_false():
    """Has user guess either 'true' or 'false'"""

    # simple answer loop that prevents false answers
    guessing = True
    while guessing:
        guess = input(f"Is this true or false? ").lower()
        if guess == "true" or guess == "false":
            guessing = False


    return guess
    

def calculate_win(computer_answer, user_score, question_num):
    """Determines if the user guessed correctly"""

    # assigns variable guess with result of 'true' or 'false'
    guess = true_or_false()

    # compares answers to computer generated answer in quiz_brain
    if guess == computer_answer:
        new_score = user_score + 1
        print(f"Congrats, {computer_answer} is the right choice!\nYour score is now {new_score}/{question_num}")
        return new_score
    else:
        print(f"Sorry, the correct answer is {computer_answer}.\nYou scored {user_score} in a row!\n Your score is now {user_score}/{question_num}")
        return user_score
        
guessing = True
score = 0
question_number = 1
while guessing != "stop":
    question_bank = gen_question_bank()
    quiz_brain = QuizBrain(question_bank)
    quiz_brain.pick_question(question_bank)
    question = quiz_brain.text
    answer = quiz_brain.answer.lower()
    print(f"Q.{question_number}: {question}")
    score = calculate_win(answer, score, question_number)
    question_number += 1
    guessing = input("Do you want to continue? If yes, hit enter, if not, type 'stop'.\n")
    print("\033c")
    if guessing == "stop":
        print(f"Your final score was {score}/{question_number}")