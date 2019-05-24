class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        index1 = 0
        index2 = 0
        total_size = len(nums1) + len(nums2)
        median = total_size // 2
        
        # check both arrays are non-empty
        if len(nums1) != 0 and len(nums2) != 0:
            
            # iterate until we have reached half the numbers
            # if array 2 has been emptied we are also done
            while (index1 < median + 1 and index2 < len(nums2)):
                
                # sort each element of array 2 into array 1
                if nums1[index1] > nums2[index2]:
                    nums1.insert(index1, nums2[index2])
                    nums2.pop(0)
                    
                # if we reach the end of array 1, simply append array 2 to the end of it and exit loop
                if index1 == len(nums1) - 1:
                    nums1.extend(nums2)
                    break
                index1 += 1
                
        # if array 1 was originally empty set it as array 2
        if len(nums1) == 0:
            nums1 = nums2
            
        # even
        if total_size % 2 == 0:
            return (nums1[median - 1] + nums1[median]) / 2
        
        # odd
        else:
            return nums1[median]
