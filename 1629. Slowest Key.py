class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        longest = releaseTimes[0]
        key = keysPressed[0]
        for i in range(1, len(releaseTimes)):
            time = releaseTimes[i] - releaseTimes[i-1]
            if time == longest:
                key = max(key, keysPressed[i])
            elif time > longest:
                key = keysPressed[i]
                longest = time
        return key
