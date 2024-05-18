# Method 1
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(i, j, can_delete):
            if i >= j:
                return True
            if s[i] == s[j]:
                return check(i + 1, j - 1, can_delete)
            elif can_delete:
                return check(i + 1, j, False) or check(i, j - 1, False)
            else:
                return False
        return check(0, len(s) - 1, True)

      
# Method 2      
class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while s[i] == s[j]:
            if i >= j:
                return True
            i += 1
            j -= 1
        return s[i + 1: j +1] == s[i + 1: j +1][::-1] or s[i: j] == s[i: j][::-1]


# Method 3:
class Solution:
    def validPalindrome(self, s: str) -> bool:

        def helper(l, r):
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True
    
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return helper(l + 1, r) or helper(l, r - 1)
        return True
