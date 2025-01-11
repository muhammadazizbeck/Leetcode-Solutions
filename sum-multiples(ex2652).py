class Solution:
    def sumOfMultiples(self, n: int) -> int:
        counter = 0
        txt = list(range(1,n+1))
        for tx in txt:
            if tx%3==0 or tx%5==0 or tx%7==0:
                counter += tx
        return counter