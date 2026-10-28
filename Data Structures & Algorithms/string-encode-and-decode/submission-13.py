class Solution:

    def encode(self, strs: List[str]) -> str:
        # format: [length][*][string]
        encoded = ""

        for word in strs:
            encoded += (str(len(word)) + '*' + word)
        
        return encoded


    def decode(self, s: str) -> List[str]:
        decoded = []

        i = 0 
        while i < len(s): 
            # find the number + delimiter 
            j = i
            while s[j] != '*':
                j += 1
            
            # calculate length 
            length = int(s[i:j])

            # grab string
            decoded.append(s[j + 1 : j + length + 1])

            i = j + length + 1
        

        return decoded
