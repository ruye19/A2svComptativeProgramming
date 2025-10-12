class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
                  
        rem = [0 for _ in range(k)]
        for num in arr:
            rem[num%k] += 1
            
        # k = 6
        # 0 1 2 3 4 5
        
        for i in range(1, k):
            if rem[i] != rem[k - i] or (k%2 == 0 and rem[k//2] % 2 != 0):
                return False
                
        return True