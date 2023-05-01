class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        sum=0
        size=len(salary)-2
        for val in salary[1:-1]:
            sum += val

        average=sum/size
        return average