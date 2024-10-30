from typing import List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ans = set()

        for email in emails:
            tmp = ""
            tmp_list = email.split("@")
            for c in tmp_list[0]:
                if c == "+":
                    break
                elif c == ".":
                    continue
                tmp += c
            tmp = tmp + "@" + tmp_list[1]    
            ans.add(tmp)    

        return len(ans)
    
class NeetSolution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        unique_emails: set[str] = set()
        for email in emails:
            local_name, domain_name = email.split('@')
            local_name = local_name.split('+')[0]
            local_name = local_name.replace('.', '')
            email = local_name + '@' + domain_name
            unique_emails.add(email)
        return len(unique_emails)
    
class NeetSolution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()

        for e in emails:
            i, local = 0, ""
            while e[i] not in ["@", "+"]:
                if e[i] != ".":
                    local += e[i]
                i += 1

            while e[i] != "@":
                i += 1
            domain = e[i + 1:]
            unique.add((local, domain))
        
        return len(unique)