# lab02 tests


# IMPORTS

import labs.lab02 as lab
import tests.wwpd_storage as s
from operator import add, mul, mod, sub
from io import StringIO 
import sys
import git

st = s.wwpd_storage


# CAPTURING PRINTS (STDOUT) - https://stackoverflow.com/questions/16571150/how-to-capture-stdout-output-from-a-python-function-call

class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio
        sys.stdout = self._stdout


# COLORED PRINTS - custom text type to terminal: https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal, ANSI colors: http://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html

class bcolors:
    HIGH_MAGENTA = '\u001b[45m'
    HIGH_GREEN = '\u001b[42m'
    HIGH_YELLOW = '\u001b[43m'
    MAGENTA = ' \u001b[35m'
    GREEN = '\u001b[32m'
    YELLOW = '\u001b[33;1m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\u001b[0m'
    
def print_error(message):
    print("\n" + bcolors.HIGH_YELLOW + bcolors.BOLD + "ERROR:" + bcolors.RESET + bcolors.YELLOW + bcolors.BOLD + " " + message + bcolors.ENDC)

def print_message(message):
    print("\n" + bcolors.HIGH_MAGENTA + bcolors.BOLD + "MESSAGE:" + bcolors.RESET + bcolors.MAGENTA + bcolors.BOLD + " " + message + bcolors.ENDC)

def print_success(message):
    print("\n" + bcolors.HIGH_GREEN + bcolors.BOLD + "SUCCESS:" + bcolors.RESET + bcolors.GREEN + bcolors.BOLD + " " + message + bcolors.ENDC)


# REFERENCE FUNCTIONS

square = lambda x: x * x
identity = lambda x: x
triple = lambda x: 3 * x
increment = lambda x: x + 1
odd = lambda x: x % 2 == 1
greater_than_5 = lambda x: x > 5
is_even = lambda x: x % 2 == 0
is_div_by_five = lambda x: x % 5 == 0
add_one = lambda x: x + 1
square = lambda x: x**2
times_two = lambda x: x * 2
add_three = lambda x: x + 3


# TESTS 

def test_lambda_curry2():
    assert lab.lambda_curry2(add)(5)(3) == 8
    assert lab.lambda_curry2(mul)(5)(42) == 210
    assert lab.lambda_curry2(mod)(123)(10) == 3
    assert lab.lambda_curry2(sub)(25)(9) == 16


def test_count_cond():
    count_factors = lab.count_cond(lambda n, i: n % i == 0)
    assert count_factors(2) == 2
    assert count_factors(4) == 3
    assert count_factors(12) == 6

    is_prime = lambda n, i: count_factors(i) == 2
    count_primes = lab.count_cond(is_prime)
    assert count_primes(2) == 1
    assert count_primes(3) == 2
    assert count_primes(4) == 2
    assert count_primes(5) == 3
    assert count_primes(20) == 8


def test_composite_identity():
    assert lab.composite_identity(square, add_one)(0) == True
    assert lab.composite_identity(square, add_one)(4) == False


def test_cycle():
    new_cycle = lab.cycle(add_one, times_two, add_three)
    assert new_cycle(0)(5) == 5
    assert new_cycle(2)(1) == 4
    assert new_cycle(3)(2) == 9
    assert new_cycle(4)(2) == 10
    assert new_cycle(6)(1) == 19


def test_make_keeper():
    print("\n\nmake_keeper(5)(is_even) prints:")
    with Capturing() as make_keeper_5_even_output:
        lab.make_keeper(5)(is_even)
    make_keeper_5_even = ['2', '4']
    if make_keeper_5_even != make_keeper_5_even_output:
        print_error("Incorrect prints from make_keeper(5)")
    assert make_keeper_5_even == make_keeper_5_even_output
    if lab.make_keeper(5)(is_even) is not None:
        print_error("Print, do not return.")
    assert lab.make_keeper(5)(is_even) is None  


    print("\n\nmake_keeper(16)(is_div_by_five) prints:")
    with Capturing() as make_keeper_16_div_output:
        lab.make_keeper(16)(is_div_by_five)
    make_keeper_16_div = ['5', '10', '15']
    if make_keeper_16_div != make_keeper_16_div_output:
        print_error("Incorrect prints from make_keeper(16)(is_div_by_five)")
        assert make_keeper_16_div == make_keeper_16_div_output   
    if lab.make_keeper(16)(is_div_by_five) is not None:
        print_error("Print, do not return.")
    assert lab.make_keeper(16)(is_div_by_five) is None 


def test_match_k():
    assert lab.match_k(2)(1010) == True
    assert lab.match_k(2)(2010) == False
    assert lab.match_k(1)(1010) == False
    assert lab.match_k(1)(1) == True
    assert lab.match_k(1)(2111111111111111) == False
    assert lab.match_k(3)(123123) == True
    assert lab.match_k(2)(123123) == False


def test_product():
    assert lab.product(3, identity) == 6
    assert lab.product(5, identity) == 120
    assert lab.product(3, square) == 36
    assert lab.product(5, square) == 14400
    assert lab.product(3, increment) == 24
    assert lab.product(3, triple) == 162


def test_accumulate():
    assert lab.accumulate(add, 0, 5, identity) == 15
    assert lab.accumulate(add, 11, 5, identity) == 26
    assert lab.accumulate(add, 11, 0, identity) == 11
    assert lab.accumulate(add, 11, 3, square) == 25
    assert lab.accumulate(mul, 2, 3, square) == 72
    assert lab.accumulate(lambda x, y: x + y + 1, 2, 3, square) == 19
    assert lab.accumulate(lambda x, y: 2 * x * y, 2, 3, square) == 576
    assert lab.accumulate(lambda x, y: (x + y) % 17, 19, 20, square) == 16

def test_add_using_accum():
    assert lab.add_using_accum(5, square) == 55
    assert lab.add_using_accum(5, triple) == 45


def test_multiply_using_accum():
    assert lab.multiply_using_accum(4, square) == 576
    assert lab.multiply_using_accum(6, triple) == 524880


def test_filtered_accum():
    assert lab.filtered_accum(add, 0, lambda x: True, 5, identity) == 15
    assert lab.filtered_accum(add, 11, lambda x: False, 5, identity) == 11
    assert lab.filtered_accum(add, 0, odd, 5, identity) == 9
    assert lab.filtered_accum(mul, 1, greater_than_5, 5, square) == 3600


def test_funception():
    assert lab.funception(add_one, 0)(3) == 6
    assert lab.funception(add_one, 1)(4) == 24
    assert lab.funception(add_one, 3)(2) == 4
    assert lab.funception(add_one, -2)(-3) is None
    assert lab.funception(add_one, -1)(4) is None


# CHECK WWPD? IS ALL COMPLETE

wwpd_complete = True

def test_wwpd():
    if len(st) != 28 or not all([i[4] for i in st]):
        print_error("WWPD? is incomplete.")
        wwpd_complete = False
    assert len(st) == 28
    assert all([i[4] for i in st])


# AUTO-COMMIT WHEN ALL TESTS ARE RAN

user = []

def test_commit():
    try:
        # IF CHANGES ARE MADE, COMMIT TO GITHUB
        user.append(input("\n\nWhat is your GitHub username (exact match, case sensitive)?\n"))
        repo = git.Repo("/workspaces/lab02-" + user[0])
        repo.git.add('--all')
        repo.git.commit('-m', 'update lab')
        origin = repo.remote(name='origin')
        origin.push()
        print_success("Changes successfully committed.")  
    except git.GitCommandError: 
        # IF CHANGES ARE NOT MADE, NO COMMITS TO GITHUB
        print_message("Already up to date. No updates committed.")
    except git.NoSuchPathError:
        # IF GITHUB USERNAME IS NOT FOUND
        print_error("Incorrect GitHub username; try again.")
        raise git.NoSuchPathError("")