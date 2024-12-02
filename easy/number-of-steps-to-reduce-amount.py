# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/description/
class Solution:
    def numberOfSteps(self, num: int) -> int:
        counter = 0
        while num != 0:
            if num % 2 != 0:
                num = num - 1
                counter += 1
            else:
                num = num / 2
                counter += 1
        return counter


if __name__ == '__main__':
    print(Solution().numberOfSteps(14))
    print(Solution().numberOfSteps(8))
    print(Solution().numberOfSteps(123))
