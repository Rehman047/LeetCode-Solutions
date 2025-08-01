class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        if goal > sum(nums):
            return 0
        l=0
        n=len(nums)
        ans=0
        fs=-1
        freq=0
        for i in range(n):
            if fs==-1 and nums[i]==1:
                fs=i
            if nums[i]==1:
                freq+=1
            while freq>goal:
                if nums[l]==1:
                    fs=-1
                    freq-=1
                l+=1
            if fs==-1:
                for j in range(l,i+1):
                    if nums[j]==1:
                        fs=j
                        break
            
            if freq==goal:
                if fs==-1:
                    ans+=i-l+1
                else: ans+=fs-l+1
        return ans

        #
