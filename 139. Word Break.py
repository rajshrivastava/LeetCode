class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def isPresent(s):
            if s in self.checked:
                return self.checked[s]
            
            for i in range(1, len(s)+1):
                if s[:i] in self.checked and self.checked[s[:i]] == True:
                    
                    self.checked[s[i:]] = isPresent(s[i:])
                    if self.checked[s[i:]] == True:
                        return True
            self.checked[s] = False
            return False
                    
        self.checked = {}
        for word in wordDict:
            self.checked[word] =True
        return isPresent(s)
