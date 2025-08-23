class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        maxx = max(max(seats) , max(students)) + 1
        count1 = [0] * maxx
        count2 = [0] * maxx
        for seat in seats:
            count1[seat] += 1
        for stud in students:
            count2[stud] += 1

        i, j = 0, 0
        remain = len(students)        
        output = 0
        while remain:
            if count1[i] == 0:
                i += 1
            if count2[j] == 0:
                j += 1
            if count1[i] and count2[j]:
                output += abs(i - j)
                count1[i] -= 1
                count2[j] -= 1
                remain -= 1
        return output    



    
             
        