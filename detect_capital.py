class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) <= 0:
            return False
        elif len(word) <= 1:
            return True
        else:
            num_of_capitals = 0
            num_of_lowers = 0
            first_cap = False
            capitals = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            lower = "abcdefghijklmnopqrstuvwxyz"
            for i in range(len(word)):
                if word[i] in capitals:
                    num_of_capitals += 1
                elif word[i] in lower:
                    num_of_lowers += 1
                
                if i == 0 and word[i] in capitals:
                    first_cap = True
                        
            return num_of_capitals == len(word) or num_of_lowers == len(word) or (first_cap and num_of_capitals == 1) 
            
            