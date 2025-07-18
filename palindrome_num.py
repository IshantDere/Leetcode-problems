class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y = str(x)
        
        list1 = []
        list2 = []

        for i in y:
            list1.append(i)
        for i in reversed(y):
            list2.append(i) 

        if list1 == list2:
            return True
        else:
            return False