class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        count = 0 
        capa = capacity
        for i in range(len(plants)):
            if plants[i] <= capacity:
                capacity = capacity - plants[i]
                plants[i] = 0
                count += 1
            else:
                count += 2 * i + 1
                capacity = capa
                capacity = capacity - plants[i]


        return count         
