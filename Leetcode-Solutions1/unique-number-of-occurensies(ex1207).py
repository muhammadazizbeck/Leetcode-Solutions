class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        txt = []
        counter = Counter(arr)
        for number,times in counter.items():
            txt.append(counter[number])
        return len(txt) == len(set(txt))