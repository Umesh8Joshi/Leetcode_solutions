class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        self._restoreIpAddresses(0, s, [], result)
        return result

    def _restoreIpAddresses(self, length, s, ips, result):
        if not s:
            if length == 4:
                result.append('.'.join(ips))
            return
        elif length == 4:
            return
        self._restoreIpAddresses(length + 1, s[1:], ips + [s[:1]], result)
        if s[0] != '0':
            if len(s) >= 2:
                self._restoreIpAddresses(length + 1, s[2:], ips + [s[:2]], result)
            if len(s) >= 3 and int(s[:3]) <= 255:
                self._restoreIpAddresses(length + 1, s[3:], ips + [s[:3]], result)
