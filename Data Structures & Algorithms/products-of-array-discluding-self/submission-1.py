class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # populate prefix 
        prefix = [1] * len(nums)

        
        i = 1 
        while i < len(prefix):
            prefix[i] = nums[i - 1] * prefix[i - 1]
            i += 1
    
        # populate postfix
        postfix = [1] * len(nums)

        i = len(postfix) - 2
        #print(i)

        while i >= 0:
            postfix[i] = nums[i + 1] * postfix[i + 1]
            i -= 1

        # combine the two arraries
        output = [1] * len(nums)
        for i in range(0, len(output)):
            output[i] = prefix[i] * postfix[i]

        return output
        