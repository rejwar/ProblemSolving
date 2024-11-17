class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h={}
        for i,num in enumerate(nums):
            h[num]=i
        for i in range(len(nums)):
            req=target-nums[i]
            if req in h and h[req]!=i:
                return [i,h[req]]

            
        