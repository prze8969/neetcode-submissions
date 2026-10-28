class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ot=[]
        nums.sort()
        for i in range(len(nums)):
            target = nums[i]
            left = i+1
            right = len(nums)-1
            if i >0:
                if nums[i]==nums[i-1]:
                    right-=1
                    left+=1
                    continue
            while(right>left):
                if (nums[left]+nums[right]==-target):
                    if [nums[left],target,nums[right]] not in ot:
                        ot.append([nums[left],target,nums[right]])
                    right-=1
                    left+=1
                elif nums[left]+nums[right]>-target:
                    right-=1
                elif nums[left]+nums[right]<-target:
                    left+=1
        return ot