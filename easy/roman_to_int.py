'''
    python code to convert roman numbers into integers in range from 0 to 3999
'''


def value(r):
    '''
    :param r: Roman number
    :return: converted into integer
    '''
    if (r == 'I'):
        return 1
    if (r == 'V'):
        return 5
    if (r == 'X'):
        return 10
    if (r == 'L'):
        return 50
    if (r == 'C'):
        return 100
    if (r == 'D'):
        return 500
    if (r == 'M'):
        return 1000
    return -1
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        i = 0
        while(i < len(s)):
            s1 = value(s[i])
            if (i+1 < len(s)):
                s2 = value(s[i+1])
                if s1 >= s2:
                    res += s1
                    i += 1
                else:
                    res = res + s2 -s1
                    i += 2
            else:
                res += s1
                i += 1
        return res