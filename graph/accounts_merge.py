'''
Given a list accounts, each element accounts[i] is a list of strings,
where the first element accounts[i][0] is a name,
and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts.
Two accounts definitely belong to the same person if there is some email
that is common to both accounts. Note that even if two accounts have the same name,
they may belong to different people as people could have the same name.
A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format:
the first element of each account is the name, and the rest of the elements are emails in sorted order.
The accounts themselves can be returned in any order.

Example 1:
Input:
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"],
["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],
["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
Explanation:
The first and third John's are the same person as they have the common email "johnsmith@mail.com".
The second John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'],
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
'''
from collections import defaultdict
from typing import List


#   DSU with union by size and path compression
class DSU:
    def __init__(self) -> None:
        self.parent = {}
        self.size = {}

    def make_set(self, val: int) -> None:
        if val in self.parent:
            return

        self.parent[val] = val
        self.size[val] = 1

    def get_parent(self, val: int) -> int:
        if self.parent[val] == val:
            return val
        #   path compression
        parent = self.get_parent(self.parent[val])
        self.parent[val] = parent
        return parent

    def union(self, set_a: int, set_b: int) -> None:
        parent_a = self.get_parent(set_a)
        parent_b = self.get_parent(set_b)
        if parent_a == parent_b:
            return

        #   union by size
        if self.size[parent_a] >= self.size[parent_b]:
            self.parent[parent_b] = parent_a
            self.size[parent_a] += self.size[parent_b]
        else:
            self.parent[parent_a] = parent_b
            self.size[parent_b] += self.size[parent_a]


#   DSU solution
class Solution:
    def __init__(self):
        self.email_to_id_map = {}
        self.id_counter = 0
        self.email_to_name = {}

    def email_to_id(self, email: str) -> int:
        if email in self.email_to_id_map:
            return self.email_to_id_map[email]

        self.email_to_id_map[email] = self.id_counter
        self.id_counter += 1
        return self.email_to_id_map[email]

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dsu = DSU()

        for account in accounts:
            name = account[0]

            first_email = account[1]
            dsu.make_set(self.email_to_id(first_email))
            self.email_to_name[first_email] = name

            #   connect all emails to first email in group
            for i in range(2, len(account)):
                email = account[i]
                self.email_to_name[email] = name

                dsu.make_set(self.email_to_id(email))
                dsu.union(self.email_to_id(first_email), self.email_to_id(email))

        #   group emails by parent
        #   key = parent_id, value - array of emails
        emails = defaultdict(list)
        for email in self.email_to_name.keys():
            parent_id = dsu.get_parent(self.email_to_id(email))
            emails[parent_id].append(email)

        result = []
        for parent_id, emails_list in emails.items():
            first_email = emails_list[0]
            name = self.email_to_name[first_email]
            emails_list.insert(0, name)
            result.append(list(sorted(emails_list)))
        return result


solution = Solution()
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"],
            ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
print(solution.accountsMerge(accounts))
