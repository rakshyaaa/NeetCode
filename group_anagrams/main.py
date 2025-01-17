from group_anagrams import Solution


if __name__ == "__main__":
    strs = ["act","pots","tops","cat","stop","hat"]
    solution = Solution()
    result = solution.groupAnagrams(strs)
    print(result)