class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        words = set(wordList) - set([beginWord])
        layer = set([beginWord])
        parent = collections.defaultdict(set)
        continue_loop = True
        
        while layer and continue_loop:
            nlayer = set()
            for word in layer:
                if word == endWord:
                    continue_loop = False
                    continue 
                
                for i in range(len(beginWord)):
                    for char in string.ascii_lowercase:
                        if char == word[i]:
                            continue
                        nword = word[: i] + char + word[i + 1: ] 
                        if nword in words:
                            nlayer.add(nword)
                            parent[nword].add(word)            
            words -= nlayer
            layer = nlayer
        
        res = []
        def dfs(node, path):
            if node == beginWord:
                res.append([node] + path[::-1])
                return 
            for lnode in parent[node]:
                path.append(node)
                dfs(lnode, path)
                path.pop()

        dfs(endWord, [])
        return res

      
# helpful article: https://leetcode.com/problems/word-ladder-ii/solutions/4200470/o-n-w-time-and-o-n-2-w-space-complexity-tle-and-mle-optimized
