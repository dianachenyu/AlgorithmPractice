class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split('.')
        version2 = version2.split('.')
        for i in range(max(len(version1), len(version2))):
            if i < len(version1):
                v1 = int(version1[i])
            else:
                v1 = 0
            if i < len(version2):
                v2 = int(version2[i])
            else:
                v2 = 0

            if v1 < v2:
                return -1
            if v1 > v2:
                return 1
        return 0
 
        
