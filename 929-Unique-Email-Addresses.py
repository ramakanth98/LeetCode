class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = []
        for mail in emails:
            temp = mail.split('@')
            if temp[-1].endswith('.com'):
                hehe = temp[0].replace(".","")
                hehe = hehe.split('+')[0]
                res.append(hehe + '@' + temp[-1])
            else:
                continue
        return(len(set(res)))



        