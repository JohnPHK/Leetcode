class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        _dict = {}
        characters = string.ascii_lowercase
        for i in range(len(characters)):
            _dict[characters[i]] = i
        
        s1_lst = [0 for _ in range(26)]
        
        for ch in s1:
            s1_lst[_dict[ch]] += 1
        
        
        len_s1 = len(s1)
        
        for i in range(len(s2) - len_s1 + 1):
            tmp = s1_lst.copy()

            for ch in s2[i: i+len_s1]:
                if tmp[_dict[ch]] > 0:
                    tmp[_dict[ch]] -= 1
            if sum(tmp) == 0:
                return True
        return False
                
            