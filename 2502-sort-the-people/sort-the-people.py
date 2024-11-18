class Solution(object):
    def sortPeople(self, names, height):
        length=len(height)
        for i in range(length):
            max_index=i
            for j in range(i+1,length):
                if height[j]>height[max_index]:
                    max_index=j
            height[i],height[max_index]= height[max_index],height[i]
            names[i],names[max_index]= names[max_index],names[i]
        return names   

        