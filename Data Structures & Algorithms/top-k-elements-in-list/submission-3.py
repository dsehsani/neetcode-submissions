class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        process: using tricky bucket sort
        '''

        frequency_hash = {} # number : frequency 
        frequency_array = [[] for i in range(len(nums) + 1)]

        # populate frequency hash 
        for num in nums:
            frequency_hash[num] = 1 + frequency_hash.get(num, 0)
        
        # iterate through dictionary to populate frequency_array 
        for num, freq in frequency_hash.items():
            frequency_array[freq].append(num)
        
        # loop in reverse of array
        result = []
        for i in range(len(frequency_array) - 1, -1, -1):
            for n in frequency_array[i]:
                if (len(result) == k):
                    return result
                
                result.append(n)

        return result





        