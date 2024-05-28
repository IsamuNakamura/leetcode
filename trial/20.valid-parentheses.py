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
        bracketMap = {
            "(":")",
            "[":"]",
            "{":"}"
        }
        for char in s:
            if char in bracketMap:
                stack.append(bracketMap[char])
            elif char in bracketMap.values():
                if stack == [] or char != stack.pop():
                    return False
            else:
                return False
        return stack == []





# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.isValid("{{[]}}"))
    print(s.isValid("[}{]"))
