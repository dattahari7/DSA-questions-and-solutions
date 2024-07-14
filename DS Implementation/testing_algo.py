# def lengthOfLongestSubstring(s):
#         n = len(s)
#         if n == 0:
#             return 0
#         if n == 1:
#             return 1
#         charMap = {}
#         maxlength = 0
#         left = 0
#         for right in range(n):
#             if (s[right] not in charMap) or charMap[s[right]] < left:
#                 charMap[s[right]] = right
#                 maxlength = max(maxlength, right-left+1)
#             else:
#                 left = charMap[s[right]] + 1
#                 charMap[s[right]] = right
#         return maxlength

# print(lengthOfLongestSubstring("pwwkew"))


# class Solution:
#     def dutchFlagSort(self, nums):
#         # Write your code here
#       red_ptr = 0
#       white_ptr = 0
#       blue_ptr = len(nums) - 1
      
#       # Iterate through the array
#       while white_ptr <= blue_ptr:
#           if nums[white_ptr] == 0:  # Red ball
#               nums[red_ptr], nums[white_ptr] = nums[white_ptr], nums[red_ptr]
#               red_ptr += 1
#               white_ptr += 1
#           elif nums[white_ptr] == 1:  # White ball
#               white_ptr += 1
#           else:  # Blue ball
#               nums[white_ptr], nums[blue_ptr] = nums[blue_ptr], nums[white_ptr]
#               blue_ptr -= 1
      
#       return numssThanCurrent(nums)


# arr = [1,2,3,4]
# prefix = [0] * len(arr)
# suffix = [0] * len(arr)

# print(arr, prefix, suffix, sep="\n")




# from collections import Counter

# class Solution:
#     def count_anagrams(self, s, c):
#         curr_win, freqC = {}, Counter(c)
#         have, need = 0, len(freqC)
#         count, left = 0, 0

#         for right, char in enumerate(s):
#             curr_win[char] = curr_win.get(char, 0) + 1
#             if char in freqC and curr_win[char] == freqC[char]:
#                 have += 1

#             while have == need:
#                 count += 1
#                 curr_win[s[left]] -= 1
#                 if s[left] in freqC and curr_win[s[left]] < freqC[s[left]]:
#                     have -= 1
#                 left += 1

#         return count

# # Example usage:
# solution = Solution()
# S1 = "fororfrdofr"
# C1 = "for"
# print(solution.count_anagrams(S1, C1))  # Output: 3

# S2 = "aabaabaa"
# C2 = "aaba"
# print(solution.count_anagrams(S2, C2))  # Output: 4


# printing subsequences using recusion

# def printF(idx, res, arr, n):
#     if idx == n:
#         # for num in res:
#         #     print(num, end=" ")
#         print(res, end="\n")
#         # if len(res) == 0:
#         #     print("[]")
#         # print()
#         return
#     res.append(arr[idx])
#     printF(idx+1, res, arr, n)
#     res.pop()
#     printF(idx+1, res, arr, n)

# arr = [3,1,2]
# n = len(arr)
# res = []
# printF(0, res, arr, n)


# def mergesort(arr, low, high):
#     if low >= high:
#         return
#     mid = low + (high - low) // 2
#     mergesort(arr, low, mid)
#     mergesort(arr, mid+1, high)
#     merge(arr, low, mid, high)

# def merge(arr, left, mid, right):
#     pass

# arr = [5,3,1,2,4]
# mergesort(arr,)


