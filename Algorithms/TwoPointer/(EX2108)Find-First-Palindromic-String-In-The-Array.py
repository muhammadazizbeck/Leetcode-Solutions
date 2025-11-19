class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        # for word in words:
        #     if word==word[::-1]:
        #         return word
        #         break
        #     else:
        #         continue
            
        # return ""

        def is_palindrome(item):
            left,right=0,len(item)-1
            while left<=right:
                if item[left]!=item[right]:
                    return False
                left += 1
                right -= 1
            return True

        for word in words:
            if is_palindrome(word):
                return word
            else:
                continue
        return ""