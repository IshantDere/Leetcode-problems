class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        word = s.split()
        last_word = word[-1]
        len_of_word = len(last_word)

        return len_of_word