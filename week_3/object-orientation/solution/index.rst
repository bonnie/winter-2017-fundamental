========
Solution
========

Part I: Discussion
==================

1. *What are the three main design advantages that object orientation can provide?
   Explain each concept.*

   Abstraction
     Allows a programmer to hide certain pieces of their code
     from the interface that other programs or users interact with. By
     properly abstracting, a user of your class doesn't have to understand
     all of the internal details to use it properly, reducing complexity.

   Polymorphism
     Allows for groups to share interchangeable functionality, so that
     component that do the same kinds of things can be used interchangeably.

   Encapsulation
     Means that methods pertaining to certain parts of a program
     stays associated, or "belongs to", that part of the program.
     For example, all of the functionality of an exam can travel in
     an `Exam` class --- import that, and you get all of the parts.

2. *What is a class?*

   A class is a "type of thing" --- like an `Exam`. It can define the
   kind of information that type of thing needs to keep track of,
   as well as actions it needs to perform. You can make individual
   instnaces of classes.

3. *What is an instance attribute?*

   A piece of data (which can be of any type, such as a list, an integer, et al)
   that is assigned to each individual instance. For example, for a `Human`
   class, we could have instance attributes for those things that are
   different from person to person, like eye color, name, etc.

4. *What is a method?*

   A method is a function that is associated to a class.
   A method is like a behavior that a class can execute.

5. *What is an instance in object orientation?*

   An instance is an individual occurrence of an object, the idea made manifest. For a `Exam` class, each individual exam is an instance.

6. *How is a class attribute different than an instance attribute?
   Give an example of when you might use each.*

   Class attributes exist on the class, whereas instance attributes exist on the individual instances, and therefore their values may vary by instance. For example, in a `Cat` class, it would make sense to have a class attribute of `species` (which would have the value `Felis catus` for all Cat instances), and an instance attribute of `name` (which would be different for each Cat instance).

Part 2: Classes and Init Methods
================================

1. Student
----------

.. literalinclude:: part2.py
    :pyobject: Student

2. Question
-----------

.. literalinclude:: part2.py
    :pyobject: Question

3. Exam
-------

.. literalinclude:: part2.py
    :pyobject: Exam

Part 3: Methods
===============

1. Add new question to `Exam`
-----------------------------

.. literalinclude:: part3.py
    :pyobject: Exam.add_question
    :prepend: class Exam(object):  # ...

2. Add method to prompt a question
----------------------------------

.. literalinclude:: part3.py
    :pyobject: Question.ask_and_evaluate
    :prepend: class Question(object):  # ...

3. Add method to administer exam
--------------------------------

.. literalinclude:: part3.py
    :pyobject: Exam.administer
    :prepend: class Exam(object):  # ...

Part 4: Actual Exam
===================

1. Taking Tests
---------------

.. literalinclude:: part4.py
    :pyobject: take_test

2. Example
----------

.. literalinclude:: part4.py
    :pyobject: example

Part 5: Inheritance
===================

.. literalinclude:: part5.py

