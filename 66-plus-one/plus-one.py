class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] = digits[-1] + 1
        i = len(digits) - 1

        while i >= 0:
            if digits[i] >= 10:
                carry = digits[i] // 10
                digits[i] = digits[i] % 10
                if i == 0:
                    digits = [carry] + digits
                else:
                    digits[i - 1] += carry
            i -= 1

        return digits
