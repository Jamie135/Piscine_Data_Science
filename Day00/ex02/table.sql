CREATE TABLE IF NOT EXISTS data_2022_oct (
    event_time TIMESTAMP,
    event_type VARCHAR(255),
    product_id INT,
    -- category_id BIGINT,
    -- category_code VARCHAR,
    -- brand VARCHAR,
    price FLOAT,
    user_id BIGINT,
    user_session UUID
);

COPY data_2022_oct FROM '/tmp/data_2022_oct.csv' CSV HEADER;
