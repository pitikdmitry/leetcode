'''
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
'''
from typing import List


class Solution:
    def is_valid(self, sections):
        for section in sections:
            if int(section) > 255:
                return False

            if len(str(int(section))) != len(section):
                return False
        return True

    def generate(self, s, start, sections, valid_sections):
        if len(sections) == 4 and start == len(s):
            if self.is_valid(sections):
                valid_sections.append('.'.join(sections))
                return
            elif len(sections) == 4:
                return

        cur_section = ''
        for i in range(start, start + 3):
            if i >= len(s):
                return

            cur_section += s[i]
            sections.append(cur_section)
            self.generate(s, i + 1, sections, valid_sections)
            sections.pop()

    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 4 * 3:
            return []
        valid_sections = []
        self.generate(s, 0, [], valid_sections)
        return valid_sections


solution = Solution()
s = '25525511135'
print(solution.restoreIpAddresses(s))
