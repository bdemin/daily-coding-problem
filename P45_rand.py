# Using a function rand5() that returns an integer from 1 to 5 (inclusive) with
# uniform probability, implement a function rand7() that returns an integer
# from 1 to 7 (inclusive).


import numpy as np


def rand5():
    return np.random.randint(1,6)


def rand7():
    while True:
        # Create a random number on the [0,24] interval
        number = 5 * rand5() + rand5() - 1
        # Narrow down to [0,20]
        if number < 21:
            break
    return number % 7 + 1


# Driver code
occurrences = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0 ,7:0}
for _ in range(1000):
    occurrences[rand7()] += 1
print(occurrences)
