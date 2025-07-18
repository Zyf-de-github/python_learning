# class Solution:
#     def maximumLength(self, nums: list[int]) -> int:
#
#         nums1=list(nums)
#         nums2=list(nums)
#         nums3=list(nums)
#         len1=0
#         len2=0
#         len3=0
#         i=0
#         while i<(len(nums1)-1):
#             if nums1[i]%2==nums1[i+1]%2:
#                 nums1.pop(i+1)
#             else:
#                 i+=1
#         len1=len(nums1)
#         i=0
#         while i<(len(nums2)):
#             if nums2[i]%2==1:
#                 nums2.pop(i)
#             else:
#                 i+=1
#         len2=len(nums2)
#         i=0
#         while i<(len(nums3)):
#             if nums3[i]%2==0:
#                 nums3.pop(i)
#             else:
#                 i+=1
#         len3=len(nums3)
#
#         return max(len1,len2,len3)


# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         data=[]
#         temp=[]
#         for i in range(len(s)):
#             for j in range(i,len(s)):
#                 if s[j] in temp:
#                     if len(data)<len(temp):
#                         data=list(temp)
#                         temp=[]
#                     else:
#                         temp=[]
#                     break
#                 else:
#                     temp.append(s[j])
#                     j+=1
#         if len(data)<len(temp):
#             data=list(temp)
#         return len(data)



# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         temp=0
#         for i in range(len(s)):
#             j=0
#             while i-j>=0 and i+j<len(s):
#                 if s[i-j]==s[i+j]:
#                     j+=1
#                 else:
#                     break
#             if j*2-1>temp:
#                 temp=j*2-1
#                 final=list(s[i-j+1:i+j])
#
#         for i in range(len(s)):
#             j=0
#             while i-j>=0 and i+j+1<len(s):
#                 if s[i-j]==s[i+j+1]:
#                     j+=1
#                 else:
#                     break
#             if j*2>temp:
#                 temp=j*2
#                 final=list(s[i-j+1:i+j])
#         return ''.join(final)


class Solution:
    def minimumDifference(self, nums: list[int]) -> int:
        import heapq
        MaxHeap = []
        MinHeap = []
        left = [0] *((len(nums) // 3)+1)
        right = [0] *((len(nums) // 3)+1)
        x = 0
        for i in range(len(nums) // 3 * 2):
            heapq.heappush(MaxHeap, -nums[i])
            if len(MaxHeap) > len(nums) // 3:
                heapq.heappop(MaxHeap)
            if len(MaxHeap) == len(nums) // 3:
                left[x] = -sum(MaxHeap)
                x += 1
        x = len(nums) // 3
        for i in range(len(nums) - 1, len(nums) // 3 - 1, -1):
            heapq.heappush(MinHeap, nums[i])
            if len(MinHeap) > len(nums) // 3:
                heapq.heappop(MinHeap)  # 弹出负数等于减去原最大数
            if len(MinHeap) == len(nums) // 3:
                right[x] = sum(MinHeap)
                x -= 1
        resault = 100000
        for i in range(len(left)):
            if left[i] - right[i] < resault:
                resault = left[i] - right[i]
        return resault


if __name__ == '__main__':
    s=[50,92,65,812,689,105,905,702,721,600,566,598,868,682,985,786,953,71,559,406,521,711,831,955,865,627,812,183,502,297,97,845,313,778,781,454,237,79,442,31,428,15,510,454,207,564,300,857,7,175,260,127,364,465,660,49,636,786,884,139,555,517,535,986,485,998,754,146,921,241,830,244,77,518,915,278,535,237,723,388,1,718,789,27,989,210,7,666,233,705,897,917,470,43,699,693,424,578,959,446,533,669,101,212,56,557,279,559,68,398,93,915,552,13,524,881,164,317,770,632,63,132,798,898,507,339,552,932,305,837,283,230,36,360,977,328,825,442,777,233,87,538,786,573,723,611,911,96,492,8,161,448,604,759,249,9]
    print(Solution().minimumDifference(s))