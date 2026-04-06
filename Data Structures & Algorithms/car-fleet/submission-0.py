class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        p_s = [[p, s] for p, s in zip(position, speed)]
        stack = []
        for pos, speed in sorted(p_s)[::-1]:
            stack.append((target - pos) / speed)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)