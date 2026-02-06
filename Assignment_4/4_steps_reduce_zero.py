class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num > 0:
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
            steps += 1
        return steps

# Example run
if __name__ == "__main__":
    sol = Solution()
    print(sol.numberOfSteps(14))  # Expected: 6
