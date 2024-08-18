CREATE TEMPORARY TABLE tmp AS SELECT DISTINCT * FROM customers;
TRUNCATE customers;
INSERT INTO customers SELECT * FROM tmp;

-- WITH CTE AS (
--     SELECT *,
--            ROW_NUMBER() OVER (PARTITION BY event_time, event_type, product_id, price, user_id, user_session ORDER BY event_time) AS n
--     FROM customers
-- )
-- DELETE FROM customers
-- WHERE ctid IN (
--     SELECT ctid
--     FROM CTE
--     WHERE n > 1
-- );


-- SELECT COUNT(*) AS total_rows FROM customers;

-- SELECT COUNT(*) AS distinct_rows
-- FROM (
--     SELECT DISTINCT ROW(event_time, event_type, product_id, price, user_id, user_session)
--     FROM customers
-- ) AS distinct_table;
