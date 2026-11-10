class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        desired = {} # target - numbers[i] : index + 1 (1-indexed)


        for i, v in enumerate(numbers):
            # success: value is a desired target 
            if v in desired: 
                return [desired[v], i + 1]
            
            # logic: update dictionary 
            remainder = target - numbers[i]
            desired[remainder] = i + 1
        
        return []


        