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


# class Solution:
#     def minimumDifference(self, nums: list[int]) -> int:
#         import heapq
#         MaxHeap = []
#         MinHeap = []
#         left = [0] *((len(nums) // 3)+1)
#         right = [0] *((len(nums) // 3)+1)
#         x = 0
#         for i in range(len(nums) // 3 * 2):
#             heapq.heappush(MaxHeap, -nums[i])
#             if len(MaxHeap) > len(nums) // 3:
#                 heapq.heappop(MaxHeap)
#             if len(MaxHeap) == len(nums) // 3:
#                 left[x] = -sum(MaxHeap)
#                 x += 1
#         x = len(nums) // 3
#         for i in range(len(nums) - 1, len(nums) // 3 - 1, -1):
#             heapq.heappush(MinHeap, nums[i])
#             if len(MinHeap) > len(nums) // 3:
#                 heapq.heappop(MinHeap)  # 弹出负数等于减去原最大数
#             if len(MinHeap) == len(nums) // 3:
#                 right[x] = sum(MinHeap)
#                 x -= 1
#         resault = 100000
#         for i in range(len(left)):
#             if left[i] - right[i] < resault:
#                 resault = left[i] - right[i]
#         return resault





# from typing import Optional
#
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# def list_to_linkedlist(lst):
#     dummy = ListNode(0)
#     cur = dummy
#     for val in lst:
#         cur.next = ListNode(val)
#         cur = cur.next
#     return dummy.next
#
# def linkedlist_to_list(node):
#     res = []
#     while node:
#         res.append(node.val)
#         node = node.next
#     return res
#
# class Solution:
#     def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         temp=ListNode(0)
#         mid=ListNode(0)
#         result=ListNode(0)
#         mid.next=head
#         temp.next=head
#         result.next=mid
#         NumList=[]
#         ReNumList=[]
#         while head!=None:
#             if head.val not in NumList:
#                 NumList.append(head.val)
#             else:
#                 if head.val not in ReNumList:
#                     ReNumList.append(head.val)
#             head=head.next
#         while temp.next!=None:
#             while temp.next!=None and temp.next.val in ReNumList:
#                 temp=temp.next
#             mid.next=temp.next
#             mid=mid.next
#             temp=temp.next
#         return result.next.next



class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        result=[]
        nums.sort()
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i+1,len(nums)-2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left=j+1
                right=len(nums)-1
                while left<right:
                    if nums[i]+nums[j]+nums[left]+nums[right]>target:
                        while left<right and nums[right]==nums[right-1]:
                            right-=1
                        right-=1
                    elif nums[i]+nums[j]+nums[left]+nums[right]<target:
                        while left<right and nums[left]==nums[left+1]:
                            left+=1
                        left+=1
                    else:
                        result.append([nums[i],nums[j],nums[left],nums[right]])
                        right-=1
                        left+=1
        return result


if __name__ == '__main__':
    test_list = [-2,-1,-1,1,1,2,2]
    test=Solution().fourSum(test_list,0)
    # print("原始列表:", test_list)
    # head = list_to_linkedlist(test_list)
    # new_head = Solution().deleteDuplicates(head)
    # result_list = linkedlist_to_list(new_head)
    # print("去重后结果:", result_list)
