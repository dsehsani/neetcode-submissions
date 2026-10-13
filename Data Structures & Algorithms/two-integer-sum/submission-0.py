class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_difference = {} # target - nums[i] : i

        for i, v in enumerate(nums):
            # check if value is a target difference
            if v in target_difference:
                return [target_difference[v], i]
            
            difference = target - v
            target_difference[difference] = i
        
        return False

        