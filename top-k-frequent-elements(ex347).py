class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums) 
        sorted_list = sorted(counter.keys(), key=lambda x: counter[x], reverse=True)
        return sorted_list[:k]