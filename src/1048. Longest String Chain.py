class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def isPredecessor(str1, str2):
            l1 = len(str1)
            i = 0
            while i < l1 and str1[i] == str2[i]:
                i += 1
            
            while i < l1 and str1[i] == str2[i+1]:
                i += 1
                
            return i == l1
                
        @lru_cache(maxsize=None)
        def findMaxChain(word):
            chain_len = 0
            for next_word in wordLen_to_words[len(word)+1]:
                if isPredecessor(word, next_word):
                    chain_len = max(chain_len, findMaxChain(next_word))
               
            return 1 + chain_len                
                
        wordLen_to_words = collections.defaultdict(list)
        for word in words:
            wordLen_to_words[len(word)].append(word)
        
        word_to_chainLength = dict()
        
        max_chainLength = 0
        for word in words:
            max_chainLength = max(max_chainLength, findMaxChain(word))
                
        return max_chainLength
        
        
