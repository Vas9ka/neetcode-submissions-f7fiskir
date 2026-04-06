class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        best_l = 0
        best_r = k - 1

        for i in range(k, len(arr)):
            if abs(arr[i] - x) < abs(arr[best_l] - x):
                best_l = i - k + 1
                best_r = i
        return arr[best_l:best_r + 1]