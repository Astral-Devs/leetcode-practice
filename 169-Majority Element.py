def majorityElement(self, nums: List[int]) -> int:
        element_counter = {}

        for num in nums:
            if num in element_counter:
                element_counter[num] += 1
            else:
                element_counter[num] = 1

        for k,v in element_counter.items():
            if v > (len(nums)//2):
                return k
