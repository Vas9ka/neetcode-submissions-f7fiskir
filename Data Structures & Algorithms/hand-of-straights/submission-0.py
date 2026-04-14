from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        hand.sort()
        counts = Counter(hand)

        for val in hand:
            if counts[val]:
                for i in range(val, val + groupSize):
                    if not counts[i]:
                        return False
                    counts[i] -= 1
        
        return True

            
