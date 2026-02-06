from typing import List

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count = 0
        for s, e in zip(startTime, endTime):
            if s <= queryTime <= e:
                count += 1
        return count

# Example run
if __name__ == "__main__":
    sol = Solution()
    print(sol.busyStudent([1,2,3], [3,2,7], 4))  # Expected: 1
