# Method 1: Trie
class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        trie_func = lambda: collections.defaultdict(trie_func)
        self.trie = trie_func()
        for word in dictionary:
            cur = self.trie
            for char in word:
                cur = cur[char]
            cur = cur['#']
       
        self.en_lookup = dict(zip(keys, values))
        self.de_lookup = collections.defaultdict(list)
        for value, key in zip(values, keys):
            self.de_lookup[value].append(key)
      
    def encrypt(self, word1: str) -> str:
        res = []
        for char in word1:
            res.append(self.en_lookup[char])
        return ''.join(res)

    def decrypt(self, word2: str) -> int:
        def dfs(idx, cur):
            if idx == len(word2):
                return int('#' in cur)
            
            res = 0
            candidates = self.de_lookup[word2[idx: idx + 2]]
            for j in range(len(candidates)):
                if candidates[j] in cur:
                    nxt = cur[candidates[j]]
                    res += dfs(idx + 2, nxt)
            return res
            
        return dfs(0, self.trie)     

     
    
# Method 2
class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.en_lookup = dict(zip(keys, values))
        self.de_lookup = collections.Counter()
        for word in dictionary:
            self.de_lookup[self.encrypt(word)] += 1
        
      
    def encrypt(self, word1: str) -> str:
        res = []
        for char in word1:
            res.append(self.en_lookup[char])
        return ''.join(res)

    def decrypt(self, word2: str) -> int:
        return self.de_lookup[word2]
            

# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)
