import collections
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie_func = lambda: collections.defaultdict(trie_func)
        trie = trie_func()

        for word in dictionary:
            t = trie
            for char in word:
                t = t[char]
            t['#'] = word

        def replace(word):
            t = trie
            for char in word:
                if char in t:
                    t = t[char]
                else:
                    break
                if '#' in t:
                    return t['#']
            return word 

        res = []
        sentence = sentence.split(' ')
        for word in sentence:
            res.append(replace(word))
        return ' '.join(res)

