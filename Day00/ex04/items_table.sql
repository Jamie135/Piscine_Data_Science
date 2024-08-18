CREATE TABLE IF NOT EXISTS items (
    product_id INT,
    category_id BIGINT,
    category_code VARCHAR(255),
    brand VARCHAR(255)
);

COPY items FROM '/tmp/item.csv' CSV HEADER;
