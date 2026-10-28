class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # convert nums to a set 
        num_set = set(nums)

        max_sequence = 0

        for num in num_set:
            # case: not left value 
            if (num - 1) in num_set:
                continue
            
            # case: minimum number, build sequence 
            sequence = 1
            value = num

            while (value + 1) in num_set:
                sequence += 1
                value = value + 1
            
            max_sequence = max(sequence, max_sequence)


        return max_sequence
            

        