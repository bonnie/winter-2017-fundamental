"""a file to demonstrate functions"""

def get_nonchocolate_cupcakes(cupcakes):
    """return a list of non-chocolate cupcakes from input list

    this function looks through the cupcake names
    from the input list (cupcakes) and returns a
    list of the names that don't include the word
    chocolate (chocolate must be in lowercase in
    the cupcake name to be eliminated)
    """

    nonchocolate_cupcakes = []

    for cupcake in cupcakes:
        if 'chocolate' not in cupcake:
            nonchocolate_cupcakes.append(cupcake)

    return nonchocolate_cupcakes

tuesday_cupcake_flavors = ['chocolate', 'chocolate brownie',
                          'double chocolate', 'vanilla', 'red velvet']

# print "calling get_nonchocolate_cupcakes on tuesday flavors"
# tuesday_nochocolate = get_nonchocolate_cupcakes(tuesday_cupcake_flavors)
# for flavor in tuesday_nochocolate:
#     print "{} is a tuesday flavor".format(flavor)


# wednesday_cupcake_flavors = ['red velvet', 'mint cookie',
#                             'devils food', 'rocky road', 'Death by Chocolate']
# print "calling get_nonchocolate_cupcakes on wednesdays flavors"
# wednesday_nonchocolate = get_nonchocolate_cupcakes(wednesday_cupcake_flavors)
# for flavor in wednesday_nonchocolate:
#     print "{} is a wednesday flavor".format(flavor)

thursday_cupcake_flavors = [1, 2, 3, 7]
thursday_flavors = get_nonchocolate_cupcakes(thursday_cupcake_flavors)


def greet_students(students):
    """print a greeting for each student in input list. Return None"""

    for student in students:
        print "Hello", student

def is_student_in_cohort(student, cohort_students):
    """return True or False depending on whether student is in cohort_students"""

    if student in cohort_students:
        return True
    else:
        return False




