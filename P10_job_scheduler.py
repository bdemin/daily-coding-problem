# Implement a job scheduler which takes in a
# function f and an integer n, and calls f after n milliseconds.


import time


def just_func():
    print('Someone called me!')


def job_scheduler(f, n):
    time.sleep(n/1000)
    f()


# Driver code:
job_scheduler(just_func, 1000)