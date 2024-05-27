def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num_copy = nums.copy()

        for i,num in enumerate(num_copy):
            nums[(i+k)%len(nums)] = num
