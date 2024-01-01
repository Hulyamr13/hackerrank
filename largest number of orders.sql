SELECT customer_id
FROM orders
GROUP BY customer_id
ORDER BY COUNT(*) DESC
LIMIT 1;
