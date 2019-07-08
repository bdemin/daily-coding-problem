# The area of a circle is defined as πr^2.
# Estimate π to 3 decimal places using a Monte Carlo method.
# Hint: The basic equation of a circle is x^2 + y^2 = r^2.


# P(point inside circle) = πr^2 / (2r)^2 = π/4
# π = 4*P(point inside circle)


import numpy as np


def monte_carlo():
    radius = 1

    insidePoints = 0
    totalPoints = 0

    accuracy = 1e-7
    lastP = 0
    while True:
        point = np.random.rand(2)
        if point[0]**2 + point[1]**2 < radius:
            insidePoints += 1
        totalPoints += 1

        newP = insidePoints/totalPoints
        if lastP != newP:
            if abs(lastP - newP) < accuracy:
                return 4 * newP
        lastP = newP
    

# Driver code:
result = monte_carlo()
print("{0:0.2f}".format(result))