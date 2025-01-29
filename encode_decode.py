from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""  
        for i in strs:
            res +=  str(len(i)) + "#" + i
        return res 

    def decode(self, s: str) -> List[str]:
        print(s)
        res, i  =  [], 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            print(i,j)
            length = int(s[i:j])
            print(length)
            i = j + 1
            res.append(s[i:i+length])
            i += length
        return res
            
if __name__ == "__main__":
    solution = Solution()
    encoded = solution.encode( ["rakshya","pandey"])
    print(encoded)
    decoded = solution.decode(encoded)
    print(decoded)
