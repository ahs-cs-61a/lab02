# lab02 tests

import labs.lab02 as lab
from operator import add, mul, mod, sub
from io import StringIO 
import sys


# capturing prints (stdout)
class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio
        sys.stdout = self._stdout
        

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
    print("\n\nmake_keeper prints:")
    assert lab.make_keeper(5)(is_even) is None  # print, don't return 
    assert lab.make_keeper(16)(is_div_by_five) is None  # print, don't return 


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
