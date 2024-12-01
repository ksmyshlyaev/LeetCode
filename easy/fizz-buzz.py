# https://leetcode.com/problems/fizz-buzz/
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        a = [str(i) for i in range(1, n + 1)]
        for i in range(len(a)):
            if int(a[i]) % 3 == 0:
                a[i] = "Fizz"
            if (i + 1) % 5 == 0:
                try:
                    int(a[i])
                    a[i] = "Buzz"
                except ValueError:
                    a[i] = a[i] + "Buzz"
        return a


if __name__ == '__main__':
    print(Solution().fizzBuzz(15))
