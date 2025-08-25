class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(arr, k):
            arr[:k] = arr[:k][::-1]
            return arr
        output = []
        for i in range(len(arr) - 1, -1 , -1):
            maxx = i 
            for j in range(i , -1, -1):
                if arr[j] > arr[maxx]:
                    maxx = j
            if maxx != i:
                flip(arr, maxx + 1)
                flip(arr, i + 1)
                output.append(maxx + 1)
                output.append(i + 1)
        return output                 

            

        return arr    
            