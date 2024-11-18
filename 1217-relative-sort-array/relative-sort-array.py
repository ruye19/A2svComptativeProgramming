class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        in_arr2=[x for x in arr1 if x in arr2]
        notIn_arr2=[x for x in arr1 if x not in arr2]
        sortbased=sorted(in_arr2,key=lambda x: arr2.index(x))
        sort_Other=sorted(notIn_arr2)
        return sortbased + sort_Other