CREATE TABLE tmp AS
SELECT c.*, category_id, category_code, brand
FROM customers c
LEFT JOIN items i ON c.product_id = i.product_id;

DROP TABLE IF EXISTS customers;
ALTER TABLE tmp RENAME TO customers

-- CREATE TABLE tmp AS (
--     SELECT 
--         c.event_time, 
--         c.event_type,
--         c.product_id,
--         category_id,
--         category_code,
--         brand,
--         c.price,
--         c.user_id,
--         c.user_session
--     FROM 
--         customers c
--     JOIN 
--         items i 
--     ON 
--         c.product_id = i.product_id
--     ORDER BY 
--         c.event_time
-- );

-- DROP TABLE customers;

-- ALTER TABLE tmp RENAME TO customers;
