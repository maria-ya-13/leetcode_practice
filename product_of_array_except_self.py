# https://leetcode.com/problems/product-of-array-except-self

# time limit exceeded {-1: 24975, 1: 24994, -2: 12, 2: 18}

from collections import Counter
class Solution:

    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def reduce(collection):
            red = 1
            if 0 in collection:
                return 0
            for x in set(collection):
                red *= x
            
            duplicate_counter = dict(Counter(collection))
            for i in duplicate_counter:
                if duplicate_counter[i] > 1:
                    if i == -1 and duplicate_counter[i]%2 ==0:
                        red*=i
                        continue
                    red*=i ** (duplicate_counter[i]-1)
                
            return red
        
        
        new_num = []        
        for i in range(len(nums)):
            nums_copy = nums.copy()
            nums_copy.pop(i)
            res = reduce(nums_copy)
            new_num.append(res)
                           
        return new_num
