class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        consumed = 0
        newBottles = numBottles
        while numBottles >= numExchange:
            consumed += newBottles
            newBottles = numBottles//numExchange
            carryForward = numBottles%numExchange
            numBottles = newBottles + carryForward
        return consumed + newBottles
