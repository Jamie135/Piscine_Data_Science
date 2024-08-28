CREATE TEMPORARY TABLE tmp AS 
SELECT * FROM customers;

-- from the temporary table, remove all duplicates rows.
-- we use ctid to have the unique identifier of the row
-- PARTITION : fonction ROW_NUMBER() attribue num ligne pour chaque groupe
-- (SELECT ctid, ROW_NUMBER() OVER(..) AS row_num FROM cust) AS duplicates:
-- fonction ROW_NUMBER() attribue num ligne à chaque groupe en double,
-- où groupe défini par colonnes spécifiées dans la clause PARTITION BY.
DELETE FROM tmp WHERE ctid IN (
SELECT ctid FROM (
    SELECT ctid, ROW_NUMBER() OVER(
            PARTITION BY date_trunc('minute', event_time),
            event_type,
            product_id,
            price,
            user_id,
            user_session ORDER BY event_time DESC
        ) AS row_num FROM customers
    ) AS duplicates WHERE duplicates.row_num > 1 );

DROP TABLE customers;

CREATE TABLE customers AS
SELECT *
FROM tmp
ORDER BY event_time;

DROP TABLE tmp;



-- SELECT COUNT(*) AS total_rows FROM customers;

-- SELECT COUNT(*) AS distinct_rows
-- FROM (
--     SELECT DISTINCT ROW(event_time, event_type, product_id, price, user_id, user_session)
--     FROM customers
-- ) AS distinct_table;
