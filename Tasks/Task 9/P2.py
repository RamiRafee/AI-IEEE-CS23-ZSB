class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        #iterate through the string and remove any non-alphanumeric characters
        i = 0
        while (i<len(s)):
            
            while(i<len(s) and  not (s[i].isalpha() or s[i].isdigit())):
                s = s.replace(s[i],'')
            i += 1

        #two pointers checking the palindrome
        first = 0
        last = len(s) - 1
        while (first <= last):
            if(s[first] != s[last] ):
                return False
            first += 1
            last -= 1
        
        return True