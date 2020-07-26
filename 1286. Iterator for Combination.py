class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        def getCombinations(cum_string, rem_chars, level):
            if level == combinationLength:
                return [cum_string]
            lis = []
            for i, ch in enumerate(rem_chars):
                lis.extend(getCombinations(cum_string+ch, rem_chars[i+1:], level+1))
            return lis
        
        self.characters = sorted(characters)
        self.counter = 0
        self.lis = []
        for i, ch in enumerate(self.characters):
            self.lis.extend(getCombinations(cum_string = ch, rem_chars = self.characters[i+1:], level=1))
        self.total = len(self.lis)
        
        print(self.lis)
    def next(self) -> str:
        self.counter += 1
        return self.lis[self.counter-1]
            
    def hasNext(self) -> bool:
        return self.counter < self.total


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
