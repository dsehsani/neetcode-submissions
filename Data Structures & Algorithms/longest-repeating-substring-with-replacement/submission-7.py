class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # case: edge
        if len(s) == 1: 
            return 1
        
        if k == len(s): 
            return len(s)
        

        # setup: sliding window 
        l, r = 0, 1
        frequency = {s[l] : 1} # char : frequency
        longest = 1

        while (r < len(s)):            
            # incrementing instance
            frequency[s[r]] = frequency.get(s[r], 0) + 1

            # update window size 
            window = len(s[l : r + 1])

            # condition: move left 
            while (window - max(frequency.values()) > k):
                # decrement from dictionary
                frequency[s[l]] -= 1
                l += 1
                window = len(s[l : r + 1])
            
            longest = max(longest, window)
            r += 1
        
        
        return longest     
        