# Write your MySQL query statement below
SELECT # select again to get null otherwise will return nothing
    (SELECT DISTINCT salary 
        FROM Employee
        ORDER BY salary DESC
        LIMIT 1 OFFSET 1) AS SecondHighestSalary;