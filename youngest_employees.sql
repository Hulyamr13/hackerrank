SELECT e_u.uin, e.name
FROM employee e
JOIN employee_uin e_u ON e.id = e_u.id
WHERE e.age < 25
ORDER BY e.name ASC, e.id ASC;
