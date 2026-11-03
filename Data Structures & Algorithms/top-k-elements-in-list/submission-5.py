class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        bucket sort implementation
        '''

        # number : frequency 
        count = {} 
        bucket = [[] for i in range(len(nums) + 1)]

        # populate frequency 
        for value in nums:
            # increment frequency
            count[value] = 1 + count.get(value, 0)


        # update bucket 
        for c, v in count.items():
            bucket[v].append(c)

        # reversely go through bucket 
        result = [] 

        print(k)

        for i in range(len(bucket) - 1, 0, -1):
            # add frequency
            for freq in bucket[i]:

                result.append(freq)

                if len(result) == k:
                    return result

        
        return []

        