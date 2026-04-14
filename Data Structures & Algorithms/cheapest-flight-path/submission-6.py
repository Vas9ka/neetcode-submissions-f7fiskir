import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        distances = [float('inf')] * n


        distances[src] = 0
        while k + 1:
            temp = distances[:]
            for u, v, w in flights:
                temp[v] = min(temp[v], distances[u] + w)
            k -= 1
            distances = temp 
        return distances[dst] if distances[dst] != float('inf') else -1