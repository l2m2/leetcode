import timeit

class Solution:
    def __temp(self, nums, target): 
        buff_dict = {}
        for i in nums:
            if i in buff_dict:
                buff_dict[i] = True
            else:
                buff_dict[target - i] = i
        ret = []
        for k, v in buff_dict.items():
            if type(v) is bool:
                ret.append(k)
        return ret
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        positive_nums = [i for i in nums if i > 0 ]
        positive_nums.sort()
        zero_nums = [i for i in nums if i == 0 ]
        negative_nums = [i for i in nums if i < 0 ]
        negative_nums.sort()
        
        ret = []
        # pick one from positive nums, pick one from negative nums
        buff_dict = {}
        last_n = None
        if (len(zero_nums) > 2):
            ret.append([0, 0, 0])
        if (len(zero_nums) > 0):
            for i in positive_nums:
                buff_dict[-i] = i
            for i in negative_nums:
                if i == last_n:
                    continue
                if i in buff_dict:
                    ret.append([-i, 0, i])
                last_n = i
        # pick one from positive nums, pick two from negative nums
        last_p = None
        for i in positive_nums:
            if i == last_p:
                continue
            fit_list = self.__temp(negative_nums, -i)
            for j in fit_list:
                ret.append([j, -i-j, i])
            last_p = i
        # pick two from positive nums, pick one from negative nums
        last_n = None
        for i in negative_nums:
            if i == last_n:
                continue
            fit_list = self.__temp(positive_nums, -i)
            for j in fit_list:
                ret.append([i, -i-j, j])
            last_n = i
        return ret


if __name__ == "__main__":
    start = timeit.default_timer()
    so = Solution()
    # nums = [14,-11,-2,-3,4,-3,-3,-8,-15,11,11,-6,-14,-13,5,-10,-13,0,-12,-8,14,-12,-10,2,-4,9,13,10,2,7,-2,-7,4,11,5,-7,-15,10,-7,-14,6,11,-5,7,6,8,5,8,-7,8,-15,14,11,13,1,-15,7,0,10,-14,14,-15,-14,3,4,6,4,4,-7,12,5,14,0,8,7,13,1,-11,-2,9,12,-1,8,0,-11,-5,0,11,2,-13,4,1,-12,5,-10,-1,-12,9,-12,-11,-2,9,-12,5,-6,2,4,10,6,-13,4,3,-7,-11,11,-3,-9,-4,-15,8,-9,-4,-13,-14,8,14]
    # nums = [-1, 0, 1, 2, -1, -4, -1]
    nums = [3,0,-2,-1,1,2]
    ret = so.threeSum(nums)
    print(ret)
    stop = timeit.default_timer()
    print('Time: ', stop - start) 