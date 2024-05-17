class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        s = s.lower()
        while i < j:
            if not(s[i] in string.ascii_lowercase or s[i] in string.digits):
                i += 1
                continue
            if not(s[j] in string.ascii_lowercase or s[j] in string.digits):
                j -= 1
                continue 
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
