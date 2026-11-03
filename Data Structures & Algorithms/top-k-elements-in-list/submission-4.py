import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # number : frequency
        frequency = {}

        # populate frequency 
        for value in nums: 
            if value in frequency: 
                frequency[value] += 1
            
            else: 
                frequency[value] = 1
        

        # apply heap + grab top k 
        return heapq.nlargest(k, frequency, key=frequency.get)
        


            



        