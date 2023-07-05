class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # only 1's array or 0's array
        if len(list(set(nums))) == 1:
            if nums[0]==1:
                return len(nums)-1
            else:
                return 0
        else:
            # make a dictionary of 111 arrays 
            num_dct = {}
            group = 1
            partSum = 0
            lst = []
            while nums:
                n = nums.pop()
                if n == 1:
                    partSum += 1
                elif (n == 0) and (partSum > 0):
                    num_dct[group] = partSum
                    partSum = 0
                    group += 1
                # 중간에 0이 여러개 들어가 있는 경우
                elif (n==0) and (partSum==0) and num_dct:
                    if len(num_dct) > 1:
                        # print(num_dct)
                        tmp = [num_dct[i] + num_dct[i+1] for i in range(1, len(num_dct))]
                        # print(tmp)
                        lst.append(max(tmp))
                    else:
                        lst.append(num_dct[1])
                    num_dct = {}
                    group = 1

            if partSum > 0:
                num_dct[group] = partSum

            if lst:
                if num_dct:
                    if len(num_dct) > 1:
                        tmp = [num_dct[i] + num_dct[i+1] for i in range(1, len(num_dct))]
                        lst.append(max(tmp))
                    else:
                        lst.append(num_dct[1])

                return max(lst)

            else:
                if len(num_dct) > 1:
                    tmp = [num_dct[i] + num_dct[i+1] for i in range(1, len(num_dct))]
                    return max(tmp)
                else:
                    return num_dct[1]
   