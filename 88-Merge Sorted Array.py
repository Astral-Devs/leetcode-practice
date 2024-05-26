def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = len(nums1) - 1
        right = len(nums2)-1
        left = len(nums1)-len(nums2)-1

        while right >= 0:
            if left >= 0:
                if nums2[right] > nums1[left]:
                    nums1[i] = nums2[right]
                    right -= 1
                else:
                    nums1[i] = nums1[left]
                    left -= 1
            else:
                nums1[i] = nums2[right]
                right -= 1

            i -= 1
