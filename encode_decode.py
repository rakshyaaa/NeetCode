from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""  
        for i in strs:
            res += str(len(i)) + '#' + i
        return res 

    def decode(self, s: str) -> List[str]:
        res, i = [],0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            res.append(s[j+1 : j+1+length])

            i = j + 1 + length

        return res        
            
if __name__ == "__main__":
    solution = Solution()
    encoded = solution.encode( ["rakshya","pandey"])
    print(encoded)
    decoded = solution.decode(encoded)
    print(decoded)
