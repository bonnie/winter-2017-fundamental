"""Solutions to part 2."""


class Student(object):
    """Student."""

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):
    """A question in an exam."""

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer


class Exam(object):
    """An exam is a test.

    Exams comprise zero or more questions.
    """

    def __init__(self, name):
        self.name = name
        self.questions = []
