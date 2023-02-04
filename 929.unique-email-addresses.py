#
# @lc app=leetcode id=929 lang=python3
#
# [929] Unique Email Addresses
#

# @lc code=start
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        index_list = 0
        index_letter = 0
        hashMap = {}
        for email in emails:
            local, domain = email.split('@')
            local = local.replace('.', '')
            changed_email = local.split('+')[0] + '@' + domain
            hashMap[changed_email] = email
        return len(hashMap)

# @lc code=end
