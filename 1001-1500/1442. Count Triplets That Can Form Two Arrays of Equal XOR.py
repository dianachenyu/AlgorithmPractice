class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        arr = [0] + arr
        n = len(arr)
        res = 0
        for i in range(1, n):
            arr[i] ^= arr[i - 1]
        for i in range(n):
            for k in range(i + 2, n):
                if arr[i] == arr[k]:    
                    res += k - i - 1
        return res

# Time O(N^2)
# Space O(N)

# TODO: understand O(N) time solution 
# https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/solutions/623747/java-c-python-one-pass-o-n-4-to-o-n
