class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        newstr = ''
        if (x == 0):
            return x

        if (x < 0):
            xstr = str(abs(x));
            for i in reversed(xstr):
                newstr += i
            output = '-' + newstr;
            if (abs(int(newstr)) >= 2147483647):
                return 0
            else:
                return int(output)

        if (x > 0):
            xstr = str(x);
            for i in reversed(xstr):
                newstr += i
            if (int(newstr) >= 2147483647):
                return 0
            else:
                return int(newstr)