# Method 1
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        counter = []
        for start, end in flowers:
            counter.append([start, 1])
            counter.append([end + 1, -1])
        counter.sort()
        
        count = 0
        times = [0]
        status = {0:0}
        for time, change in counter:
            count += change
            if not times or times[-1] != time:
                times.append(time)
            status[time] = count

        res = []
        for time in persons:
            idx = bisect.bisect(times, time)
            check_time = times[idx - 1]
            res.append(status[check_time])
        return res 

# m = len(flowers), n = len(persons)
# Time O(mlogm + nlogn)
# Space O(m + n)
                
      
      
# Method 2
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        status = [[float("inf"), 0]]
        for start, end in flowers:
            status.append([start, 1])
            status.append([end + 1, -1])
        status.sort()
        
        res = [0] * len(persons)
        persons = [(time, idx) for idx, time in enumerate(persons)]
        persons.sort()
        
        sidx = 0
        stime = status[sidx][0]
        count = 0
        
        for ptime, pidx in persons:
            while ptime >= stime:
                count += status[sidx][1]
                sidx += 1
                stime = status[sidx][0]
            res[pidx] = count
        return res 
    
# m = len(flowers), n = len(persons)
# Time O(mlogm + nlogn)
# Space O(m + n)
                
            
            
            
        
