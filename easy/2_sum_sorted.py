class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums = {}
        for i, number in enumerate(numbers):
            if target - number in nums:
                return [nums[target - number], i]
            nums[number] = i

    def twoSum2(self, numbers, target):
        '''
        :param numbers: List[int]
        :param target: int
        :return: List[num]
        '''
        k = 0
        for i in numbers:
            j = target -i
            k += 1
            tmp_numbers = numbers[k:]
            if j in tmp_numbers:
                return [k-1, tmp_numbers.index(j) + k]