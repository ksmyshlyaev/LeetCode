# https://leetcode.com/problems/running-sum-of-1d-array/
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        else:
            result_list = []
            for i in range(len(nums)):
                if i == 0:
                    result_list.append(nums[0])
                else:
                    result_list.append(sum(nums[0:i + 1]))
            return result_list

    # More optimal solution from community
    # def runningSumTwo(self, nums: List[int]) -> List[int]:
    #     for i in range(1, len(nums)):
    #         nums[i] = nums[i - 1] + nums[i]
    #     return nums


if __name__ == '__main__':
    print(Solution().runningSum([1, 2, 3, 4]))
    print(Solution().runningSum([1]))
    # print(Solution().runningSumTwo([1]))
