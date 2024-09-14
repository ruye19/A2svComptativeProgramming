class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = []
        carry = 0

        # Make both strings of equal length by padding with zeros
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)

        # Iterate over the strings from right to left
        for i in range(max_len - 1, -1, -1):
            # Add the corresponding bits and the carry
            total = int(a[i]) + int(b[i]) + carry
            
            # Compute the resulting bit and carry
            if total == 2:  # 1 + 1 = 10
                result.append('0')
                carry = 1
            elif total == 3:  # 1 + 1 + carry = 11
                result.append('1')
                carry = 1
            else:  # total is either 0 (0 + 0) or 1 (0 + 1 or 1 + 0)
                result.append(str(total))
                carry = 0

        # If there's a leftover carry, append it
        if carry:
            result.append('1')

        # The result array is in reverse order, so reverse it to get the final result
        return ''.join(reversed(result))