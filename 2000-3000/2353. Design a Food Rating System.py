class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.lookup = dict()
        self.best = collections.defaultdict(list)
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.lookup[food] = [cuisine, rating]
            self.best[cuisine].append([-rating, food])
        for cuisine in self.best:
            heapq.heapify(self.best[cuisine])

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, _ = self.lookup[food]
        self.lookup[food][1] = newRating
        heapq.heappush(self.best[cuisine], [-newRating, food])

    def highestRated(self, cuisine: str) -> str:
        heap = self.best[cuisine]
        while heap and -heap[0][0] != self.lookup[heap[0][1]][1]:
            heapq.heappop(heap)
        return heap[0][1]
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
