class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sum_odd = 0
        sum_even = 0

        for i in range(1,2*n+1):
            if i % 2 == 0:
                sum_even += i
            else:
                sum_odd += i

        # bottom = sum_odd

        # while sum_odd > 0:
        #     if sum_even % bottom == 0 and sum_odd % bottom == 0:
        #         gcd = bottom
        #         break
        #     else:
        #         bottom -= 1

        # return gcd

        return gcd(sum_even,sum_odd)