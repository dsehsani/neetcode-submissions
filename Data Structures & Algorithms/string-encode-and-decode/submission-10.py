DELIMITER = '#'

class Solution:

    def encode(self, strs: List[str]) -> str:
        '''
        Format: [INT]#[STRING]
        '''
        encoded = ""
        
        for string in strs:
            encoded += str(len(string))
            encoded += DELIMITER
            encoded += string
        
        return encoded



    def decode(self, s: str) -> List[str]:
        decoded, i = [], 0

        while i < len(s):
            j = i

            # find delimiter
            while s[j] != DELIMITER:
                j += 1
            
            # find length of string 
            length = int(s[i:j])

            # grab the string 
            decoded.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        
        return decoded







                

