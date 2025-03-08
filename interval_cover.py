from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Step 1: Sort intervals by start time
        intervals.sort(key=lambda i: (i[0], -i[1]))

        result = []
        curr_end = intervals[0][0]
        target = max(interval[1] for interval in intervals)
        i, n = 0, len(intervals)

        while curr_end < target:
            max_end = curr_end
            best_interval = None

            # Step 2: Find the interval that extends coverage the farthest
            while i < n and intervals[i][0] <= curr_end:
                if intervals[i][1] > max_end:
                    max_end = intervals[i][1]
                    best_interval = intervals[i]
                i += 1

            if not best_interval:  # If no interval extends coverage, return what we have
                break

            result.append(best_interval)
            curr_end = max_end

            if curr_end >= target:
                break

        return result

# Example Usage
if __name__ == "__main__":
    s = Solution()
    intervals = [[0,60], [0,35], [40,120], [55,140], [60,120], [100,160], [130,160]]
    output = s.merge(intervals)
    print(output)
