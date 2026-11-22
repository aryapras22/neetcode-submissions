class Solution:
    def isPalindrome(self, s: str) -> bool:
    # First things off that the string input need to be cleaned from regex
    # or maybe could be inserted into an array that skip space, and regex
    # after the array created we can create another copy of an array that reversed
    # we can compare both array
    # but i think the string on python are sort of array

        text = s.strip().lower().replace(" ","").replace("?","").replace(".","").replace(",","").replace("'","").replace(":", "").replace("!","")
        reversed_text = "".join(reversed(text))
        return reversed_text == text