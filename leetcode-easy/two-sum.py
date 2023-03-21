class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #  n^2 approach

        # listLen = len(nums)
        # ans = []
        # for i in range(listLen):
        #     for j in range (i+1, listLen):
        #         if (nums[i] + nums[j] == target):
        #             ans.append(i)
        #             ans.append(j)
        # # print(ans)
        # return ans

        # O(n) time - extra space
        
        hashMap = {}
        for i in range (len(nums)):
            if nums[i] in hashMap:
                return [hashMap[nums[i]], i]
            else :
                hashMap[target - nums[i]] = i 
