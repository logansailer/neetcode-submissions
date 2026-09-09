class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnum = ''.join(filter(str.isalnum, s))
        alnum = alnum.lower()
        for i in range(len(alnum)//2):
            if alnum[i] != alnum[-(i+1)]:
                return False
        return True
        