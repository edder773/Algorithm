SELECT TRUNCATE(PRICE, -4) as PRICE_GROUP, count(*) AS PRODUCTS
FROM PRODUCT
GROUP BY PRICE_GROUP
ORDER BY PRICE_GROUP