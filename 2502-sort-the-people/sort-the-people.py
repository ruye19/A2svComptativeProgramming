class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        #   | min-index
        # 5 9 6 7 4 0
        #           | min-at
        max_index = 0
        for i in range(len(names)):
            max_at = max_index
            for j in range(max_index, len(names)):
                if heights[max_at] < heights[j]:
                    max_at = j
            names[max_index], names[max_at] =  names[max_at], names[max_index]
            heights[max_index], heights[max_at] =  heights[max_at], heights[max_index]
            max_index += 1
        return names
                    