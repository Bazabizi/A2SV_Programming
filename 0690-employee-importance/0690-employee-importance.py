"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        self.ans = 0
        def dfs(employee):
            if not employee:
                return
            
            self.ans += employee.importance
            
            if not employee.subordinates:
                return
            for subordinate in employee.subordinates:
                for e in employees:
                    if e.id == subordinate:
                        dfs(e)
            
        
        for employee in employees:
            if employee.id == id:
                dfs(employee)
                break
        
        return self.ans