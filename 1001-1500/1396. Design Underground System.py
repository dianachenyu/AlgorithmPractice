class UndergroundSystem:

    def __init__(self):
        self.customers = {} # {id: (in_station, in_time)}
        self.total_time = collections.defaultdict(lambda: [0, 0]) # {(in_station, out_station) : (total_time, count)}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customers[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        in_station, in_time = self.customers[id]
        self.total_time[(in_station, stationName)][0] += t - in_time
        self.total_time[(in_station, stationName)][1] += 1
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time, count = self.total_time[(startStation, endStation)]
        return total_time / count
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
