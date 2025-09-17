import heapq
from typing import List

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        # Maps food -> (cuisine, rating)
        self.food_info = {}

        # Maps cuisine -> max-heap of (-rating, food)
        self.cuisine_map = {}

        for f, c, r in zip(foods, cuisines, ratings):
            self.food_info[f] = [c, r]
            if c not in self.cuisine_map:
                self.cuisine_map[c] = []
            heapq.heappush(self.cuisine_map[c], (-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, _ = self.food_info[food]
        self.food_info[food][1] = newRating
        heapq.heappush(self.cuisine_map[cuisine], (-newRating, food))
        # old rating remains in heap, but we'll clean it during query

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisine_map[cuisine]

        # Pop invalid entries (where rating doesn't match latest)
        while heap:
            rating, food = heap[0]
            if -rating == self.food_info[food][1]:
                return food
            heapq.heappop(heap)  # remove outdated entry
