"example file to showcase pytestlib"

from testlib import unit_test, Asserts, run_tests


def fib(num: int)->int:
    "returns the fibenaci number of num"
    assert isinstance(num, int)
    assert num >= 0
    if num <= 1:
        return num
    else:
        return fib(num-2) + fib(num-1)


@unit_test
def fibenaci_test():
    "shows that fib works"
    Asserts.equal(fib(0), 0)
    Asserts.equal(fib(1), 1)
    Asserts.equal(fib(2), 1)
    Asserts.equal(fib(3), 2)
    Asserts.equal(fib(4), 3)
    Asserts.equal(fib(5), 5)



if __name__ == "__main__":
    run_tests()
