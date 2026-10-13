class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a defaut dictionary 
        result = defaultdict(list)

        # iterate through the strings
        for string in strs:
            # create a frequency map for characters [a-z]
            frequency_map = [0] * 26

            # populate frequency_map
            for c in string:
                frequency_map[ord(c) - ord('a')] += 1
            
            # check if frequency_map exist 
            result[tuple(frequency_map)].append(string)


        # return result's values
        return list(result.values())