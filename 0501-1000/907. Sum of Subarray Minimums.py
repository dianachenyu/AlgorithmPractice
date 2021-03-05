# res[i] represents the sum of min(subarrays), for subarrays ending at index i
# stack keeps the indexs of strictly increasing num 
# for subarry starting with index stack[-1]+1 until index, its min is num 
# for subarrays starting with index <= stack[-1], sum of mins is res[stack[-1]] 
# Time O(N) Space O(N)

class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        n = len(arr)
        res = [0] * (n + 1)
        arr.append(0)
        stack = [-1]
        for idx, num in enumerate(arr[:-1]):
            while num <= arr[stack[-1]]:
                stack.pop()
            res[idx] = res[stack[-1]] + num * (idx - stack[-1])
            stack.append(idx)
        return sum(res)%(10 ** 9 + 7)
