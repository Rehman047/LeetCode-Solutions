class Solution(object):
    def func(self,nums,k):
        l=0
        r=0
        n=len(nums)
        ans=0
        m=defaultdict(int)
        while r<n:
            m[nums[r]]+=1

            while len(m)>k:
                m[nums[l]]-=1
                if(m[nums[l]]==0):
                    m.pop(nums[l])
                l+=1
            
            ans+=r-l+1
            r+=1
        return ans
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k==1:
                return self.func(nums,k)
        else:
                return self.func(nums,k)-self.func(nums,k-1)


        