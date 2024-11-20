class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        result=0
        left,right=0,len(skill)-1
        temp=skill[left]+skill[right]
        while(left<right):
            no1=skill[left]+skill[right] 
            if no1==temp:
                result+=skill[left]*skill[right]  
                left+=1
                right-=1
            else:
                return -1    
        return result