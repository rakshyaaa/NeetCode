from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1

        for i in range(len(nums)):
            res[i] = prefix 
            
            prefix *= nums[i]
            print(nums[i],prefix,res[i])

        print(res)
        postfix = 1

        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
            print(nums[i],postfix,res[i])

        return res
            

if __name__ == "__main__":
    solution = Solution()
    res = solution.productExceptSelf(nums = [1,2,4,6])
    print(res)