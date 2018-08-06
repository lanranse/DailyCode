class Solution:
    """
    @param nums: A list of integers
    @return: An integer denotes the middle number of the array
    """

    def median(self, nums):
        l = len(nums)
        mid = (l - 1) // 2
        result = self.sort(nums, 0, l - 1, mid)
        print('median:{}'.format(result))
        return result

    def sort(self, nums, left, right, mid):
        po = self.position(nums, left, right)
        print(nums)
        print(po, mid)
        if po == mid:
            print('result={}'.format(nums[po]))
            return nums[po]
        elif po > mid:
            self.sort(nums, left, po - 1, mid)
        else:
            self.sort(nums, po + 1, right, mid)

    def position(self, nums, left, right):
        temp = nums[left]
        while left < right:
            while left < right and nums[right] >= temp:
                right -= 1
            nums[left] = nums[right]
            while left < right and nums[left] <= temp:
                left += 1
            nums[right] = nums[left]
        nums[left] = temp
        return left


if __name__ == '__main__':
    nums=[4,5,1,2,3]
    mid=Solution().median(nums)
    print(mid)