class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # tuple : list
        anagrams = collections.defaultdict(list)
        result = []

        for string in strs: 
            # convert characters to a sorted tuple
            characters = tuple(sorted(string))

            # case: anagram found 
            anagrams[characters].append(string)
        
        # update result 
        for key in anagrams:
            result.append(anagrams[key])
        
        
        return result


        