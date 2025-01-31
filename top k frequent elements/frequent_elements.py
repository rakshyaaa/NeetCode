from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #hashmap to count the occurences of each element in the array

        freq = [[] for i in range(len(nums) +1)]

        for n in nums:
            count[n] = 1 + count.get(n,0)  #adding count of each element in the hashmap
            print(count)

        for n,c in count.items():
            freq[c].append(n)
            print(freq)

        res = []

        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)

                if len(res) == k:
                    return res