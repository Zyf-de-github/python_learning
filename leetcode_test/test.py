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


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        data=[]
        temp=[]
        for i in range(len(s)):
            for j in range(i,len(s)):
                if s[j] in temp:
                    if len(data)<len(temp):
                        data=list(temp)
                        temp=[]
                    else:
                        temp=[]
                    break
                else:
                    temp.append(s[j])
                    j+=1
        if len(data)<len(temp):
            data=list(temp)
        return len(data)

if __name__ == '__main__':
    c='dvdf'
    print(Solution().lengthOfLongestSubstring(c))