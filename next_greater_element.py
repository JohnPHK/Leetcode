class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        to_return = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    k = j + 1
                    while k < len(nums2):
                        if nums2[j] < nums2[k]:
                            to_return.append(nums2[k])
                            break
                        k += 1
                    if k == len(nums2):
                        to_return.append(-1)

        return to_return
