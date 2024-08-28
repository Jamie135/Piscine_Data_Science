CREATE TABLE tmp_customers (
    event_time TIMESTAMP NOT NULL,
    event_type VARCHAR(255),
    product_id INT,
    price FLOAT,
    user_id BIGINT,
    user_session UUID,
    category_id BIGINT,
    category_code VARCHAR(255),
    brand VARCHAR(255));

CREATE TABLE tmp_items(
    product_id INT,
    category_id BIGINT,
    category_code VARCHAR(255),
    brand VARCHAR(255));

INSERT INTO tmp_items (product_id, category_id,
category_code, brand)
SELECT
    "product_id",
    MAX("category_id") AS "category_id",
    MAX("category_code") AS "category_code",
    MAX("brand") AS "brand"
FROM items
GROUP BY "product_id";

INSERT INTO tmp_customers
SELECT c.event_time, c.event_type, c.product_id,
c.price, c.user_id, c.user_session,
    i.category_id, i.category_code, i.brand
FROM customers c
LEFT JOIN tmp_items i ON c.product_id = i.product_id
ORDER BY c.event_time;

DROP TABLE customers;

DROP TABLE tmp_items;

ALTER TABLE tmp_customers RENAME TO customers;
