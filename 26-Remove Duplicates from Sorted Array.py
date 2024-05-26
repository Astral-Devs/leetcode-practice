def removeDuplicates(self, nums: List[int]) -> int:
        fast = 1
        slow = 0

        while fast < len(nums):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]

            fast += 1
        
        for i in range(len(nums)-slow-1):
            nums.pop()

        return(len(nums))
