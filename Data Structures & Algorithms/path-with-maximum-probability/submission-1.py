from collections import defaultdict
import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        probs = [0] * n
        probs[start_node] = 1
        idx = 0
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append((v, succProb[idx]))
            graph[v].append((u, succProb[idx]))
            idx += 1
        

        max_heap = [(1, start_node)]

        
        while max_heap:
            prob, node = heapq.heappop_max(max_heap)
            if node == end_node:
                return prob
            if prob < probs[node]:
                continue

            for nei, nei_prob in graph[node]:
                curr_prob = nei_prob * prob
                if curr_prob > probs[nei]:
                    probs[nei] = curr_prob
                    heapq.heappush_max(max_heap, (curr_prob, nei))
        
        return 0


