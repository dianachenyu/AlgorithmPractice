# solution 1:
  def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        for num in nums:
            if not ranges or num != ranges[-1][1] + 1:
                ranges.append([num, num])
            else:
                ranges[-1][1] += 1
        res = []
        for start, end in ranges:
            if start == end:
                res.append(str(start))
            else:
                res.append(str(start) + "->" + str(end))
        return res

      
# solution 2
    def summaryRanges(self, nums: List[int]) -> List[str]:
        left = 0
        n = len(nums)
        res = []
        for right in range(n):
            if right == n - 1 or nums[right] + 1 != nums[right + 1]:
                ans = str(nums[left])
                if left != right:
                    ans += "->" + str(nums[right])
                res.append(ans)
                left = right + 1
        return res
        
