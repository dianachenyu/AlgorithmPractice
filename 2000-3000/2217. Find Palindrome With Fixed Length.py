class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        half_length = math.ceil(intLength / 2)
        max_num = (10 ** (half_length - 1)) * 9
        res = []
        for query in queries:
            query -= 1
            if query >= max_num:
                res.append(-1)
            elif intLength == 1:
                res.append(query + 1)
            else:
                num = 10 ** (half_length - 1) + query
                snum = str(num)
                num = int(snum + snum[: intLength - half_length][::-1])            
                res.append(num)
        return res 
