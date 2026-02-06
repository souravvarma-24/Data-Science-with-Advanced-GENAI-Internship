from typing import List

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        teams = 0

        for j in range(n):
            left_small = left_big = 0
            right_small = right_big = 0

            for i in range(j):
                if rating[i] < rating[j]:
                    left_small += 1
                else:
                    left_big += 1

            for k in range(j+1, n):
                if rating[k] < rating[j]:
                    right_small += 1
                else:
                    right_big += 1

            teams += left_small * right_big + left_big * right_small

        return teams

# Example run
if __name__ == "__main__":
    sol = Solution()
    print(sol.numTeams([2,5,3,4,1]))
