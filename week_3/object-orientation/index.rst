.. TODO:
.. Part 3/4/5 Return values of administer functions of Quiz and Exam return different values (Boolean and integer, respectively). Should the Quiz be made to return 0 or 1 for pass fail so that the return type is consistent?

.. Parts 4/5 should use classes to solve the questions posed, currently they just ask student to write functions. Specifically there should be a StudentQuiz/StudentExam class that has the attributes self.exam, self.student, self.score. (Introduction to the idea of middle tables.)

.. also, in part 4, for take_test, we might want to specify what the function should return, if anything.

.. In the discussion questions, we ask the both "what is an instance attribute?" and "how are instance and class attributes different?". The latter seems to entail the former, so we should consider ditching the former question all together.

.. Add in a note about following the spec and why it's important. Lots of people get creative with their attribute and method names.

.. Should we add doctests, so the students *know* when they're not doing what we asked?

.. Is there a way to split this into practice/assessment so that the graded portion is shorter?


=========================
Object Orientation Skills
=========================

Object Orientation Skills is meant to help you practice and assess your understanding of
classes and object orientation in Python.

Follow the directions below to review what you should have learned,
practice implementing classes, and submit an assessment of your understanding.

Take Aways
==========


- know how to define classes with attributes and methods
- understand the difference between instance attributes and class attributes
- know how to instantiate a class with initial parameters
- make a new class from an existing class via inheritance
- be able to explain abstraction, encapsulation, and polymorphism


Assessment
==========

Complete Parts 1 through 5 in the file `assessment.py`.

.. include:: ../assessment.rst

Directions
==========

Part 1: Discussion
------------------

Answer each question in your own words.

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

2. What is a class?

3. What is an instance attribute?

4. What is a method?

5. What is an instance in object orientation?

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

Part 2: Classes and Init Methods
--------------------------------

*Directions:* Make Python classes that could store each of the
following three pieces of data. Use the dictionaries below as examples
to guide you in creating class definitions for the following objects.
Define an `__init__` method to allow callers of this class to provide
initial values for each attribute.

1. Student

   Students can have first and last names and addresses. Here are two
   example students. Write a class that can store data such as this:

   .. code-block:: python

        {'first_name': 'Jasmine',
         'last_name': 'Debugger',
         'address': '0101 Computer Street'}

        {'first_name': 'Jaqui',
         'last_name': 'Console',
         'address': '888 Binary Ave'}

2. Question

   Questions include a question and a correct answer. Here are two example
   questions. Write a class that can store data such as this:

   .. code-block:: python

        {'question': 'What is the capital of Alberta?',
         'correct_answer': 'Edmonton'}

        {'question': 'Who is the author of Python?',
         'correct_answer': 'Guido Van Rossum'}

3. Exam

   Notice that an Exam should have an attribute called `questions`.
   Simply initialize the `questions` attribute as an empty list in the body
   `__init__` function. We'll deal with adding questions to the exam
   later on in this assignment. Your `__init__` function should
   take a `name` for the exam as a parameter.

   .. note:: A Note on Attributes

        Though we've mainly seen attributes that are strings or integers,
        remember: attributes can also be lists and many other data types.
        In the case of our `questions` attribute, we'll have a list of
        `Question` objects.

   For example, here are two exams. Make a class that could store
   data like this:

   .. code-block:: python

        {'name':'Midterm',
         'questions': [

            {'question':'What is the capital of Alberta?',
             'correct_answer': 'Edmonton'},

            {'question': 'Who is the author of Python?',
             'correct_answer': 'Guido Van Rossum' }

          ]
        }

        {'name':'Final',
         'questions': [

            {'question':"Who is Ubermelon's competition?",
             'correct_answer': 'Sqysh'},

            {'question': "What is Balloonicorn's favorite color?",
             'correct_answer': 'Sparkles'}

          ]
        }



Part 3: Methods
---------------

1. Add a method to the `Exam` class which takes a `question` and a
   `correct_answer` as parameters, makes a `Question` from those, and
   adds it to the exam's list of questions.

   For example

   .. parsed-literal::
      :class: console

      $ `python -i assessment.py`:cmd:
      >>> `exam = Exam('midterm')`:cmd:
      >>> `exam.add_question(`:cmd:
      ...     `'What is the method for adding an element to a set?',`:cmd:
      ...     `'.add()')`:cmd:

2. Add a method to the `Question` class that prints the question to the
   console and prompts the user for an answer. It should return `True`
   or `False` depending on whether the correct answer matches the user's
   answer.

   For example

   .. parsed-literal::
      :class: console

      $ `python -i assessment.py`:cmd:
      >>> `question = Question(`:cmd:
      ...     `'What is the method for adding an element to a set?',`:cmd:
      ...     `'.add()')`:cmd:
      >>> `question.ask_and_evaluate()`:cmd:
      What is the method for adding an element to a set? > `.add()`:cmd:
      True


3. Add a method to the `Exam` class which administers all of the exam's
   questions, and **returns** the user's score (as a decimal percentage) at the end.

   So, building on our code from problem 2, here's how the `Exam` class
   should work.

   .. parsed-literal::
      :class: console

      $ `python -i assessment.py`:cmd:
      >>> `exam = Exam('midterm')`:cmd:
      >>> `exam.add_question(`:cmd:
      ...     `'What is the method for adding an element to a set?',`:cmd:
      ...     `'.add()')`:cmd:
      >>> `exam.administer()`:cmd:
      What is the method for adding an element to a set? > `.add()`:cmd:
      1.0

   .. hint:: Here's some pseudocode for the `administer` method.

     Inside the `Exam.administer` method, you'll need to first
     initialize a variable called `score`; set it to zero.

     Next, loop through each of the questions in the exam.

     For each question, call the question's method from Problem #2 --- `ask_and_evaluate`.

     If the return value of `ask_and_evaluate` is `True`, increment the `score`.

     After the last question has been administered, calculate and return the percentage score.


Part 4: Create an actual exam!
------------------------------

.. warning:: Create functions, not methods!

  Part 4 doesn't require you to modify the class definitions you've
  created in the previous 3 parts of this assignment. Simply *use* the
  classes you've defined.

1. Write a *function*, `take_test`, that takes an Exam and a Student
   as parameters, administers the exam, and assigns the score to the
   student instance as a new attribute called **score**. This function should also print a message to the screen indicating the score.

2. Write a function, `example`, which does the following:

   - Creates an exam

   - Adds a few questions to the exam

     - These should be part of the function; no need to prompt the
       user for questions.

   - Creates a student

   - Administers the test for that student using the take test function you just wrote

Part 5: Inheritance
-------------------

A "quiz" is like an exam --- it's a set of questions that students
are prompted to answer. However, whereas exams are given a raw score (or
more conveniently, a percentage score),
quizzes are pass/fail: if you answered at least half of the questions
correctly, you pass the quiz. When you call the `administer` method on
a quiz, it should only return `True` if you passed or `False` if you failed.

Think about how we could solve this requirement: we have an `Exam` class
and we want to have a `Quiz` class that is similar.

Write code to solve this problem. Incorporate as many of the "design" parts
of the class lectures as you feel comfortable with.
