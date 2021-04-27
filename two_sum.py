# https://leetcode.com/problems/two-sum/

# how to use hash-map here? 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:  
        for pos_num_1 in range(len(nums)):
            for pos_num_2 in range(len(nums)):
                if pos_num_1 == pos_num_2:
                    continue
                if (nums[pos_num_1]+nums[pos_num_2]) == target:
                    return [pos_num_1,pos_num_2]
            
