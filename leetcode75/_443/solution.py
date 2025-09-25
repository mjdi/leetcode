# https://leetcode.com/problems/string-compression/?envType=study-plan-v2&envId=leetcode-75
from typing import List
                
class Solution:
    @staticmethod
    def compress(chars: List[str]) -> int:
        if len(chars) == 1:
            return 1

        curr_char = chars[0]
        char_ctr = 0
        write_ptr = 0

        def work(i, chars, curr_char, char_ctr, write_ptr):
            char = chars[i] if i < len(chars) else ""
            if char == curr_char:
                char_ctr += 1
            else:
                chars[write_ptr] = curr_char  # write char
                write_ptr += 1
                if char_ctr != 1:
                    for digit in str(char_ctr):  # write num chars
                        chars[write_ptr] = digit
                        write_ptr += 1
                curr_char = char
                char_ctr = 1

            # print(f'{i=}, {chars=}, {curr_char=}, {char_ctr=}, {write_ptr=}')
            return chars, curr_char, char_ctr, write_ptr

        for i in range(0, len(chars)):
            chars, curr_char, char_ctr, write_ptr = \
                work(i, chars, curr_char, char_ctr, write_ptr)

        chars, curr_char, char_ctr, write_ptr = \
            work(len(chars), chars, curr_char, char_ctr, write_ptr)

        # print(chars)
        chars = chars[:write_ptr]
        # print(chars)

        return len(chars)

# can avoid defining a function if you modify the first condition, and range(1, len(chars + 1))

# class Solution: (chun2lu)
#     def compress(self, chars: List[str]) -> int:
#         count = 1
#         left = 0

#         for right in range(1,len(chars)+1):
#             if right < len(chars) and chars[right-1] == chars[right]:
#                 count += 1
#             else:
#                 chars[left] = chars[right-1]
#                 left += 1
#                 if count > 1:
#                     for c in str(count):
#                         chars[left] = c
#                         left += 1
#                 count = 1

#         return left
