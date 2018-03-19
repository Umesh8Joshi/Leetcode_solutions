class Solution:
    def plusone(self, digits):
        return [x+1 for x in digits]

if __name__ == '__main__':
    s = Solution
    a = [9]
    print(s.plusone(a))