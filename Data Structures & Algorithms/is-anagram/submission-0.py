class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram_s = {} # character : instances
        anagram_t = {} 

        # exit case: not same length 
        if (len(s) != len(t)):
            return False
        
        for i, char_s in enumerate(s):
            # grab character from t
            char_t = t[i]

            # check if both characters are in dictionaries 
            if char_s in anagram_s:
                anagram_s[char_s] += 1
            
            else:
                anagram_s[char_s] = 1
            
            if char_t in anagram_t:
                anagram_t[char_t] += 1
            
            else:
                anagram_t[char_t] = 1
        
        # check the dictionaries if equal 
        return anagram_s == anagram_t


