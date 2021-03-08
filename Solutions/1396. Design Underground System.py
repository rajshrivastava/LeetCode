class UndergroundSystem:

    def __init__(self):
        # stationPairs = {(s1, s2) : [toTaltime, trips]}
        # c_in = {id: (time, s)}
        self.stationPairs = dict()        
        self.c_in = dict()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.c_in[id] = (t, stationName)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        time_in, s1 = self.c_in[id]
        tripTime = t - time_in
        
        if (s1, stationName) not in self.stationPairs:
            self.stationPairs[(s1,stationName)] = [0,0]
        self.stationPairs[(s1,stationName)][0] += tripTime
        self.stationPairs[(s1,stationName)][1] += 1
        del self.c_in[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTime, trips =  self.stationPairs[(startStation, endStation)]
        return totalTime/trips

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
