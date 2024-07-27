class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        bal_dict = {'b':1, 'a':1, 'l':2, 'o':2, 'n':1}
        text_dict = {'b':0, 'a':0, 'l':0, 'o':0, 'n':0}

        for i in range(len(text)):
            if text[i] in text_dict.keys():
                text_dict[text[i]] += 1
        
        res = []
        for i,j in text_dict.items():
            res.append(j // bal_dict[i])
        return min(res)
