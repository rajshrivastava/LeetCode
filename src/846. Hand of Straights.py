class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand)%W != 0:
            return False
        
        def getFirst(data):
            return next(iter(data))
        
        hand.sort()
        counts = collections.OrderedDict()
        for h in hand:
            if h in counts:
                counts[h] += 1
            else:
                counts[h] = 1
        
        for _ in range(len(hand)//W):
            val = getFirst(counts)
            for __ in range(W):
                if val in counts:
                    counts[val] -= 1
                    if counts[val] == 0:
                        del counts[val]
                else:
                    return False
                
                val += 1
        return True
