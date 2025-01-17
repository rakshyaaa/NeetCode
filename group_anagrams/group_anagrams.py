from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)  #mapping character count to a list of anagrams

        for s in strs:
            count = [0] * 26   #initializing an array of alphabet order counters

            for c in s:
                count[ord(c) - ord('a')] +=1

                print(count)

            result[tuple(count)].append(s)
            print(result)

        return result.values()