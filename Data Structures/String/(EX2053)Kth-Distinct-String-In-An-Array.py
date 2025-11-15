class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        result = []
        freq = Counter(arr)

        for num,count in freq.items():
            if count == 1:
                result.append(num)
            else:
                continue
            
        if len(result)>=k:
            return result[k-1]
        else:
            return ""