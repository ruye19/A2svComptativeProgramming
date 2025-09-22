class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0 for _ in range(n)]
        for v in bookings:
            res[v[0] - 1] += v[2]
            if (v[1] < n):
                 res[v[1]] -= v[2]

        for i in range(1, len(res)):
            res[i] += res[i - 1]
        return res