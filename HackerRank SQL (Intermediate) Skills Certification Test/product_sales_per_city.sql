SELECT
    ci.city_name,
    pr.product_name,
    ROUND(SUM(ii.line_total_price), 2) AS tot
FROM
    city AS ci
INNER JOIN customer AS cu ON ci.id = cu.city_id
INNER JOIN invoice AS i ON cu.id = i.customer_id
INNER JOIN invoice_item AS ii ON i.id = ii.invoice_id
INNER JOIN product AS pr ON ii.product_id = pr.id
GROUP BY
    ci.city_name,
    pr.product_name
ORDER BY
    tot DESC,
    ci.city_name,
    pr.product_name;
