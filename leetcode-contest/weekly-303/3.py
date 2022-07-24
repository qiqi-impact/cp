from sortedcontainers import SortedList

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.fcr = {}
        self.cr = {}
        for i in range(len(foods)):
            self.fcr[foods[i]] = [cuisines[i], ratings[i]]
            if cuisines[i] not in self.cr:
                self.cr[cuisines[i]] = SortedList(key=lambda x:(x[0], tuple([-ord(c) for c in x[1]])))
            self.cr[cuisines[i]].add((ratings[i], foods[i]))

    def changeRating(self, food: str, newRating: int) -> None:
        oldr = self.fcr[food][1]
        self.fcr[food][1] = newRating
        self.cr[self.fcr[food][0]].discard((oldr, food))
        self.cr[self.fcr[food][0]].add((newRating, food))
        
    def highestRated(self, cuisine: str) -> str:
        return self.cr[cuisine][-1][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)