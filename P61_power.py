# Implement integer exponentiation. That is, implement the pow(x, y) function,
# where x and y are integers and returns x^y.

# Do this faster than the naive method of repeated multiplication.

# For example, pow(2, 10) should return 1024.


import time


# Execution time measuring decorator by Fahim Sakri (https://medium.com/pythonhive/python-decorator-to-measure-the-execution-time-of-methods-fa04cb6bb36d#targetText=To%20overcome%20this%2C%20created%20the,timeit%20decorator%20on%20the%20method.&targetText=The%20code%20will%20look%20like%20this%20after%20removing%20the%20redundant%20code.)
def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print('%r  %2.2f ms' % (method.__name__, (te - ts) * 1000))
        return result
    return timed


# Simple O(n) solution
@timeit
def regular_pow_func(x, y):
    # return x**y
    result = 1
    while y:
        result *= x
        y -= 1
    return result


# O(log(n)) recursive solution
@timeit
def _pow(x, y):
    return rec(x,y)

def rec(x, y):
    # Recursive function to calculate the exponential
    if y == 0:
        return 1
    elif y % 2 == 0:
        res = rec(x, y/2)
        return res*res
    else:
        return rec(x, y-1) * x


# Driver code
pairs = [(2, 4), (2, 0), (10, 10000), (10, 100000)]
for base, exp in pairs:
    _pow(base, exp)
    regular_pow_func(base, exp)
