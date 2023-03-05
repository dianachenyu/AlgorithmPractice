class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        nums = collections.defaultdict(list)
        for idx, num in enumerate(arr):
            nums[num].append(idx)
        visited = set()
        curs = set([0])
        step = 0

        while True:
            nxts = set()
            for cur in curs:
                if cur == n - 1:
                    return step

                visited.add(cur)
                candidates = [cur - 1, cur + 1] + nums[arr[cur]]
                nums[arr[cur]] = []
                for nxt in candidates:
                    if 0 <= nxt < n and nxt not in visited and nxt not in nxts:
                        nxts.add(nxt)
            step += 1
            curs = nxts
        return -1 

      
# Time O(N), Space O(N)
# BFS
# Trick: need to set nums[arr[cur]] = []; otherwise will copy list nums[arr[cur]] up to N times, get a total time complexity O(N^2)
