class Solution:
    def countSubarrays(self, nums, k):
        #using sliding window
        max_value = max(nums)
        res = start = max_count = 0
        for i in range(len(nums)):
            if nums[i] == max_value:
                max_count += 1
            while max_count == k:
                if nums[start] == max_value:
                    max_count -= 1
                start += 1
            res += start
        return res