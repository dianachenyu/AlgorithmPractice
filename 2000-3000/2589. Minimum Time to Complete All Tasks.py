class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        n = len(tasks)
        run = [0] * 2001
        
        tasks.sort(key=lambda x: x[1])
        
        for start, end, duration in tasks:
            for time in range(start, end + 1):
                if run[time]:
                    duration -= 1
                if duration == 0:
                    break
            
            time = end
            while duration > 0:
                duration -= run[time] == 0
                run[time] = 1
                time -= 1
        return sum(run)
                
        
# Greedy
# Intuition: don't work on a task until you have to = work on a task as late as possible
