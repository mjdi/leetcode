# https://leetcode.com/problems/decode-string/description/?envType=study-plan-v2&envId=leetcode-75
                
class Solution:
    @staticmethod
    def decodeString(s: str) -> str:
        def decodeStringIndex(s: str, i: int) -> str:
            result = ""
            while i < len(s) and s[i] != "]":
                if not s[i].isdigit():
                    result += s[i]
                    i += 1
                else:
                    k = ""
                    while i < len(s) and s[i].isdigit():
                        k += s[i]
                        i += 1
                    i += 1  # ignore '['
                    decodedString, i = decodeStringIndex(s, i)
                    i += 1  # ignore ']'
                    result += int(k) * decodedString
            return result, i

        index = 0
        return decodeStringIndex(s, index)[0]
