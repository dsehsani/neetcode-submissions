class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # target : index
        target_hash = {}

        i = 0
        while (i < len(nums)):
            # find remainder
            remainder = target - nums[i]

            # check if in hash 
            if nums[i] in target_hash:
                return [target_hash[nums[i]], i]
                            
            target_hash[remainder] = i
            i += 1

        print(target_hash)
        
        return []
        