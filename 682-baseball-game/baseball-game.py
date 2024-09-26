class Solution:
    def calPoints(self, operations: List[str]) -> int:
        rec=[]
       
        for re in operations:
            if re.lstrip('-').isdigit():
                rec.append(int(re))
            elif re == "+":
                rec.append(rec[-1]+rec[-2])
            elif re=="D":
                rec.append(2*rec[-1])
            elif re=="C":
                rec.pop()
        return sum(rec)                  