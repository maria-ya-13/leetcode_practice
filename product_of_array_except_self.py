# https://leetcode.com/problems/product-of-array-except-self

from collections import Counter
class Solution:   
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def reduce(num_counter):
            red = 1
            if 0 in num_counter:
                if num_counter[0] > 0:
                    return 0
                num_counter.pop(0)        
            for i in num_counter:
                red*=i ** (num_counter[i])
            return red
        
        new_num = []  
        num_counter = dict(Counter(nums))
        for num in nums:
            cur_num_counter = num_counter.copy()
            cur_num_counter[num] -=1
            new_num.append(reduce(cur_num_counter))                 
        return new_num
