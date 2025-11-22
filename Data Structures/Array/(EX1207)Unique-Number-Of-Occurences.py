class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = Counter(arr)

        # result = []
        # for item,count in freq.items():
        #     result.append(count)
        
        # return len(result)==len(set(result))

        seen = set()
        for char,count in freq.items():
            if count in seen:
                return False
            else:
                seen.add(count)
            
        return True