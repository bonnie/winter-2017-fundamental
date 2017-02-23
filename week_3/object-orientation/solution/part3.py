"""Solutions to part 3"""


class Student(object):
    """A student."""

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):
    """Question class"""

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        """Pose a question.

        Shows the user the question, receives their answer,
        and returns True/False for if their answer is correct.
        """

        print self.question,
        answer = raw_input("> ")
        return self.correct_answer == answer


class Exam(object):
    """An exam is a test."""

    def __init__(self, name):
        self.name = name
        self.questions = []

    def add_question(self, question, correct_answer):
        """Add question to exam."""

        question_object = Question(question, correct_answer)
        self.questions.append(question_object)

    def administer(self):
        """Administer a test, returning the score."""

        score = 0

        for question in self.questions:
            if question.ask_and_evaluate():
                score += 1

        return float(score) / len(self.questions)
