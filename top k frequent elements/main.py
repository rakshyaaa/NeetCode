from frequent_elements import Solution


if __name__ == "__main__":
    nums = [1,2,2,3,3,3]
    k = 2
    solution = Solution()
    result = solution.topKFrequent(nums,k)
    print(result)