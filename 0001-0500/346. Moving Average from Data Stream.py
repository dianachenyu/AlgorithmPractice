# Question
# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
# Implement the MovingAverage class:
# - MovingAverage(int size) Initializes the object with the size of the window size.
# - double next(int val) Returns the moving average of the last size values of the stream.
 
# Example 1:
# Input
# ["MovingAverage", "next", "next", "next", "next"]
# [[3], [1], [10], [3], [5]]
# Output
# [null, 1.0, 5.5, 4.66667, 6.0]



class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = collections.deque()
        self.total = 0
        self.count = 0
        

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.total += val
        self.count += 1
        if self.count > self.size:
            lval = self.queue.popleft()
            self.count -= 1
            self.total -= lval
        return self.total/self.count
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

      
# Time O(1)
# Space O(N), N=window size
