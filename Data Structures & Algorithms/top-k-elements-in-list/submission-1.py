class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_hash = defaultdict(int)
        result = []

        # populate hash 
        for num in nums:
            frequency_hash[num] += 1
        
        # reverse the dictionary
        reversed_frequency = dict(sorted(frequency_hash.items(), key=lambda item: item[1], reverse=True))

        # iterate through dictionary k times 
        for freq in reversed_frequency:
            if (k == 0):
                return result
            
            # append to result 
            result.append(freq)
            k -= 1
        

        return result


        


        