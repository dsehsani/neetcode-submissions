class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # base conditions 
        if len(s) == 0:
            return 0 
        
        if len(s) == 1:
            return 1
        
        # define sliding window
        longest = 1
        left, right = 0, 1
        duplicates = {s[left]:True}     # character : bool

        while (right < len(s)):
            # case: duplicate encountered 
            if s[right] in duplicates: 
                
                # logic: find duplicate, remove from dictionary
                while (s[left] != s[right]):
                    del duplicates[s[left]]
                    left += 1
                
                # duplicate found [no need to remove from dictionary]
                left += 1
            
            # case: no duplicate 
            duplicates[s[right]] = True

            length = len(s[left:right + 1])
            longest = max(length, longest)

            right += 1

        return longest





        
