def canJump(self, nums: List[int]) -> bool:
        points = 0

        for num in nums:
            if points < 0:
                return False
            
            points = max(points,num)-1
        
        return True
