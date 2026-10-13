class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_finder = defaultdict(list) # defaults to []

        for s in strs:
            # count of lowercase appearances [a-z] 
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1 #normalize to count
            
            # append to dictionary 
            anagram_finder[tuple(count)].append(s)
        
        # returning the values 
        return list(anagram_finder.values())

        
        