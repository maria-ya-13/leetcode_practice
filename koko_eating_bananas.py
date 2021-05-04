# https://leetcode.com/problems/koko-eating-bananas/

# binary search case

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        if len(piles) == 1:
            return math.ceil(piles[0] / h)
        
        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2
            if sum(int((pile - 1) / mid) + 1 for pile in piles) <= h:
                right = mid
            else:
                left = mid + 1
        return left
