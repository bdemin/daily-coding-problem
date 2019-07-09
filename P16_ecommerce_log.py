# You run an e-commerce website and want to record the last N
# order ids in a log. Implement a data structure to accomplish this,
# with the following API:

# record(order_id): adds the order_id to the log
# get_last(i): gets the ith last element from the log.
# i is guaranteed to be smaller than or equal to N.
# You should be as efficient with time and space as possible.


class Log():
    def __init__(self, N):
        self.N = N
        self.log = [None] * N
        self.index = 0

    def record(self, order_id):
        self.log[self.index] = order_id
        self.index += 1
        if self.index == len(self.log):
            self.index = 0
        

    def get_last(self, i):
        start = self.index - i - 1
        if start < 0:
            return self.log[len(self.log) + start]
        else:
            return self.log[start]


# Driver code:
log = Log(5)
for i in range(5):
    log.record(i)
log.record(10)
log.record(20)
log.record(30)
print(log.log)
print(log.get_last(0))
print(log.get_last(1))
print(log.get_last(2))
print(log.get_last(3))
print(log.get_last(4))