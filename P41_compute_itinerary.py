# Given an unordered list of flights taken by someone, each represented as
# (origin, destination) pairs, and a starting airport, compute the person's
# itinerary. If no such itinerary exists, return null. If there are multiple
# possible itineraries, return the lexicographically smallest one.
# All flights must be used in the itinerary.

# For example, given the list of flights
# [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]
# and starting airport 'YUL', you should return the list
# ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

# Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')]
# and starting airport 'COM', you should return null.

# Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')]
# and starting airport 'A', you should return the list ['A', 'B', 'C', 'A', 'C']
# even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary.
# However, the first one is lexicographically smaller.


# This solution has a worst case of O(n^2). Can be improved.
def compute_itinerary(flights, start):
    itinerary = []
    origin = start
    index = 0

    while index < len(flights):
        if flights[index][0] == origin: # Origin found
            itinerary.append(origin)
            origin = flights[index][1]
            del flights[index]
            index = 0
        else: # Continue searching for flights
            index += 1

    itinerary.append(origin) # Add the final destination

    if flights: # Must use all flights
        return None
    return itinerary


# Driver code
flights =  [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]
start = 'YUL'
assert compute_itinerary(flights, start) == ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']

flights = [('SFO', 'COM'), ('COM', 'YYZ')]
start = 'COM'
assert compute_itinerary(flights, start) == None

flights = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')]
start  = 'A'
assert compute_itinerary(flights, start) == ['A', 'B', 'C', 'A', 'C']
