class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointer technique
        i, j = 0, len(s) - 1

        while i < j: 
            # case: non-alphanumeric 
            if not (s[i].isalnum()):
                i += 1
                continue
            
            elif not (s[j].isalnum()):
                j -= 1
                continue
            
            # case: same character 
            if (s[i].lower() == s[j].lower()):
                i += 1
                j -= 1
                continue
            
            return False


        return True
            




        