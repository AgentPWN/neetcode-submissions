class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sort = sorted(nums)
        count = 1
        count_list = []
        print(len(sort))
        print(sort)
        if len(sort) == 1:
            count_list.append(1)
        elif len(sort) == 0:
            count_list.append(0)
        else:
            for i in range(len(sort)-1):
                if sort[i] == sort[i+1] - 1:
                    count += 1
                elif sort[i] == sort[i+1]:
                    continue
                else:
                    count_list.append(count)
                    count = 1
            count_list.append(count)
        return max(count_list)