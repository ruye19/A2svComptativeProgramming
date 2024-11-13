class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        first= 0
        last= len(s) - 1
        while(first<last):
            s[first], s[last] = s[last], s[first]
            first += 1
            last -= 1
            