from heapq import *


class RunningMedian:
    count = 0
    current_sum = 0
    def __init__(self):
        self.small = []  # smaller half, max heap - negate the values while storing in list
        self.large = []  # larger half, min heap
    
    def add(self, num): #add number to the right heap
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))
        self.count = self.count + 1
        self.current_sum = self.current_sum + num
            
            # find the median
    def findMedian(self):
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])

    # find the number of contributions
    def size(self):
        return self.count

    # find the sum of contributions
    def cur_sum(self):
        return self.current_sum
