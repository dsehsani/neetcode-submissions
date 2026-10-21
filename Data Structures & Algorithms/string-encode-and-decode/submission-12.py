class Solution:

    def encode(self, strs: List[str]) -> str:
        '''
        encoding: [Number][#][String]
        '''
        encoded = ""

        for string in strs:
            encoded += str(len(string)) + '#' + string

        return encoded




    def decode(self, s: str) -> List[str]:
        decoded = []

        i = 0
        while i < len(s):
            # find the total number
            
            j = i
            while s[j] != '#':
                j += 1
            
            # decoding length
            
            length = int(s[i:j])
            decoded.append(s[j+1:length + j + 1])
            i = length + j + 1



        
            
            


        return decoded
