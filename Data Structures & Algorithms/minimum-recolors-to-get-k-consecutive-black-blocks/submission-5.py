class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        curr = 0
        for i in range(k):
            if blocks[i] == 'W':
                curr += 1
        if curr == 0:
            return curr
        ans = curr
        for i in range(k, len(blocks)):
            if blocks[i] == 'W':
                curr += 1

            if blocks[i - k] == 'W':
                curr -= 1
            ans = min(curr, ans)

        return ans
            