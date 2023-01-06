# lab02 WWPD?

# IMPORTS

import inspect
import tests.wwpd_storage as s

st = s.wwpd_storage 

# COLORED PRINTS - custom text type to terminal: https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal, ANSI colors: http://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html

class bcolors:
    HIGH_MAGENTA = '\u001b[45m'
    HIGH_GREEN = '\u001b[42m'
    HIGH_YELLOW = '\u001b[43;1m'
    HIGH_RED = '\u001b[41m'
    HIGH_BLUE = '\u001b[44m'
    MAGENTA = ' \u001b[35m'
    GREEN = '\u001b[32m'
    YELLOW = '\u001b[33;1m'
    RED = '\u001b[31m'
    BLUE = '\u001b[34m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\u001b[0m'


# INCORRECT ANSWER LOOP, INSTRUCTIONS, COMPLETE, OPTIONS

def repeat():
    print("Try again:")
    return input()

def intro(name):
    print("\nWhat Would Python Display?: " + name)
    print("Type the expected output, 'function' if you think the answer is a function object, 'infinite loop' if it loops forever, 'nothing' if nothing is displayed, or 'error' if it errors; use single quotes '' when needed.\n")

def complete():
    print(bcolors.HIGH_GREEN + bcolors.BOLD + "\nSUCCESS: All questions for this question set complete." + bcolors.ENDC)

def options():

    print(bcolors.HIGH_MAGENTA + bcolors.BOLD + "\nMESSAGE: All questions for this question set complete. Restart question set?" + bcolors.ENDC)
    guess = input("Y/N?\n")
    guess = guess.lower()
    while guess != "y" and guess != "n":
        print(bcolors.HIGH_YELLOW + bcolors.BOLD + "\nUnknown input, please try again." + bcolors.ENDC)
        guess = input()
    if guess == "y":
        return "restart"
    return False


# WWPD? ALGORITHM 

def wwpd(name, question_set, stored_list):

    intro(name)

    match_elems1 = [[question_set[i][0], question_set[i][2]] for i in range(len(question_set))]
    match_elems2 = [[stored_list[i][0], stored_list[i][1]] for i in range(len(stored_list))]

    restart = str(match_elems1)[1:-1] in str(match_elems2) and options() == "restart"

    done = False
    for i in question_set:
        group = [i[0], i[2], i[3], True]
        if group not in stored_list or restart:
            done = True 
            if i[1]:
                print(i[1])
            if i[2]:
                print(i[2])
            guess = input()
            while guess != i[3]:
                guess = repeat()
            if str(match_elems1)[1:] not in str(match_elems2):
                op = open("tests/wwpd_storage.py", "w")
                if not stored_list:
                    stored_list = [group]
                else:
                    for j in range(len(stored_list)):
                        if group[0] < stored_list[j][0]:
                            stored_list.insert(j, group)
                            break
                    stored_list.append(group)
                op.write("wwpd_storage = " + str(stored_list))
                op.close()
    if done:
        complete()


# REFERENCE FUNCTIONS

a = lambda x: x
b = lambda x: lambda: x
c = b(88)
d = lambda f: f(4)

def square(x):
    return x * x

z = 3
e = lambda x: lambda y: lambda: x + y + z

higher_order_lambda = lambda f: lambda x: f(x)
g = lambda x: x * x
call_thrice = lambda f: lambda x: f(f(f(x)))
print_lambda = lambda z: print(z)


def even(f):
    def odd(x):
        if x < 0:
            return f(-x)
        return f(x)
    return odd

steven = lambda x: x

def cake():
    print('beets')
    def pie():
        print('sweets')
        return 'cake'
    return pie

def snake(x, y):
    if cake == more_cake:
        return chocolate
    else:
        return x + y


# QUESTION SET - ELEMENT FORMAT: [<QUESTION #>, <INITIAL PRINTS> (usually empty), <QUESTION>, <ANSWER>, <COMPLETE?>]
# INSPECT MODULE - convert function body into String: https://docs.python.org/3/library/inspect.html 

lambda_qs = [
    ["", ">>> lambda x: x", "function"],
    [">>> a = lambda x: x # Assigning the lambda function to the name a", ">>> a(5)", str(a(5))],
    ["", ">>> (lambda: 3)()  # Using a lambda expression as an operator in a call exp.", str((lambda: 3)())],
    [">>> b = lambda x: lambda: x  # Lambdas can return other lambdas!/n>>> c = b(88)", ">>> c", "function"],
    ["", ">>> c()", str(c())], 
    [inspect.getsorce(square) + "\n>>> d = lambda f: f(4) # They can have functions as arguments as well.", ">>> d(square)", str(d(square))], 
    [">>> x = None\n>>> x", ">>> lambda x: x", "function"], 
    [">>> z = 3\n>>>e = lambda x: lambda y: lambda: x + y + z", ">>> e(0)(1)()", str(e(0)(1)())], 
    [">>> f = lambda z: x + z", ">>> f(3)", "error"], 
    [">>> higher_order_lambda = lambda f: lambda x: f(x)\n>>> g = lambda x: x * x", ">>> higher_order_lambda(2)(g) # Which argument belongs to which function call?", "error"],
    ["", ">>> higher_order_lambda(g)(2)", str(higher_order_lambda(g)(2))], 
    [">>> call_thrice = lambda f: lambda x: f(f(f(x)))", ">>> call_thrice(lambda y: y + 1)(0)", str(call_thrice(lambda y: y + 1)(0))], 
    [">>> print_lambda = lambda z: print(z)  # When is the return expression of a lambda expression executed?", ">>> print_lambda", "function"],
    ["", ">>> one_thousand = print_lambda(1000)", "1000"], 
    ["", ">>> one_thousand", "nothing"]
]
    
lambda_qs = [[i + 1] + lambda_qs[i] + [False] for i in range(len(lambda_qs))]

hofs_qs = [
    ["\n" + inspect.getsource(even) + ">>> steven = lambda x: x\n>>> stewart = even(steven)", ">>> steward", "function"],
    ["", ">>> steward(61)", str(even(steven)(61))], 
    ["", ">>> stewart(-4)", str(even(steven)(-4))],
    ["\n" + inspect.getsource(cake), ">>> chocolate = cake()", "beets"],
    ["", ">>> chocolate", "function"],
    ["", ">>> chocolate()", "sweets"],
    ["", "", "'cake'"],
    ["", ">>> more_chocolate, more_cake = chocolate(), cake", "sweets"],
    ["", ">>> more_chocolate", "'cake'"],
    ["\n" + inspect.getsource(snake), ">>> snake(10, 20)", "function"],
    [">>> cake = 'cake'", ">>> snake(10, 20)", "30"]
]

hofs_qs = [[i + 1] + hofs_qs[i] + [False] for i in range(len(hofs_qs))] 


#WWPD? QUESTIONS

def wwpd_lambdas():
    wwpd("Lambdas", lambda_qs, st)

def wwpd_hofs():
    wwpd("HOFs", hofs_qs, st)

wwpd_lambdas()