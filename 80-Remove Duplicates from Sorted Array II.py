def removeDuplicates(self, nums: List[int]) -> int:
        fast,slow,duplicates_left = 1,0,1
        
        while fast < len(nums):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
                duplicates_left = 1
            else:
                if duplicates_left != 0:
                    slow += 1
                    nums[slow] = nums[fast]
                    duplicates_left -= 1 

            fast += 1
        
        for i in range(len(nums)-slow-1):
            nums.pop()
