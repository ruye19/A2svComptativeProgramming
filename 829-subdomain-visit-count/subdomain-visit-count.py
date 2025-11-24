class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domainCount = defaultdict(int)
        for i in cpdomains:
            visit, domain = i.split()
            domainCount[domain] += int(visit)
            for j in range (len(domain)):
                if domain[j] == ".":
                    sub = domain[j + 1:]
                    domainCount[sub] += int(visit)
        output = []
        for d in domainCount:
            ab = [str(domainCount[d]), d]
            output.append(" ".join(ab))
        return output    
