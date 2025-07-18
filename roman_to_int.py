class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        roman_to_int = {
            "I" : 1,
            "V" : 5,
            "X" : 10, 
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        total = 0
        previous_num = 0

        for i in reversed(s):
            
            if roman_to_int[i] < previous_num:
                total -= roman_to_int[i]
            else :
                total += roman_to_int[i]
            previous_num = roman_to_int[i]

        return total
