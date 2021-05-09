# https://leetcode.com/problems/two-sum/

var twoSum = function(nums, target) {
    let map = {};
    let required = 0;
    for (let i = 0; i < nums.length - 1; i++) {
        required = target-nums[i];
        map[required] = i;
        if (nums[i+1] in map) {
            return [map[nums[i+1]], i+1];
        }
    } 
};
