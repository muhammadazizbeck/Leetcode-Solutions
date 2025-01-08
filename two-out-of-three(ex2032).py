class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        txt=[]
        numx = set(nums1)
        numy = set(nums2)
        numz = set(nums3)
        final_list = list(numx)+list(numy)+list(numz)
        for let in final_list:
            if final_list.count(let)>=2:
                txt.append(let)
        return list(set(txt))