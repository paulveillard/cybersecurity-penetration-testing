class Solution(object):
    # def findShortestSubArray(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     res = len(nums)
    #     counter = collections.Counter()
    #     for num in nums:
    #         counter[num] += 1
    #     degree = max(counter.values())
    #     for key, kdegree in counter.most_common():
    #         if degree != kdegree:
    #             break
    #         res = min(res, self.smallestSubArray(nums, key, degree))
    #     return res

    # def smallestSubArray(self, nums, key, degree):
    #     start = nums.index(key)
    #     pos = start + 1
    #     degree -= 1
    #     while pos < len(nums) and degree != 0:
    #         if nums[pos] == key:
    #             degree -= 1
    #         pos += 1
    #     return pos - start

    def findShortestSubArray(self, nums):
        left, right, count = {}, {}, {}
        for i, x in enumerate(nums):
            if x not in left: left[x] = i
            right[x] = i
            count[x] = count.get(x, 0) + 1

        ans = len(nums)
        degree = max(count.values())
        for x in count:
            if count[x] == degree:
                ans = min(ans, right[x] - left[x] + 1)

        return ans
