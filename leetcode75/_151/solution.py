# https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=leetcode-75
                
class Solution:
    @staticmethod
    def reverseWords(s: str) -> str:

        i = len(s) - 1
        word, rev = "", ""
        more_than_one_word = False
        while i >= 0:
            if s[i] == " ":
                if word != "":
                    if more_than_one_word:
                        rev += " "
                    rev += word
                    word = ""
                    more_than_one_word = True
                i -= 1
                continue
            word = s[i] + word  # not space
            i -= 1
        if word != "":
            rev += (" " if more_than_one_word else "") + word

        return rev

