ALTER TABLE customers
ADD COLUMN category_id BIGINT,
ADD COLUMN category_code VARCHAR(255),
ADD COLUMN brand VARCHAR(255);

UPDATE customers c
LEFT JOIN items i
ON c.product_id = i.product_id
SET 
    c.category_id = i.category_id,
    c.category_code = i.category_code,
    c.brand = i.brand;
