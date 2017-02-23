
class Student(object):
    """A class to hold students"""

    def __init__(self, fname, lname, addy):
        """initialize a new student"""

        self.first_name = fname
        self.last_name = lname
        self.address = addy

class Question(object):
    """class to hold Questions and their correct answers"""

    def __init__(self, ques, ans):
        """initialize a new question"""

        self.question = ques
        self.correct_answer = ans

    # existential_question = Question('Why?', 'Because')

    def ask_and_answer(self):
        """ask the user the question, return whether answer was correct"""

        user_answer = raw_input(self.question + ' ')

        if user_answer == self.correct_answer:
            return True

        return False


# existential_question.ask_and_answer()

class Exam(object):
    """class to hold an exam with questions"""

    def __init__(self, exam_name):
        """initialize a new exam with a name, and no questions"""

        self.name = exam_name
        self.questions = []


    def add_question(self, question, correct_answer):
        """add a question to the exam"""

        # make a question object
        current_question = Question(question, correct_answer)

        # append to questions attribute
        self.questions.append(current_question)


    def administer(self):
        """administer the exam"""

        # initialize the tally of correct answers
        total_correct = 0

        for exam_question in self.questions:

            # ask the question
            result = exam_question.ask_and_answer()

            if result is True:
                total_correct += 1


        # calculate score
        return float((total_correct) * 100)/len(self.questions) 


# cs101.add_question




# class HackbrightStudent(Student):

#     school = 'Hackbright'




# class Cat(Animal):

#     sound = 'Meow'