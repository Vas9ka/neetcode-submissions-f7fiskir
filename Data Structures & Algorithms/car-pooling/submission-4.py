import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])  # sort by start

        min_heap = []  # (end, passengers)
        current = 0

        for passengers, start, end in trips:
            # remove all finished trips
            while min_heap and min_heap[0][0] <= start:
                finished_end, finished_passengers = heapq.heappop(min_heap)
                current -= finished_passengers

            # add current trip
            current += passengers
            if current > capacity:
                return False

            heapq.heappush(min_heap, (end, passengers))

        return True