class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)
        counter = 0
        for word in words:
            if set(word).issubset(allowed_set):
                counter += 1
        return counter