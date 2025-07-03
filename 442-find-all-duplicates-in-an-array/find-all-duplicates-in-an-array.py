class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count={}
        output=[]
        for i in nums:
            count[i]=1+count.get(i,0)
        for  val,countt in count.items():
            if countt>=2:
                output.append(val) 
        return output                  