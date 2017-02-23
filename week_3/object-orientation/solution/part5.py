"""Solutions to part 5."""

from part3 import Exam


class Quiz(Exam):
    """Quizzes for students.

    A quiz is like an exam, except that it is pass/fail.
    A quiz passes if more than 50% of answers are correct.
    """

    def administer(self):
        """Administer a quiz."""

        score = super(Quiz, self).administer()
        return score > 0.5


def example():
    """Show usage of quiz, questions, and student."""

    quiz = Exam('Monday Quiz')

    quiz.add_question(
        'What is the parent class for a non-inheriting Python '
        'class?',
        'object')

    quiz.add_question(
        'Which special method determines how objects should be '
        'represented?',
        '__repr__')

    quiz.add_question(
        'What is the greatest programming language ever?',
        'Python')  # note from Joel: actual answer: LISP

    passed = quiz.administer()

    if passed:
        print "You passed!"

    else:
        print "Oh no! You failed!"
