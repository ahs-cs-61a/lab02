# lab02 wwpd

import inspect

# preliminaries

def repeat():
    print("try again:")
    return input()


def intro():
    print("What Would Python Display?")
    print(
        "type the expected output, 'function' if you think the answer is a function object, 'infinite loop' if it loops forever, 'nothing' if nothing is displayed, or 'error' if it errors; use single quotes '' when needed\n"
    )


def outro():
    print("\nall questions for this question set complete")


# reference functions


def square(x):
    return x * x


# wwpd questions


def wwpd_lambdas():
    intro()
    
    print(">>> lambda x: x")
    x = input()
    while x != 'function':
        x = repeat()

    print(">>> a = lambda x: x  # Assigning the lambda function to the name a")
    print(">>> a(5)")
    x = input()
    while x != "5":
        x = repeat()

    print(">>> (lambda: 3)()  # Using a lambda expression as an operator in a call exp.")
    x = input()
    while x != 3:
        x = repeat()

    print(">>> b = lambda x: lambda: x  # Lambdas can return other lambdas!")
    print(">>> c = b(88)")
    print(">>> c")
    x = input()
    while x != 'function':
        x = repeat()
    print(">>> c()")
    x = input()
    while x != '88':
        x = repeat()

    print(">>> d = lambda f: f(4) # They can have functions as arguments as well.")
    print(inspect.getsource(square))
    print(">>> d(square)")
    x = input()
    while x != '16':
        x = repeat()

    print(">>> x = None")
    print("x")
    print(">>> lambda x: x")
    x = input()
    while x != 'nothing':
        x = repeat()

    print(">>> z = 3")
    print(">>> e = lambda x: lambda y: lambda: x + y + z")
    print(">>> e(0)(1)()")
    x = input()
    while x != "4":
        x = repeat()

    print(">>> f = lambda z: x + z")
    print(">>> f(3)")
    x = input()
    while x != "error":
        repeat()

    print(">>> higher_order_lambda = lambda f: lambda x: f(x)")
    print(">>> g = lambda x: x * x")
    print(">>> higher_order_lambda(2)(g) # Which argument belongs to which function call?")
    x = input()
    while x != "error":
        x = repeat()
    
    print(">>> higher_order_lambda(g)(2)")
    x = input()
    while x != "4":
        x = repeat()

    print(">>> call_thrice = lambda f: lambda x: f(f(f(x)))")
    print(">>> call_thrice(lambda y: y + 1)(0)")
    x = input()
    while x != "3":
        x = repeat()

    print(">>> print_lambda = lambda z: print(z)  # When is the return expression of a lambda expression executed?")
    print(">>> print_lambda")
    x = input()
    while x != "function":
        x = repeat()
    print(">>> one_thousand = print_lambda(1000)")
    x = input()
    while x != "1000":
        x = repeat()
    print(">>> out_thousand")
    x = input()
    while x != "nothing":
        x = repeat()