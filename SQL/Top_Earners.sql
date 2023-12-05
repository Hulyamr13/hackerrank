SELECT MAX(months * salary) AS max_earnings,
       COUNT(*) AS employees_with_max_earnings
FROM Employee
WHERE months * salary = (
    SELECT MAX(months * salary)
    FROM Employee
);
