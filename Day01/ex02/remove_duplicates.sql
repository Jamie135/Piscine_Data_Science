WITH cte AS (
    SELECT *,
        LAG(event_time) OVER (PARTITION BY event_type, product_id, price, user_id, user_session ORDER BY event_time) AS lag
    FROM customers
)
DELETE FROM customers
USING cte
WHERE customers.event_time = cte.event_time
AND customers.event_type = cte.event_type
AND customers.product_id = cte.product_id
AND customers.price = cte.price
AND customers.user_id = cte.user_id
AND customers.user_session = cte.user_session
AND (cte.event_time - cte.lag <= INTERVAL '1 second' AND cte.lag IS NOT NULL);


-- CREATE TABLE tmp AS
-- WITH cte AS (
--     SELECT *,
--     LAG(event_time) OVER (PARTITION BY event_type, product_id, price, user_id, user_session ORDER BY event_time) AS lag
--     FROM customers
-- )
-- SELECT event_time, event_type, product_id, price, user_id, user_session
-- FROM cte
-- WHERE event_time - lag > INTERVAL '1 second'
-- OR lag IS NULL;
-- DROP TABLE customers;
-- ALTER TABLE tmp RENAME TO customers;


-- SELECT COUNT(*) AS total_rows FROM customers;

-- SELECT COUNT(*) AS distinct_rows
-- FROM (
--     SELECT DISTINCT ROW(event_time, event_type, product_id, price, user_id, user_session)
--     FROM customers
-- ) AS distinct_table;
