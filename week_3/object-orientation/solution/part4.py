"""Solutions for part 4."""

from part3 import Exam, Student


def take_test(student, exam):
    """Administer exam to student and record score on student."""

    student.score = exam.administer()

    print "Your score is %2f percent." % (student.score * 100)


def example():
    """Show usage of exam, questions, and student."""

    exam = Exam('midterm')

    exam.add_question(
        'What is the parent class for a non-inheriting Python '
        'class?',
        'object')

    exam.add_question(
        'Which special method determines how objects should be '
        'represented?',
        '__repr__')

    exam.add_question(
        'Which special method determines how to initialize '
        'instances?',
        '__init__')

    exam.add_question(
        'What is the greatest programming language ever?',
        'Python')  # note from Joel: actual answer: LISP

    student = Student(
        'Jasmine',
        'Debugger',
        '1010 Computer Street')

    take_test(student, exam)
