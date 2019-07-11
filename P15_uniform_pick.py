# Given a stream of elements too large to store in memory,
# pick a random element from the stream with uniform probability.


import numpy as np


# Length is known
def uniform_pick(stream):
    randIndex = np.random.randint(len(stream))
    return stream[randIndex]


# Driver code
stream = [1,2,4,7,4]
for i in range(100):
    result = uniform_pick(stream)
    # print(result)



# Length is unknown (https://github.com/r1cc4rdo/daily_coding_problem/blob/master/daily_coding_problem_11_15.py)
def sample_gen_func(num):
    for x in range(num):
        yield x

def uniform_pick_2(stream):
    sampleCount = 0
    selectedSample = None

    for sample in stream:
        sampleCount += 1
        if np.random.rand() <= 1.0 / sampleCount:
            selectedSample = sample
    return selectedSample



N = 3
print(uniform_pick_2(sample_gen_func(N)))