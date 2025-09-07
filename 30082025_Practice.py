# Longest Palindraome
# https://leetcode.com/problems/longest-palindromic-substring/submissions/1753135226/
from pyarrow.compute import fill_null


class palindrome:
    def longestPalindrome(self, string_: str) -> str:
        if len(string_) <= 1:
            return string_

        # Constraint is that the number of characters can be 1000 too
        # With increase in the length of characters the complexity increases

        max_length = 1
        max_string = string_[0]

        for i in range(len(string_)-1):
            #print(i)
            for j in range(i+1, len(string_)):
                print(i,j,(j-i+1), max_length, string_[i:j+1],string_[i:j+1][::-1])
                if j-i+1 > max_length and string_[i:j+1] == string_[i:j+1][::-1]:
                    max_length = j-i+1
                    max_string = string_[i:j+1]

        return max_string

    def longestPalindrome1(self, s: str) -> str:
        if len(s) <= 1:
            return s

        def expand_from_center(left, right):
            print("1,", left, right, s[left], "==", s[right])
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                print(left, right,s[left], "==", s[right])
                print("***********")
            print("##########")
            return s[left + 1:right]

        max_str = s[0]

        for i in range(len(s) - 1):
            print("Odd")
            odd = expand_from_center(i, i)
            print("Even")
            even = expand_from_center(i, i + 1)

            if len(odd) > len(max_str):
                max_str = odd
            if len(even) > len(max_str):
                max_str = even
            print(i, odd, even, max_str)
        return max_str

    def longestPlaindrome_method3(self, s:str) -> str:
        if len(s) <= 1:
            return s

        max_length = 1
        max_string = s[0]

        dp = [[False for _ in range(len(s))] for _ in range(len(s))]

        #print(dp)



obj_palindrome = palindrome() # object creation/ Instantiation
#palindrome = obj_palindrome.longestPalindrome("cbbdscdadfr")
#print(palindrome)

#palindrome1 = obj_palindrome.longestPalindrome1("cbbdscdadfr")
#print(palindrome1)

palindrome3 = obj_palindrome.longestPlaindrome_method3("cbba")
print(palindrome3)
