class Solution:
    def isHappy(self, n: int) -> bool:
        
        
        output = set()
        while n != 0:
            if n == 1:
                return True
            elif n in output:
                return False
            else:
                output.add(n)   
                result = 0
                while n > 0:
                    last = n % 10 
                    result += last **2 
                    n //= 10
                n = result
                
    
        
        
        """
        2
        4
        16
        1 + 36 = 37
        9 + 49 = 58
        25 + 64 = 89
        64 + 81 = 145
        1 + 16 + 25 = 425
        5 * 10 + 2
        425 % 10 = 5
        425 //10 = 42

        42//10 = 4


        16 + 4
        
        
        """