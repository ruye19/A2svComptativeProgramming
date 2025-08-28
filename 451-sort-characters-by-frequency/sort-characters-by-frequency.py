class Solution:
    def frequencySort(self, s: str) -> str:
        countter = Counter(s)
        hashmap = defaultdict(list)
        for ch,freq in countter.items():
            hashmap[freq].append(ch)
        result = []
        maximum = max(countter.values())
        for i in range(maximum, -1, -1):
            for letter in hashmap[i]:
                result.append(letter * i)
        return "".join(result)        