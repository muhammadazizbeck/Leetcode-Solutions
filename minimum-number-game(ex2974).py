class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        arr = []
        while nums:
            alice_choice = nums.pop(0)
            if nums:
                bob_choice = nums.pop(0)
                arr.append(bob_choice)
            else:
                break
            arr.append(alice_choice)
        return arr