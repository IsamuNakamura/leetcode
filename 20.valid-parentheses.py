#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:

        if  len(s) < 1 or 10 ** 4 < len(s):
            return False

        stack = []
        dict = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []





# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.isValid("{{[]}}"))
    print(s.isValid("[}{]"))
