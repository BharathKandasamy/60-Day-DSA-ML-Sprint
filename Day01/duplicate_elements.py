class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums1 = set()
        for i in nums:
            if i in nums1:
                return True
            else:
                nums1.add(i)
        return False
