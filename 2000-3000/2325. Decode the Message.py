class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        d = {' ': ' '}
        
        idx = 0
        for char in key:
            if char not in d:
                d[char] = chr(97 + idx)
                idx += 1

        res = [d[char] for char in message]
        return ''.join(res)
        
