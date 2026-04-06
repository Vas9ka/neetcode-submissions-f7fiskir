class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            sum_l_r = numbers[left] + numbers[right]
            if sum_l_r < target:
                left += 1
            elif sum_l_r > target:
                right -= 1
            else:
                return [left + 1, right + 1]
        return []