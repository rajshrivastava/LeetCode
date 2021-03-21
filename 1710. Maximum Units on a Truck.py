class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: x[1], reverse = True)
        totalUnits = 0
        for n, units in boxTypes:
            if truckSize == 0:
                break
            boxes = min(truckSize, n)
            totalUnits += (boxes*units)
            truckSize -= boxes
            
        return totalUnits
