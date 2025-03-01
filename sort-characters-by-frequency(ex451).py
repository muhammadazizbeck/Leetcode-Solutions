class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        sorted_chars = sorted(s, key=lambda x: (-counter[x], x))
        return "".join(sorted_chars)