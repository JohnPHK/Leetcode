from typing import List

def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
    stack = []
    ans = []
    nums_map = {}
    
    for i in range(len(nums2)):
        if len(stack) > 0:
            p = stack[-1]
            while p < nums2[i] and len(stack) > 0:
                nums_map[p] = nums2[i]
                stack.pop()
                if len(stack) > 0:
                    p = stack[-1]

                
        stack.append(nums2[i])
    while len(stack) > 0:
        p = stack.pop()
        nums_map[p] = -1
    
    for i in range(len(nums1)):
        if nums1[i] in nums_map:
            ans.append(nums_map[nums1[i]])
    
    return ans

if __name__ == "__main__":
    print(nextGreaterElement([4,1,2], [1,3,4,2]))
