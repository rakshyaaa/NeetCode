from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        print(numSet)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest



if __name__ == "__main__":
    solution = Solution()
    res = solution.longestConsecutive(nums = [0,3,2,5,4,6,1,1])
    print(res)