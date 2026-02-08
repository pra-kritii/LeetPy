class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        if n<=1:
            return n
        
        start =0
        for i in range(1,n):
            if nums[i]!=nums[start]:
                start+=1
                nums[start]=nums[i]
        return start+1